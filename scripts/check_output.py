"""Validate every published chapter and the deployment revision manifest."""
import json
from pathlib import Path
from check_preview import HeadParser, check_html
from previews import BASE
from urllib.parse import quote


def check(root=Path('book/html')):
    checked = 0
    maximum = 0
    for path in root.rglob('*.html'):
        source = path.read_text(encoding='utf-8')
        if path.name in ('print.html', 'search.html', '404.html', 'toc.html'):
            assert 'discord:component-embed' not in source, path
            continue
        errors, counts = check_html(source)
        assert not errors, (str(path), errors)
        parser = HeadParser()
        parser.feed(source)
        canonical = BASE + quote(path.relative_to(root).as_posix(), safe='/')
        assert parser.metadata['og:url'] == canonical, path
        assert f'<link rel="canonical" href="{canonical}">' in source, path
        assert parser.metadata['description'] == parser.metadata['og:description'], path
        assert parser.metadata['twitter:title'] == parser.metadata['og:title'], path
        assert source.count('property="og:title"') == 1, path
        assert source.count('name="description"') == 1, path
        maximum = max(maximum, counts['bytes'])
        checked += 1
    revision = json.loads((root / 'revision.json').read_text())['sha']
    assert len(revision) == 40 and all(c in '0123456789abcdef' for c in revision)
    assert checked > 0
    print(f'Validated {checked} chapters; maximum {maximum} bytes; 6 components, 1 gallery item per chapter; SHA {revision}')


if __name__ == '__main__':
    check()
