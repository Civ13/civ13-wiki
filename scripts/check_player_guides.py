"""Check current player guide content and rendered local links, including anchors."""
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

PAGES = ('index.md', 'New_Player_Guide.md', 'guides/Guide_to_Chemistry.md',
         'guides/Guide_to_Power.md', 'guides/Guide_to_Research.md',
         'gamemodes/Civilizations_and_Nomads.md', 'developers/Civ13_MCP.md',
         'guides/Guide_to_Farming.md', 'guides/Guide_to_Medical.md',
         'guides/Guide_to_Crafting.md', 'guides/Guide_to_Construction.md',
         'guides/Guide_to_Resource_Extraction.md', 'guides/Guide_to_Survival.md',
         'guides_overview.md', 'gamemodes/The_Art_of_the_Deal.md',
         'guides/Guide_to_Weapons.md')


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
    assert all(term in chemistry for term in ('15-second', '9:1 blend', 'Fruit Protease', 'additional-chemical-reactions'))
    assert all(term in power for term in ('30 PU', '10 PU', 'stored chemical state', 'Electricity'))
    # mdBook 0.4.x embeds navigation; newer local versions also emit toc.html.
    navigation = root / ('toc.html' if (root / 'toc.html').is_file() else 'index.html')
    nav_text = navigation.read_text(encoding='utf-8')
    assert 'Guide_to_Power.html' in nav_text and 'developers/Civ13_MCP.html' in nav_text
    assert 'Guide_to_Resource_Extraction.html' in nav_text and 'Guide_to_Survival.html' in nav_text
    print(f'Checked {len(PAGES)} player pages and {links} local links including fragments')


if __name__ == '__main__':
    check()
