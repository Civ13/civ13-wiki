"""Generate crawler-visible chapter previews after mdBook renders HTML."""
import argparse
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, urljoin, urlparse

BASE = 'https://civ13.github.io/civ13-wiki/'
IMAGE = 'https://civ13.github.io/public/img/banner.png'
SITE = 'Civilization 13 Wiki'
MARKER = '<!-- chapter-preview -->'


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = []
        self.paragraphs = []
        self.in_title = False
        self.in_main = False
        self.paragraph = None
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.in_title = True
        if tag == 'main':
            self.in_main = True
        if tag in ('script', 'style'):
            self.skip += 1
        if tag == 'p' and self.in_main:
            self.paragraph = []

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if tag == 'main':
            self.in_main = False
        if tag in ('script', 'style'):
            self.skip = max(0, self.skip - 1)
        if tag == 'p' and self.paragraph is not None:
            text = ' '.join(''.join(self.paragraph).split())
            if text:
                self.paragraphs.append(text)
            self.paragraph = None

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)
        if self.paragraph is not None and not self.skip:
            self.paragraph.append(data)


def serialize(payload):
    text = json.dumps(payload, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
    if len(text.encode('utf-8')) > 3000:
        raise ValueError('Preview exceeds 3000 UTF-8 bytes')
    return text


def metadata(title, description, canonical):
    # This intentionally emits only a fixed display-only website schema.
    if len(canonical) > 512:
        raise ValueError('Chapter URL exceeds link Button limit')
    payload = {'component': {'type': 17, 'components': [
        {'type': 10, 'content': '## ' + title},
        {'type': 10, 'content': description},
        {'type': 12, 'items': [{'media': {'url': IMAGE}, 'description': 'Civilization 13 banner'}]},
        {'type': 1, 'components': [{'type': 2, 'style': 5, 'label': 'Read this chapter', 'url': canonical}]},
    ]}}
    tags = [f'<link rel="canonical" href="{html.escape(canonical, quote=True)}">']
    values = {'description': description, 'og:title': title, 'og:description': description,
              'og:url': canonical, 'og:type': 'website', 'og:site_name': SITE,
              'og:image': IMAGE, 'og:image:alt': 'Civilization 13 banner',
              'twitter:card': 'summary_large_image', 'twitter:title': title,
              'twitter:description': description, 'twitter:image': IMAGE,
              'twitter:image:alt': 'Civilization 13 banner'}
    for name, value in values.items():
        attr = 'property' if name.startswith('og:') else 'name'
        tags.append(f'<meta {attr}="{name}" content="{html.escape(value, quote=True)}">')
    tags.append('<script id="discord:component-embed" type="application/json">' + serialize(payload) + '</script>')
    return '\n'.join(tags)


def generate(root, base=BASE):
    parsed = urlparse(base)
    if parsed.scheme not in ('http', 'https') or not parsed.netloc or parsed.query or parsed.fragment:
        raise ValueError('Base must be an absolute HTTP(S) URL without query or fragment')
    count = 0
    for path in sorted(root.rglob('*.html')):
        relative = path.relative_to(root).as_posix()
        source = path.read_text(encoding='utf-8')
        if path.name == 'toc.html':
            continue
        if MARKER not in source:
            raise ValueError(f'Missing preview build marker: {relative}')
        # mdBook utility pages are deliberately not advertised as chapters.
        if path.name in ('print.html', 'search.html', '404.html'):
            source = source.replace(MARKER, '')
        else:
            page = Page()
            page.feed(source)
            title = ''.join(page.title).strip()[:160]
            description = (page.paragraphs[0] if page.paragraphs else f'Read {title} in the {SITE}.')[:300]
            canonical = urljoin(base.rstrip('/') + '/', quote(relative, safe='/'))
            source = source.replace(MARKER, metadata(title, description, canonical))
            count += 1
        path.write_text(source, encoding='utf-8')
    print(f'Generated {count} chapter previews')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('book/html'))
    parser.add_argument('--base', default=BASE)
    args = parser.parse_args()
    generate(args.root, args.base)
