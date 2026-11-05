"""Fail when the CI workflow's pinned tool list drifts from tools.json."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check():
    versions = {k: v for k, v in json.loads((ROOT / 'tools.json').read_text(encoding='utf-8')).items() if not k.startswith('_')}
    workflow = (ROOT / '.github/workflows/wiki.yml').read_text(encoding='utf-8')
    match = re.search(r'^\s*tool:\s*(.+)$', workflow, re.MULTILINE)
    assert match, 'install-action tool list not found in wiki.yml'
    pinned = dict(item.strip().split('@') for item in match.group(1).split(','))
    assert pinned == versions, f'wiki.yml pins {pinned} but tools.json pins {versions}'
    book = (ROOT / 'book.toml').read_text(encoding='utf-8')
    for name in re.findall(r'^\[preprocessor\.(\w+)\]', book, re.MULTILINE):
        assert f'mdbook-{name}' in versions, f'book.toml enables preprocessor {name} that tools.json does not pin'
    print(f'tools.json and wiki.yml agree on {len(versions)} tools')


if __name__ == '__main__':
    check()
