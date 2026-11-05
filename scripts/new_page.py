"""Create a wiki page from a template and list it in SUMMARY.md.

    python3 scripts/new_page.py guide "Guide to Beekeeping" --group "Food & Animals"
    python3 scripts/new_page.py map "Verdun" --group "Early Firearms (1650 to 1930)"
    python3 scripts/new_page.py gamemode "Train Raid"

The kind picks the template in templates/ and the folder (guides/, maps/,
gamemodes/). --group names a draft group in SUMMARY.md (`- [Group]()`) and
appends the page as its last child; without it, the page is appended to the
part the kind belongs to. The overview pages are regenerated afterwards.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'
KINDS = {
    'guide': ('guides', 'Guide_to_{}', '# Guides'),
    'map': ('maps', '{}', '# Maps & Scenarios'),
    'gamemode': ('gamemodes', '{}', '# Gamemodes'),
}


def slug(title):
    words = re.sub(r'[^A-Za-z0-9]+', ' ', title).split()
    return '_'.join(words)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('kind', choices=sorted(KINDS))
    parser.add_argument('title')
    parser.add_argument('--group', help='draft group in SUMMARY.md to list the page under')
    parser.add_argument('--label', help='sidebar label (default: the title)')
    args = parser.parse_args()

    folder, pattern, part = KINDS[args.kind]
    title = args.title
    if args.kind == 'guide':
        title = re.sub(r'^Guide to ', '', title, flags=re.I)
    name = pattern.format(slug(title)) + '.md'
    page = SRC / folder / name
    if page.exists():
        sys.exit(f'{page.relative_to(ROOT)} already exists')
    template = (ROOT / 'templates' / f'{args.kind}.md').read_text(encoding='utf-8')
    page.write_text(template.replace('{title}', args.title), encoding='utf-8')

    summary = SRC / 'SUMMARY.md'
    lines = summary.read_text(encoding='utf-8').splitlines()
    label = args.label or title
    rel = f'{folder}/{name}'
    if args.group:
        starts = [i for i, line in enumerate(lines) if re.fullmatch(rf'(\s*)- \[{re.escape(args.group)}\]\(\)\s*', line)]
        if not starts:
            page.unlink()
            sys.exit(f'SUMMARY.md has no draft group named {args.group!r}')
        start = starts[0]
        indent = len(lines[start]) - len(lines[start].lstrip())
        end = start + 1
        while end < len(lines) and (not lines[end].strip() or len(lines[end]) - len(lines[end].lstrip()) > indent):
            end += 1
        while end > start + 1 and not lines[end - 1].strip():
            end -= 1
        lines.insert(end, ' ' * (indent + 4) + f'- [{label}]({rel})')
    else:
        try:
            start = lines.index(part)
        except ValueError:
            page.unlink()
            sys.exit(f'SUMMARY.md has no part {part!r}')
        end = start + 1
        while end < len(lines) and not lines[end].startswith('# '):
            end += 1
        while end > start + 1 and not lines[end - 1].strip():
            end -= 1
        lines.insert(end, f'- [{label}]({rel})')
    summary.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    subprocess.run([sys.executable, str(ROOT / 'scripts' / 'nav.py'), '--write'], check=True, cwd=ROOT)
    print(f'Created {page.relative_to(ROOT)} and listed it in SUMMARY.md as "{label}"')


if __name__ == '__main__':
    main()
