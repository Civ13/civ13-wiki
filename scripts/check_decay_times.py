"""Compare the Food Decay Times page with the decay values in the game source.

The page is hand-curated (sprites, biomes, uses, reactions), so it is not
regenerated; this check reports rows whose "Decay (minutes)" cell no longer
matches `decay` on the matching food type in a Civ13 checkout, and rows whose
label matches no food name. It is advisory: the report goes to the job
summary and the exit code is 0 unless `--strict` is given.

    python3 scripts/check_decay_times.py --civ13 ../Civ13
"""
import argparse
import html
import os
import re
import sys
from pathlib import Path

PAGE = Path('src/Food_Decay_Times.md')
FOOD = Path('code/modules/reagents/reagent_containers/food')
TICK = 600  # deciseconds per minute; `decay` is declared as minutes*600


def load_food_types(root):
    """Return {typepath: (name, decay)} with values inherited along the path."""
    declared = {}
    for path in sorted((root / FOOD).rglob('*.dm')):
        current = None
        for line in path.read_text(encoding='utf-8', errors='replace').splitlines():
            line = re.sub(r'//.*', '', line).rstrip()
            match = re.match(r'^(/obj/item/weapon/reagent_containers/food[^\s(]*)', line)
            if match:
                current = match.group(1).rstrip('/')
                declared.setdefault(current, {})
                continue
            if current is None or not line.startswith('\t'):
                continue
            match = re.match(r'^\tname\s*=\s*"([^"]*)"', line)
            if match:
                declared[current]['name'] = match.group(1)
            match = re.match(r'^\tdecay\s*=\s*([0-9*+\- ()]+)$', line)
            if match:
                declared[current]['decay'] = eval(match.group(1), {'__builtins__': {}})  # digits and operators only

    def inherited(typepath, key):
        parts = typepath.split('/')
        while len(parts) > 1:
            value = declared.get('/'.join(parts), {}).get(key)
            if value is not None:
                return value
            parts.pop()
        return None

    return {typepath: (inherited(typepath, 'name'), inherited(typepath, 'decay') or 0) for typepath in declared}


def page_rows():
    """Yield (label, minutes or None) for every table row with a bold label and a decay cell."""
    text = PAGE.read_text(encoding='utf-8')
    for row in re.split(r'<tr>', text)[1:]:
        row = row.split('</tr>')[0]
        label = re.search(r'<b>([^<]+)</b>', row)
        cells = re.findall(r'<td[^>]*>\s*(.*?)\s*</td>', row, re.S)
        if not label or not cells:
            continue
        # Decay is the cell right after the label; meat and seafood rows add a rot column and an image after it.
        label_cell = next((i for i, cell in enumerate(cells) if '<b>' in cell), len(cells) - 1)
        decay_cell = cells[label_cell + 1] if label_cell + 1 < len(cells) else cells[-1]
        value = html.unescape(re.sub(r'<[^>]+>', '', decay_cell)).strip()
        minutes = int(value) if re.fullmatch(r'\d+', value) else None
        yield html.unescape(label.group(1)).strip(), minutes


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--civ13', type=Path, required=True, help='path to a Civ13 checkout')
    parser.add_argument('--strict', action='store_true', help='exit 1 when any row differs')
    args = parser.parse_args()
    types = load_food_types(args.civ13)
    by_name = {}
    for name, decay in types.values():
        if name:
            by_name.setdefault(name.lower(), set()).add(decay)
    matched, mismatched, unmatched = 0, [], []
    for label, minutes in page_rows():
        decays = by_name.get(label.lower())
        if not decays:
            unmatched.append(label)
            continue
        matched += 1
        expected = sorted(d // TICK if d else 0 for d in decays)
        if minutes is None:
            if any(expected):
                mismatched.append((label, '-', expected))
        elif minutes not in expected:
            mismatched.append((label, minutes, expected))
    lines = [f'Food Decay Times: {matched} rows matched a food type, {len(mismatched)} differ, '
             f'{len(unmatched)} labels have no exact name match.']
    if mismatched:
        lines += ['', '| Row | Page (minutes) | Source (minutes) |', '| --- | --- | --- |']
        lines += [f'| {label} | {page} | {", ".join(str(e) for e in expected)} |' for label, page, expected in mismatched]
    print('\n'.join(lines))
    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        Path(summary).open('a', encoding='utf-8').write('### ' + '\n'.join(lines) + '\n')
    if mismatched and args.strict:
        sys.exit(1)


if __name__ == '__main__':
    main()
