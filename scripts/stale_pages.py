"""List wiki pages that have not been touched or reviewed for a long time.

A page's age is the date of its last commit, unless it carries a review
marker on its own line, which wins when newer:

    <!-- reviewed: 2026-11-05 -->

    python3 scripts/stale_pages.py              # pages older than 12 months
    python3 scripts/stale_pages.py --months 6 --markdown > report.md

Needs full git history (`fetch-depth: 0` in CI). Pages with no commit date
(not yet committed) are skipped.
"""
import argparse
import datetime as dt
import re
import subprocess
from pathlib import Path

SRC = Path('src')
MARKER = re.compile(r'^<!-- reviewed: (\d{4}-\d{2}-\d{2}) -->\s*$', re.M)
SKIP = {'SUMMARY.md', '404.md'}


def last_commit_dates():
    out = subprocess.check_output(['git', 'log', '--format=%x00%cs', '--name-only', '--', 'src'], text=True)
    dates, current = {}, None
    for line in out.splitlines():
        if line.startswith('\x00'):
            current = line[1:]
        elif line and line not in dates:
            dates[line] = current
    return dates


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--months', type=int, default=12)
    parser.add_argument('--markdown', action='store_true', help='print a Markdown table instead of plain lines')
    args = parser.parse_args()
    cutoff = dt.date.today() - dt.timedelta(days=30 * args.months)
    commits = last_commit_dates()
    stale = []
    for page in sorted(SRC.rglob('*.md')):
        rel = page.relative_to(SRC).as_posix()
        if rel in SKIP:
            continue
        committed = commits.get(f'src/{rel}')
        if not committed:
            continue
        age = dt.date.fromisoformat(committed)
        marker = MARKER.search(page.read_text(encoding='utf-8'))
        if marker:
            age = max(age, dt.date.fromisoformat(marker.group(1)))
        if age < cutoff:
            stale.append((age, rel))
    stale.sort()
    if args.markdown:
        print(f'{len(stale)} pages have not been edited or marked reviewed in {args.months} months '
              f'(cutoff {cutoff}). Edit the page, or add `<!-- reviewed: YYYY-MM-DD -->` after checking it against the game.\n')
        if stale:
            print('| Last touched | Page |')
            print('| --- | --- |')
            for age, rel in stale:
                print(f'| {age} | [{rel}](https://github.com/civ13/civ13-wiki/blob/master/src/{rel}) |')
    else:
        for age, rel in stale:
            print(f'{age}  {rel}')
        print(f'{len(stale)} pages older than {args.months} months (cutoff {cutoff})')


if __name__ == '__main__':
    main()
