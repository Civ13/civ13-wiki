"""Build the deployable wiki using the installed pinned mdBook tools."""
import json
import subprocess
from pathlib import Path
from previews import generate
from check_output import check

if __name__ == '__main__':
    subprocess.run(['mdbook', 'build'], check=True)
    root = Path('book/html')
    generate(root)
    sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
    (root / 'revision.json').write_text(json.dumps({'sha': sha}) + '\n', encoding='utf-8')
    check(root)
