"""Install the pinned mdBook toolchain from tools.json into ./tools (gitignored).

Prebuilt release binaries are downloaded for mdbook, mdbook-admonish and
mdbook-linkcheck. mdbook-emojicodes publishes no binaries, so it is built with
`cargo install` when cargo is available. Run `python3 scripts/setup_tools.py`
(Windows: `py -3 scripts/setup_tools.py`), then add ./tools to PATH, or use
`python3 scripts/setup_tools.py --run serve` to run mdbook with ./tools first on PATH.
"""
import argparse
import io
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tarfile
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / 'tools'
WINDOWS = platform.system() == 'Windows'
EXE = '.exe' if WINDOWS else ''


def target():
    machine = platform.machine().lower()
    arm = machine in ('arm64', 'aarch64')
    if WINDOWS:
        return 'x86_64-pc-windows-msvc'
    if platform.system() == 'Darwin':
        return 'aarch64-apple-darwin' if arm else 'x86_64-apple-darwin'
    return 'aarch64-unknown-linux-gnu' if arm else 'x86_64-unknown-linux-gnu'


def urls(versions):
    t = target()
    archive = 'zip' if WINDOWS else 'tar.gz'
    return {
        'mdbook': f"https://github.com/rust-lang/mdBook/releases/download/v{versions['mdbook']}/mdbook-v{versions['mdbook']}-{t}.{archive}",
        'mdbook-admonish': f"https://github.com/tommilligan/mdbook-admonish/releases/download/v{versions['mdbook-admonish']}/mdbook-admonish-v{versions['mdbook-admonish']}-{t}.{archive}",
        'mdbook-linkcheck': f"https://github.com/Michael-F-Bryan/mdbook-linkcheck/releases/download/v{versions['mdbook-linkcheck']}/mdbook-linkcheck.{t}.zip",
    }


def extract(name, data, url):
    wanted = name + EXE
    if url.endswith('.zip'):
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            member = next(m for m in archive.namelist() if Path(m).name == wanted)
            (TOOLS / wanted).write_bytes(archive.read(member))
    else:
        with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as archive:
            member = next(m for m in archive.getmembers() if Path(m.name).name == wanted)
            (TOOLS / wanted).write_bytes(archive.extractfile(member).read())
    if not WINDOWS:
        os.chmod(TOOLS / wanted, 0o755)


def installed_version(name):
    exe = TOOLS / (name + EXE)
    if not exe.is_file():
        return None
    try:
        out = subprocess.run([str(exe), '--version'], capture_output=True, text=True, timeout=30).stdout
    except (OSError, subprocess.SubprocessError):
        return None
    match = re.search(r'\d+\.\d+\.\d+', out)
    if match:
        return match.group(0)
    stamp = TOOLS / (name + '.version')  # tools that print no version number
    return stamp.read_text(encoding='utf-8').strip() if stamp.is_file() else None


def install(versions, force=False):
    TOOLS.mkdir(exist_ok=True)
    for name, url in urls(versions).items():
        if not force and installed_version(name) == versions[name]:
            print(f'{name} {versions[name]} already installed')
            continue
        print(f'Downloading {url}')
        with urllib.request.urlopen(url, timeout=120) as response:
            extract(name, response.read(), url)
        print(f'Installed {name} {installed_version(name)}')
    name = 'mdbook-emojicodes'
    if not force and installed_version(name) == versions[name]:
        print(f'{name} {versions[name]} already installed')
    elif shutil.which('cargo'):
        subprocess.run(['cargo', 'install', '--locked', '--root', str(TOOLS / 'cargo'), f'{name}@{versions[name]}'], check=True)
        shutil.copy2(TOOLS / 'cargo' / 'bin' / (name + EXE), TOOLS / (name + EXE))
        (TOOLS / (name + '.version')).write_text(versions[name] + '\n', encoding='utf-8')
        print(f'Installed {name} {installed_version(name)}')
    else:
        print(f'WARNING: cargo not found; {name} was not installed (install Rust from https://rustup.rs/ or run with --skip-cargo). '
              'mdbook still builds without it, but :emoji: codes stay as text.')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--force', action='store_true', help='reinstall even when versions match')
    parser.add_argument('--run', nargs=argparse.REMAINDER, help='after installing, run mdbook with these arguments (e.g. --run serve)')
    args = parser.parse_args()
    versions = json.loads((ROOT / 'tools.json').read_text(encoding='utf-8'))
    install({k: v for k, v in versions.items() if not k.startswith('_')}, args.force)
    print(f'Tools are in {TOOLS}. Add it to PATH or use --run.')
    if args.run:
        env = dict(os.environ, PATH=str(TOOLS) + os.pathsep + os.environ.get('PATH', ''))
        sys.exit(subprocess.run([str(TOOLS / ('mdbook' + EXE)), *args.run], cwd=ROOT, env=env).returncode)


if __name__ == '__main__':
    main()
