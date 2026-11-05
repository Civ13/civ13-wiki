"""List changed pages that in-game Player Help pins, so reviewers know a Civ13 re-pin follows.

Usage: python3 scripts/check_pinned_changes.py <base-ref> [<head-ref>]
Compares the two trees directly (no merge base needed), so on a pull_request
checkout with fetch-depth 2 pass `HEAD^1 HEAD` to diff the merge commit against
its base. Reads the pin list from Civ13's scripts/player_help_bridge.py (public, fetched
over HTTPS; pass --bridge <path> to use a local copy). Never fails the build:
it prints the list, writes it to the GitHub job summary when available, and
emits a notice annotation.
"""
import argparse
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

BRIDGE_URL = 'https://raw.githubusercontent.com/Civ13/Civ13/master/scripts/player_help_bridge.py'
ROOT = Path(__file__).resolve().parents[1]


def pinned_pages(bridge_source):
    block = re.search(r'WIKI_REVIEWED_GUIDES\s*=\s*\{(.*?)\n\}', bridge_source, re.DOTALL)
    legacy = re.search(r'WIKI_LEGACY_GUIDES\s*=\s*\((.*?)\)', bridge_source, re.DOTALL)
    pages = set(re.findall(r"^\s*'([^']+\.md)'\s*:", block.group(1), re.MULTILINE)) if block else set()
    if legacy:
        pages |= set(re.findall(r"'([^']+\.md)'", legacy.group(1)))
    return pages


def changed_files(base, head):
    result = subprocess.run(['git', 'diff', '--name-only', base, head], cwd=ROOT, capture_output=True, text=True)
    if result.returncode:
        print(f'::warning::git diff {base} {head} failed ({result.stderr.strip()}); skipping the pinned-guide check')
        return None
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('base')
    parser.add_argument('head', nargs='?', default='HEAD')
    parser.add_argument('--bridge', type=Path, help='local copy of Civ13 scripts/player_help_bridge.py')
    args = parser.parse_args()
    if args.bridge:
        source = args.bridge.read_text(encoding='utf-8')
    else:
        try:
            with urllib.request.urlopen(BRIDGE_URL, timeout=60) as response:
                source = response.read().decode('utf-8')
        except OSError as error:
            print(f'::warning::Could not fetch the Civ13 pin list ({error}); skipping the pinned-guide check')
            return 0
    pinned = pinned_pages(source)
    if not pinned:
        print('::warning::No pinned guides found in player_help_bridge.py; skipping')
        return 0
    files = changed_files(args.base, args.head)
    if files is None:
        return 0
    changed = [path for path in files if path.startswith('src/') and path[len('src/'):] in pinned]
    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if not changed:
        print(f'No pinned Player Help guide changed ({len(pinned)} pinned pages checked)')
        return 0
    lines = ['## Player Help pins', '',
             'These pages are pinned by Civ13 Player Help; after merge the Civ13 "Player Help wiki re-pin" '
             'workflow (or `python3 scripts/agent_preflight.py wiki-pins --wiki-root <wiki> --write`) must refresh them, '
             'otherwise in-game Help stops serving them:', '']
    lines += [f'- `{path}`' for path in changed]
    text = '\n'.join(lines)
    print(text)
    if summary:
        Path(summary).open('a', encoding='utf-8').write(text + '\n')
    print(f'::notice title=Player Help re-pin needed::{len(changed)} pinned guide(s) changed: ' + ', '.join(changed))
    return 0


if __name__ == '__main__':
    sys.exit(main())
