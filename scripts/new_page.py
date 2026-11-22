"""Create a wiki page from a template and list it in SUMMARY.md.

    python3 scripts/new_page.py guide "Guide to Beekeeping" --group "Food & Farming" --blurb "Wild nests, kept hives, honey and wax."
    python3 scripts/new_page.py map "Verdun" --group "Early Firearms (1650 to 1930)"
    python3 scripts/new_page.py gamemode "Train Raid"

The kind picks the template in templates/ and the folder (guides/, maps/,
gamemodes/). --group names an entry in SUMMARY.md (a guide section such as
"Food & Farming", or a map vote group) and appends the page as its last
child. Guides and maps need --group; a game mode defaults to "Game Modes".
A guide also needs --blurb, the one-line description shown on its section
page, which is saved to scripts/nav_blurbs.json. The generated navigation
blocks are refreshed afterwards.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'
KINDS = {
    'guide': ('guides', 'Guide_to_{}', None),
    'map': ('maps', '{}', None),
    'gamemode': ('gamemodes', '{}', 'Game Modes'),
}


def slug(title):
    words = re.sub(r'[^A-Za-z0-9]+', ' ', title).split()
    return '_'.join(words)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('kind', choices=sorted(KINDS))
    parser.add_argument('title')
    parser.add_argument('--group', help='SUMMARY.md entry to list the page under')
    parser.add_argument('--blurb', help='one-line description for a guide (required for guides)')
    parser.add_argument('--label', help='sidebar label (default: the title)')
    args = parser.parse_args()

    folder, pattern, default_group = KINDS[args.kind]
    group = args.group or default_group
    if not group:
        sys.exit(f'A {args.kind} needs --group: the SUMMARY.md entry to list it under')
    if args.kind == 'guide' and not args.blurb:
        sys.exit('A guide needs --blurb: its one-line description for the section page')
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
    starts = [i for i, line in enumerate(lines) if re.fullmatch(rf'(\s*)- \[{re.escape(group)}\]\([^)]*\)\s*', line)]
    if not starts:
        page.unlink()
        sys.exit(f'SUMMARY.md has no entry named {group!r}')
    start = starts[0]
    indent = len(lines[start]) - len(lines[start].lstrip())
    end = start + 1
    while end < len(lines) and (not lines[end].strip() or len(lines[end]) - len(lines[end].lstrip()) > indent):
        end += 1
    while end > start + 1 and not lines[end - 1].strip():
        end -= 1
    lines.insert(end, ' ' * (indent + 4) + f'- [{label}]({rel})')
    summary.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    if args.kind == 'guide':
        blurbs = ROOT / 'scripts' / 'nav_blurbs.json'
        data = json.loads(blurbs.read_text(encoding='utf-8'))
        data['pages'][rel] = args.blurb
        blurbs.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    subprocess.run([sys.executable, str(ROOT / 'scripts' / 'nav.py'), '--write'], check=True, cwd=ROOT)
    print(f'Created {page.relative_to(ROOT)} and listed it in SUMMARY.md as "{label}"')


if __name__ == '__main__':
    main()
