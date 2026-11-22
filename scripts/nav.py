"""Keep the overview pages in step with src/SUMMARY.md.

SUMMARY.md is the single source of truth for navigation. Group headings there
are draft chapters (`- [Group]()`) with the pages nested under them. This
script renders those groups into the overview pages between marker comments:

    <!-- nav:Guides Overview -->
    ...generated...
    <!-- /nav -->

A title starting with `#` names a part, so `<!-- nav:#Guides -->` renders the
sections listed under `# Guides`. Two more block kinds use the one-line
descriptions in scripts/nav_blurbs.json:

    <!-- nav-list:Start Here -->   a section's pages, each with its description
    <!-- nav-cards:#Guides -->     a card per section, for the main page

Every section and page under `# Guides` needs a description there.

`--write` regenerates the blocks in place; `--check` (the CI default) fails
when a block is stale, a page is missing from SUMMARY.md, a SUMMARY.md entry
points at a missing file, or a page is listed twice.
"""
import argparse
import html
import json
import os
import re
import sys
from pathlib import Path

SRC = Path('src')
SUMMARY = SRC / 'SUMMARY.md'
UNLISTED = {'SUMMARY.md', '404.md'}
BLURBS = Path(__file__).resolve().parent / 'nav_blurbs.json'
DESCRIBED_PART = 'Guides'
ENTRY = re.compile(r'^(\s*)- \[([^\]]+)\]\(([^)]*)\)\s*$')
BLOCK = re.compile(r'(<!-- (nav|nav-list|nav-cards):([^>]+?) -->\n)(.*?)(<!-- /nav -->)', re.S)


class Node:
    def __init__(self, title, path, depth, part=None):
        self.title = title
        self.path = path
        self.depth = depth
        self.part = part
        self.children = []


def parse(text=None):
    """Return the top-level nodes of SUMMARY.md, with parts flattened."""
    text = SUMMARY.read_text(encoding='utf-8') if text is None else text
    roots = []
    stack = []
    part = None
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith('# '):
            part = line[2:].strip()
            continue
        if not line.strip() or line.startswith('#'):
            continue
        match = ENTRY.match(line)
        if not match:
            raise SystemExit(f'SUMMARY.md:{number}: cannot parse {line!r}')
        indent, title, path = match.groups()
        depth = len(indent.replace('\t', '    ')) // 4
        node = Node(title, path, depth, part)
        while stack and stack[-1].depth >= depth:
            stack.pop()
        (stack[-1].children if stack else roots).append(node)
        stack.append(node)
    return roots


def walk(nodes):
    for node in nodes:
        yield node
        yield from walk(node.children)


def find(nodes, title):
    if title.startswith('#'):
        members = [node for node in nodes if node.part == title[1:]]
        if not members:
            raise SystemExit(f'SUMMARY.md has no part titled {title[1:]!r}')
        return Node(title[1:], '', -1, title[1:]), members
    for node in walk(nodes):
        if node.title == title:
            return node, node.children
    raise SystemExit(f'SUMMARY.md has no entry titled {title!r}')


def blurbs():
    return json.loads(BLURBS.read_text(encoding='utf-8'))


def relative(target, page):
    """Rewrite a SUMMARY.md path (relative to src/) for a page's own folder."""
    return Path(os.path.relpath(SRC / target, (SRC / page).parent)).as_posix()


def render_list(children, page, data):
    """Render pages as a described list, nesting one level of subpages."""
    lines = []

    def emit(items, indent):
        for item in items:
            blurb = data['pages'].get(item.path, '')
            text = f'{indent}- **[{item.title}]({relative(item.path, page)})**'
            lines.append(f'{text}: {blurb}' if blurb else text)
            emit(item.children, indent + '    ')

    emit(children, '')
    lines.append('')
    return '\n'.join(lines)


