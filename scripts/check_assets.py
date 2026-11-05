"""Check the Git LFS asset contract: every release-hosted link in src/ matches an LFS-tracked file and nothing links LFS files locally."""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELEASE = 'https://github.com/civ13/civ13-wiki/releases/download/assets/'


def lfs_files():
    out = subprocess.run(['git', 'lfs', 'ls-files', '--name-only'], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return [Path(line.strip()) for line in out.splitlines() if line.strip()]


def check():
    tracked = lfs_files()
    assert tracked, 'no Git LFS files found; is git-lfs installed?'
    names = {}
    for path in tracked:
        assert path.name not in names, f'LFS asset basename {path.name} is not unique: {path} and {names[path.name]}'
        names[path.name] = path
    linked = set()
    for page in (ROOT / 'src').rglob('*.md'):
        text = page.read_text(encoding='utf-8')
        for name in re.findall(re.escape(RELEASE) + r'([\w.%-]+)', text):
            assert name in names, f'{page.relative_to(ROOT)} links release asset {name} that is not LFS-tracked'
            linked.add(name)
        for path in tracked:
            assert not re.search(r'(?:images|video)/[\w./-]*' + re.escape(path.name), text), \
                f'{page.relative_to(ROOT)} references LFS file {path.name} by local path; link {RELEASE}{path.name} instead'
    print(f'{len(tracked)} LFS assets, {len(linked)} linked from pages')


if __name__ == '__main__':
    check()
