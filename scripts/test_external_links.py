"""Exercise the external sweep's real Lychee arguments using local HTTP fixtures.

Requires lychee 0.24.2 on PATH (the version used by links.yml). No public
network requests or GitHub credentials are used by these regressions.
"""
import os
from pathlib import Path
import re
import shlex
import subprocess
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = Path(__file__).resolve().parents[1]


def sweep_args():
    workflow = (ROOT / '.github/workflows/links.yml').read_text(encoding='utf-8')
    args, = re.findall(r'^\s+args: (.+)$', workflow, re.M)
    return shlex.split(args)


def check_summary(text):
    # The entire file is excluded, so even a bare URL or HTML href added in
    # future must fail loudly rather than disappear from external checking.
    if re.search(r'https?\s*:|//[^\s/]', text, re.I):
        raise ValueError('SUMMARY.md contains an external URL; preserve it in the external sweep before excluding this file')


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200 if self.path == '/ok' else 404)
        self.end_headers()
        self.wfile.write(b'fixture')

    do_HEAD = do_GET

    def log_message(self, *args):
        pass


class LinkSweepTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f'http://127.0.0.1:{cls.server.server_port}'

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def run_sweep(self, extra=None, include_summary=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'src').mkdir()
            (root / 'src/SUMMARY.md').write_text('- [Group]()\n    - [Guide](guide.md)\n', encoding='utf-8')
            (root / 'src/guide.md').write_text(f'[Working]({self.url}/ok)\n', encoding='utf-8')
            for name in ('README.md', 'CONTRIBUTING.md'):
                (root / name).write_text('# Fixture\n', encoding='utf-8')
            for name, text in (extra or {}).items():
                (root / name).write_text(text, encoding='utf-8')
            args = sweep_args()
            if include_summary:
                index = args.index('src/SUMMARY.md')
                del args[index - 1:index + 1]
            return subprocess.run(
                ['lychee', *args, '--format', 'markdown'], cwd=root,
                env={**os.environ, 'NO_PROXY': '127.0.0.1', 'no_proxy': '127.0.0.1'},
                capture_output=True, text=True, timeout=30)

    def test_intentional_groups_are_not_errors(self):
        result = self.run_sweep()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn('Empty URL', result.stdout + result.stderr)

    def test_regression_reproduces_without_summary_exclusion(self):
        result = self.run_sweep(include_summary=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Empty URL', result.stdout + result.stderr)

    def test_real_broken_external_links_are_reported(self):
        for filename in ('src/guide.md', 'README.md', 'CONTRIBUTING.md'):
            with self.subTest(filename=filename):
                result = self.run_sweep({filename: f'[Broken]({self.url}/missing)\n'})
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('/missing', result.stdout + result.stderr)
                self.assertIn('404', result.stdout + result.stderr)

    def test_empty_links_outside_summary_still_fail(self):
        result = self.run_sweep({'src/guide.md': '[Accidental empty link]()\n'})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Empty URL', result.stdout + result.stderr)

    def test_current_summary_has_no_external_links_to_hide(self):
        check_summary((ROOT / 'src/SUMMARY.md').read_text(encoding='utf-8'))

    def test_future_summary_external_links_fail_guard(self):
        for text in ('[Link](https://example.com)', '<https://example.com>',
                     '<a href="http://example.com">Link</a>', '[Link](//example.com)'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                check_summary(text)


if __name__ == '__main__':
    unittest.main()