def render_cards(sections, page, data):
    """Render one card per section: icon, title, description and every page."""
    lines = ['<div class="wiki-topic-grid">']
    for section in sections:
        meta = data['sections'].get(section.path, {})
        icon = relative('images/icons/' + meta.get('icon', 'guides') + '.png', page)
        links = ''.join(f'<li><a href="{relative(item.path, page)}">{html.escape(item.title)}</a></li>'
                        for item in section.children)
        lines.append(
            f'<section class="wiki-topic"><h3><img src="{icon}" alt="" width="36" height="36">'
            f'<a href="{relative(section.path, page)}">{html.escape(section.title)}</a></h3>'
            f'<p>{html.escape(meta.get("blurb", ""))}</p><ul>{links}</ul></section>')
    lines.append('</div>')
    lines.append('')
    return '\n'.join(lines)


def render(children, page):
    """Render child groups as sections for the given overview page."""
    lines = []
    for group in children:
        heading = f'[{group.title}]({relative(group.path, page)})' if group.path else group.title
        lines.append(f'## {heading}')
        lines.append('')
        for item in group.children:
            lines.append(f'- [{item.title}]({relative(item.path, page)})')
        if not group.children:
            lines.append(f'- [{group.title}]({relative(group.path, page)})')
        lines.append('')
    return '\n'.join(lines)


def update(roots, write):
    stale = []
    data = blurbs()
    for page in sorted(SRC.rglob('*.md')):
        text = page.read_text(encoding='utf-8')
        if '<!-- nav' not in text:
            continue
        rel = page.relative_to(SRC).as_posix()

        def replace(match):
            kind = match.group(2)
            children = find(roots, match.group(3))[1]
            if kind == 'nav-list':
                body = render_list(children, rel, data)
            elif kind == 'nav-cards':
                body = render_cards(children, rel, data)
            else:
                body = render(children, rel)
            return match.group(1) + body + match.group(5)

        updated = BLOCK.sub(replace, text)
        if updated != text:
            stale.append(rel)
            if write:
                page.write_text(updated, encoding='utf-8')
    return stale


def check(roots):
    problems = []
    seen = {}
    for node in walk(roots):
        if not node.path:
            continue
        if node.path in seen:
            problems.append(f'{node.path} is listed twice in SUMMARY.md ({seen[node.path]!r} and {node.title!r})')
        seen[node.path] = node.title
        if not (SRC / node.path).is_file():
            problems.append(f'SUMMARY.md links to missing page {node.path}')
    data = blurbs()
    for section in roots:
        if section.part != DESCRIBED_PART:
            continue
        if not data['sections'].get(section.path, {}).get('blurb'):
            problems.append(f'{section.path} has no section description in scripts/nav_blurbs.json')
        icon = data['sections'].get(section.path, {}).get('icon', 'guides')
        if not (SRC / 'images' / 'icons' / f'{icon}.png').is_file():
            problems.append(f'{section.path} names a missing icon {icon!r} in scripts/nav_blurbs.json')
        for node in walk(section.children):
            if not data['pages'].get(node.path):
                problems.append(f'{node.path} has no description in scripts/nav_blurbs.json')
    listed = set(seen)
    for path in list(data['sections']) + list(data['pages']):
        if path not in listed:
            problems.append(f'scripts/nav_blurbs.json describes {path}, which SUMMARY.md does not list')
    for page in sorted(SRC.rglob('*.md')):
        rel = page.relative_to(SRC).as_posix()
        if rel not in seen and rel not in UNLISTED:
            problems.append(f'{rel} is not listed in SUMMARY.md (add it or delete the page)')
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--write', action='store_true', help='regenerate the overview blocks in place')
    args = parser.parse_args()
    roots = parse()
    problems = check(roots)
    stale = update(roots, args.write)
    if args.write:
        for page in stale:
            print(f'Updated {page}')
    else:
        problems.extend(f'{page}: generated navigation block is stale; run python3 scripts/nav.py --write'
                        for page in stale)
    for problem in problems:
        print(f'ERROR: {problem}', file=sys.stderr)
    if problems:
        sys.exit(1)
    listed = sum(1 for node in walk(roots) if node.path)
    print(f'Navigation OK: {listed} pages in SUMMARY.md, {len(stale)} overview block(s) {"updated" if args.write else "current"}')


if __name__ == '__main__':
    main()
