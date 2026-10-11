"""Check current player guide content and rendered local links, including anchors."""
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

PAGES = ('index.md', 'New_Player_Guide.md', 'guides/Guide_to_Chemistry.md',
         'guides/Guide_to_Power.md', 'guides/Guide_to_Research.md',
         'gamemodes/Civilizations_and_Nomads.md')


def check(root=Path('book/html')):
    links = 0
    for page in PAGES:
        source = (Path('src') / page).read_text(encoding='utf-8')
        assert 'Persistence' not in source and 'valzargaming.com:1714' not in source, page
        rendered = root / Path(page).with_suffix('.html')
        html = rendered.read_text(encoding='utf-8')
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', source):
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            path = rendered.parent / unquote(url.path) if url.path else rendered
            if path.suffix == '.md':
                path = path.with_suffix('.html')
            assert path.is_file(), (page, target)
            if url.fragment:
                contents = path.read_text(encoding='utf-8') if path != rendered else html
                assert f'id="{unquote(url.fragment)}"' in contents, (page, target)
            links += 1
    chemistry = (root / 'guides/Guide_to_Chemistry.html').read_text(encoding='utf-8')
    power = (root / 'guides/Guide_to_Power.html').read_text(encoding='utf-8')
    assert all(term in chemistry for term in ('15-second', '9:1 blend', 'Fruit Protease', 'historical-chemical-reactions-export'))
    assert all(term in power for term in ('30 PU', '10 PU', 'stored chemical state', 'Electricity'))
    assert 'Guide_to_Power.html' in (root / 'toc.html').read_text(encoding='utf-8')
    print(f'Checked {len(PAGES)} player pages and {links} local links including fragments')


if __name__ == '__main__':
    check()
