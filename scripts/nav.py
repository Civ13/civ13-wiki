"""Keep the overview pages in step with src/SUMMARY.md.

SUMMARY.md is the single source of truth for navigation. Group headings there
are draft chapters (`- [Group]()`) with the pages nested under them. This
script renders those groups into the overview pages between marker comments:

    <!-- nav:Guides Overview -->
    ...generated...
    <!-- /nav -->

`--write` regenerates the blocks in place; `--check` (the CI default) fails
when a block is stale, a page is missing from SUMMARY.md, a SUMMARY.md entry
points at a missing file, or a page is listed twice.
"""
import argparse
import os
import re
import sys
from pathlib import Path

SRC = Path('src')
SUMMARY = SRC / 'SUMMARY.md'
UNLISTED = {'SUMMARY.md', '404.md'}
ENTRY = re.compile(r'^(\s*)- \[([^\]]+)\]\(([^)]*)\)\s*$')
BLOCK = re.compile(r'(<!-- nav:([^>]+?) -->\n)(.*?)(<!-- /nav -->)', re.S)


class Node:
    def __init__(self, title, path, depth):
        self.title = title
        self.path = path
        self.depth = depth
        self.children = []


def parse(text=None):
    """Return the top-level nodes of SUMMARY.md, with parts flattened."""
    text = SUMMARY.read_text(encoding='utf-8') if text is None else text
    roots = []
    stack = []
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith('#'):
            continue
        match = ENTRY.match(line)
        if not match:
            raise SystemExit(f'SUMMARY.md:{number}: cannot parse {line!r}')
        indent, title, path = match.groups()
        depth = len(indent.replace('\t', '    ')) // 4
        node = Node(title, path, depth)
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
    for node in walk(nodes):
        if node.title == title:
            return node
    raise SystemExit(f'SUMMARY.md has no entry titled {title!r}')


def relative(target, page):
    """Rewrite a SUMMARY.md path (relative to src/) for a page's own folder."""
    return Path(os.path.relpath(SRC / target, (SRC / page).parent)).as_posix()


def render(node, page):
    """Render a node's child groups as sections for the given overview page."""
    lines = []
    for group in node.children:
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
    for page in sorted(SRC.rglob('*.md')):
        text = page.read_text(encoding='utf-8')
        if '<!-- nav:' not in text:
            continue
        rel = page.relative_to(SRC).as_posix()

        def replace(match):
            return match.group(1) + render(find(roots, match.group(2)), rel) + match.group(4)

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
