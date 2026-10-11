"""Read-only guards for emitted inline Discord preview HTML; no network or full schema validation."""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


def script_json(payload):
    """Serialize safely for an HTML script and reject an oversized emitted payload."""
    text = json.dumps(payload, ensure_ascii=False, separators=(',', ':'), allow_nan=False)
    text = text.replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    if len(text.encode('utf-8')) > 3000:
        raise ValueError('serialized payload exceeds 3000 UTF-8 bytes')
    return text


def web_url(value, maximum=2048):
    if not isinstance(value, str) or len(value) > maximum or any(c.isspace() for c in value):
        return False
    try:
        url = urlsplit(value)
        return url.scheme in ('http', 'https') and bool(url.hostname) and not url.username and not url.password
    except ValueError:
        return False


def validate_payload(raw):
    errors = []
    counts = {'bytes': len(raw.encode('utf-8')), 'components': 0, 'gallery_items': 0}
    if counts['bytes'] > 3000:
        errors.append('payload exceeds 3000 UTF-8 bytes')
    if '<' in raw:
        errors.append('literal < in script JSON; serialize with Unicode escaping')
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('duplicate JSON key: ' + key)
            result[key] = value
        return result
    try:
        payload = json.loads(raw, object_pairs_hook=unique_object,
                             parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
    except (ValueError, RecursionError) as exc:
        return errors + ['invalid JSON: ' + str(exc)], counts
    if not isinstance(payload, dict) or set(payload) != {'component'}:
        return errors + ['expected a single component property'], counts

    def media(value, thumbnail=False):
        if not isinstance(value, dict) or not web_url(value.get('url')):
            errors.append('media needs an absolute HTTP(S) URL of at most 2048 characters')
            return
        suffix = Path(urlsplit(value['url']).path).suffix.lower()
        formats = {'.png', '.gif', '.jpg', '.jpeg', '.webp', '.avif'}
        if not thumbnail:
            formats |= {'.mp4', '.webm', '.mov'}
        if suffix == '.svg':
            errors.append('SVG preview media is unsupported')
        elif suffix and suffix not in formats:
            errors.append('unsupported media extension: ' + suffix)
        # Extensionless assets need separate response Content-Type verification.

    def visit(node, allowed, root=False):
        if not isinstance(node, dict):
            errors.append('component must be an object')
            return
        counts['components'] += 1
        kind = node.get('type')
        if type(kind) is not int or kind not in allowed:
            errors.append('unsupported component type or placement: ' + str(kind))
            return
        if 'custom_id' in node:
            errors.append('custom_id is forbidden in website previews')
        if kind in (17, 1, 9):
            children = node.get('components')
            if not isinstance(children, list) or not children:
                errors.append('layout needs a nonempty components array')
                children = []
            if kind == 17:
                if not root:
                    errors.append('nested Container')
                allowed_children = {1, 9, 10, 12, 14}
            elif kind == 1:
                allowed_children = {2}
                if len(children) > 5:
                    errors.append('Action Row exceeds five buttons')
            else:
                allowed_children = {10}
                if not 1 <= len(children) <= 3:
                    errors.append('Section requires one to three Text Displays')
                visit(node.get('accessory'), {2, 11})
            for child in children:
                visit(child, allowed_children)
        elif kind == 2:
            allowed_keys = {'id', 'type', 'url', 'style', 'label', 'emoji', 'disabled'}
            if set(node) - allowed_keys:
                errors.append('Button contains forbidden keys')
            if type(node.get('style')) is not int or node['style'] != 5:
                errors.append('Button must use link style 5')
            if 'disabled' in node and type(node['disabled']) is not bool:
                errors.append('Button disabled must be boolean')
            if not web_url(node.get('url'), 512):
                errors.append('Button needs an absolute HTTP(S) URL of at most 512 characters')
            label = node.get('label')
            if label is not None and (not isinstance(label, str) or not 1 <= len(label) <= 80):
                errors.append('Button label must contain 1 to 80 characters')
            emoji = node.get('emoji')
            if not label and not (isinstance(emoji, dict) and (emoji.get('name') or emoji.get('id'))):
                errors.append('Button needs a label and/or emoji')
        elif kind == 10:
            if not isinstance(node.get('content'), str) or not node['content']:
                errors.append('Text Display needs nonempty string content')
        elif kind == 11:
            media(node.get('media'), thumbnail=True)
        elif kind == 12:
            items = node.get('items')
            if not isinstance(items, list) or not 1 <= len(items) <= 10:
                errors.append('Media Gallery requires one to ten items')
                items = items if isinstance(items, list) else []
            counts['gallery_items'] += len(items)
            for item in items:
                media(item.get('media') if isinstance(item, dict) else None)
        elif kind == 14:
            if 'spacing' in node and (type(node['spacing']) is not int or node['spacing'] not in (1, 2)):
                errors.append('Separator spacing must be 1 or 2')

    visit(payload['component'], {17}, root=True)
    if counts['components'] > 40:
        errors.append('preview exceeds 40 components including root/accessories')
    if counts['gallery_items'] > 10:
        errors.append('preview exceeds ten total gallery items')
    return errors, counts


class HeadParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_head = False
        self.head_count = 0
        self.closed_heads = 0
        self.script = None
        self.scripts = []
        self.metadata = {}
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'head':
            self.head_count += 1
            if self.in_head or self.head_count > 1:
                self.errors.append('duplicate or nested head element')
            self.in_head = True
        if tag == 'body' and self.in_head:
            self.errors.append('body starts before head closes')
        if tag == 'meta' and self.in_head:
            key = attrs.get('name', attrs.get('property'))
            value = attrs.get('content', attrs.get('value', ''))
            if key and value and not self.metadata.get(key):
                self.metadata[key] = value
        if tag == 'script' and attrs.get('id') == 'discord:component-embed':
            if not self.in_head:
                self.errors.append('component script is outside head')
            if attrs.get('type') not in ('application/json', 'application/vnd.discord.component-embed+json'):
                self.errors.append('component script has incorrect MIME type')
            self.script = []

    def handle_data(self, data):
        if self.script is not None:
            self.script.append(data)

    def handle_endtag(self, tag):
        if tag == 'head':
            if not self.in_head:
                self.errors.append('head closes without an open head')
            self.closed_heads += 1
            self.in_head = False
        if tag == 'script' and self.script is not None:
            self.scripts.append(''.join(self.script))
            self.script = None


def check_html(html):
    parser = HeadParser()
    parser.feed(html)
    parser.close()
    errors = parser.errors
    counts = {}
    if parser.head_count != 1 or parser.closed_heads != 1 or parser.in_head:
        errors.append('expected one explicitly closed head element')
    if parser.script is not None:
        errors.append('unterminated component script')
    if len(parser.scripts) != 1:
        errors.append('expected exactly one inline component script')
    for raw in parser.scripts:
        found, counts = validate_payload(raw)
        errors.extend(found)
    for key in ('og:title', 'og:description', 'og:image', 'og:url', 'og:type', 'og:site_name', 'twitter:card'):
        if not parser.metadata.get(key):
            errors.append('missing fallback metadata: ' + key)
    for key in ('og:image', 'og:url'):
        if key in parser.metadata and not web_url(parser.metadata[key]):
            errors.append('fallback needs an absolute HTTP(S) URL: ' + key)
    if parser.metadata.get('twitter:card') not in (None, 'summary', 'summary_large_image', 'player', 'photo'):
        errors.append('invalid twitter:card value')
    if 'og:image' in parser.metadata and urlsplit(parser.metadata['og:image']).path.lower().endswith('.svg'):
        errors.append('SVG fallback image is unsupported')
    return errors, counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pages', nargs='+', type=Path)
    args = parser.parse_args()
    failed = False
    for page in args.pages:
        try:
            errors, counts = check_html(page.read_text(encoding='utf-8'))
        except (OSError, UnicodeError, ValueError, RecursionError) as exc:
            errors, counts = [str(exc)], {}
        print(json.dumps({'page': str(page), 'errors': errors, 'counts': counts}))
        failed |= bool(errors)
    return int(failed)


if __name__ == '__main__':
    raise SystemExit(main())
