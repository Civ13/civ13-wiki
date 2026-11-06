"""Render built pages in Chromium and save a browsable screenshot report.

Serves an already-built site from 127.0.0.1, blocks every other origin, and
captures each selected page at desktop and mobile sizes. The report goes to
render-report/ (index.html plus JPEG screenshots) and a Markdown summary is
appended to $GITHUB_STEP_SUMMARY when it is set.

Page selection:
  --all                     every .html page in the site (minus --skip prefixes)
  --changed BASE --mode M   pages whose sources changed since git revision BASE,
                            M is "mdbook" (src/X.md -> X.html) or "jekyll"
                            (front matter permalink, else X.md -> X.html)
  --default PAGE            always rendered; also the fallback when a change
                            touches shared files (theme, layouts, CSS, config)

The run fails only when a page cannot be served or loaded. Horizontal
overflow, script errors and blocked external requests are reported as notes.
"""
import argparse
import functools
import html
import http.server
import os
import re
import subprocess
import sys
import threading
from pathlib import Path

REPORT = Path('render-report')
MAX_BYTES = 15 * 1024 * 1024
MAX_HEIGHT = 8000  # px; very long pages are cut, the report says so
VIEWPORTS = {
    'desktop': {'viewport': {'width': 1280, 'height': 900}},
    'mobile': {'viewport': {'width': 390, 'height': 844}, 'is_mobile': True, 'has_touch': True},
}


def changed_files(base):
    out = subprocess.check_output(['git', 'diff', '--name-only', '--diff-filter=ACMR', base, 'HEAD'], text=True)
    return [line for line in out.splitlines() if line]


def front_matter_permalink(path):
    try:
        text = Path(path).read_text(encoding='utf-8')
    except (OSError, UnicodeDecodeError):
        return None
    if not text.startswith('---'):
        return None
    end = text.find('\n---', 3)
    match = re.search(r'^permalink:\s*["\']?([^"\'\s]+)', text[:end if end > 0 else 0], re.M)
    return match.group(1) if match else None


def map_source(path, mode):
    """Return the built page for a changed source file, '' for a shared file, None to ignore."""
    if mode == 'mdbook':
        if path.startswith('src/') and path.endswith('.md'):
            if path == 'src/SUMMARY.md':
                return ''
            return path[len('src/'):-len('.md')] + '.html'
        if path.startswith(('theme/', 'book.toml', 'scripts/nav-additions.js')):
            return ''
        return None
    # jekyll
    if path.startswith(('_layouts/', '_includes/', '_sass/', '_data/', 'public/css/', '_config.yml')):
        return ''
    top = path.split('/', 1)[0]
    if top.startswith(('_', '.')) or top in ('tools', 'workers', 'vendor') or path in ('README.md', 'LICENSE.md'):
        return None
    if not path.endswith(('.md', '.markdown', '.html')):
        return None
    permalink = front_matter_permalink(path)
    if permalink:
        page = permalink.lstrip('/')
        return page + 'index.html' if page.endswith('/') or not page else page
    return re.sub(r'\.(md|markdown)$', '.html', path)


def select_pages(args, site):
    notes = []
    pages = []
    if args.all:
        for page in sorted(site.rglob('*.html')):
            relative = page.relative_to(site).as_posix()
            if not relative.startswith(tuple(args.skip)):
                pages.append(relative)
    if args.changed:
        shared = False
        for path in changed_files(args.changed):
            page = map_source(path, args.mode)
            if page == '':
                shared = True
            elif page is not None:
                if (site / page).is_file():
                    pages.append(page)
                else:
                    notes.append(f'{path}: no built page at {page}')
        if shared:
            notes.append('Shared theme or layout files changed, so the default pages are included.')
    pages += args.default
    unique = list(dict.fromkeys(pages))
    if len(unique) > args.limit:
        notes.append(f'{len(unique) - args.limit} more pages were not rendered (limit {args.limit}).')
        unique = unique[:args.limit]
    return unique, notes


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def serve(site):
    handler = functools.partial(QuietHandler, directory=str(site))
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def render(pages, origin):
    from playwright.sync_api import sync_playwright
    REPORT.mkdir(exist_ok=True)
    results = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        for name, options in VIEWPORTS.items():
            context = browser.new_context(service_workers='block', **options)
            blocked = []

            def route(request_route, request):
                if request.url.startswith(origin + '/'):
                    request_route.continue_()
                else:
                    blocked.append(request.url)
                    request_route.abort()

            context.route('**/*', route)
            for page_path in pages:
                blocked.clear()
                errors = []
                page = context.new_page()
                page.on('pageerror', lambda error, errors=errors: errors.append(str(error)))
                result = {'page': page_path, 'viewport': name, 'notes': []}
                try:
                    response = page.goto(f'{origin}/{page_path}', wait_until='load', timeout=30000)
                    status = response.status if response else 0
                    result['ok'] = status == 200
                    if status != 200:
                        result['notes'].append(f'HTTP {status}')
                    page.evaluate("""async () => {
                        for (const image of document.images) image.loading = 'eager';
                        await Promise.all([...document.images].map(i => i.decode().catch(() => {})));
                        await document.fonts.ready;
                    }""")
                    width, height, inner = page.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight, innerWidth]')
                    if width > inner:
                        result['notes'].append(f'scrolls sideways ({width}px wide in a {inner}px window)')
                    shot = REPORT / (re.sub(r'[^A-Za-z0-9._-]+', '_', page_path.removesuffix('.html')) + f'.{name}.jpg')
                    clip_height = min(height, MAX_HEIGHT)
                    if height > MAX_HEIGHT:
                        result['notes'].append(f'cut at {MAX_HEIGHT}px of {height}px')
                    page.screenshot(path=str(shot), type='jpeg', quality=65, animations='disabled',
                                    full_page=True, clip={'x': 0, 'y': 0, 'width': inner, 'height': clip_height})
                    result['shot'] = shot.name
                except Exception as error:  # noqa: BLE001 - reported, then fails the run
                    result['ok'] = False
                    result['notes'].append(f'load failed: {error}'.splitlines()[0])
                if errors:
                    result['notes'].append(f'{len(errors)} script error(s): ' + '; '.join(errors)[:300])
                if blocked:
                    result['notes'].append(f'{len(blocked)} external request(s) blocked')
                results.append(result)
                page.close()
            context.close()
        browser.close()
    return results


def write_report(title, pages, results, notes):
    rows = []
    by_page = {}
    for result in results:
        by_page.setdefault(result['page'], {})[result['viewport']] = result
    for page in pages:
        cells = []
        for name in VIEWPORTS:
            result = by_page.get(page, {}).get(name, {})
            image = (f'<a class="shot" href="{html.escape(result["shot"])}"><img src="{html.escape(result["shot"])}" loading="lazy" alt="{name}"></a>'
                     if result.get('shot') else '<em>no screenshot</em>')
            note = ''.join(f'<li>{html.escape(n)}</li>' for n in result.get('notes', []))
            cells.append(f'<td>{image}<ul>{note}</ul></td>')
        rows.append(f'<tr><th>{html.escape(page)}</th>{"".join(cells)}</tr>')
    run_notes = ''.join(f'<li>{html.escape(n)}</li>' for n in notes)
    (REPORT / 'index.html').write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
body {{ font: 15px/1.4 system-ui, sans-serif; margin: 16px; background: #f6f6f4; color: #1d1d1b; }}
table {{ border-collapse: collapse; width: 100%; }} th, td {{ border: 1px solid #ccc; padding: 8px; vertical-align: top; text-align: left; }}
th {{ width: 14em; word-break: break-all; }} .shot {{ display: block; max-height: 720px; overflow-y: auto; border: 1px solid #999; }}
img {{ display: block; width: 100%; }} td:nth-child(3) .shot {{ max-width: 260px; }} ul {{ margin: 6px 0 0; padding-left: 18px; color: #8a4b00; }}
</style></head><body>
<h1>{html.escape(title)}</h1>
<p>Built from this pull request and served locally. Other origins were blocked, so embeds and remote images may be missing. Desktop is 1280px wide, mobile 390px. Click a screenshot for full size.</p>
<ul>{run_notes}</ul>
<table><thead><tr><th>Page</th><th>Desktop</th><th>Mobile</th></tr></thead><tbody>{"".join(rows)}</tbody></table>
</body></html>
''', encoding='utf-8')


def report_bytes():
    return sum(path.stat().st_size for path in REPORT.rglob('*') if path.is_file())


def write_summary(title, artifact, results, notes, size):
    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    lines = [f'## {title}', '',
             f'Download the **{artifact}** artifact from this run and open index.html. '
             'Pages are built from this PR and served locally with other origins blocked; nothing is deployed.', '',
             '| Page | Desktop | Mobile |', '| --- | --- | --- |']
    by_page = {}
    for result in results:
        by_page.setdefault(result['page'], {})[result['viewport']] = result
    for page, views in by_page.items():
        def cell(result):
            if not result:
                return 'not run'
            mark = 'ok' if result.get('ok') else 'FAILED'
            return mark + (': ' + '; '.join(result['notes']).replace('|', '/') if result.get('notes') else '')
        lines.append(f'| `{page}` | {cell(views.get("desktop"))} | {cell(views.get("mobile"))} |')
    lines += [''] + [f'- {note}' for note in notes] + [f'- Report size: {size / 1048576:.1f} MiB (limit 15 MiB).']
    text = '\n'.join(lines) + '\n'
    if summary:
        with open(summary, 'a', encoding='utf-8') as handle:
            handle.write(text)
    print(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('site', type=Path, help='built site directory')
    parser.add_argument('--title', default='Render previews')
    parser.add_argument('--artifact', default='render-report')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--skip', action='append', default=[])
    parser.add_argument('--changed', metavar='BASE')
    parser.add_argument('--mode', choices=('mdbook', 'jekyll'), default='jekyll')
    parser.add_argument('--default', action='append', default=[])
    parser.add_argument('--limit', type=int, default=20)
    args = parser.parse_args()

    site = args.site.resolve()
    pages, notes = select_pages(args, site)
    if not pages:
        sys.exit('No pages selected')
    server = serve(site)
    try:
        results = render(pages, f'http://127.0.0.1:{server.server_address[1]}')
    finally:
        server.shutdown()
    write_report(args.title, pages, results, notes)
    size = report_bytes()
    write_summary(args.title, args.artifact, results, notes, size)
    if size > MAX_BYTES:
        # Keep the upload small: drop the screenshots and leave only the page list.
        for shot in REPORT.glob('*.jpg'):
            shot.unlink()
        sys.exit(f'Report is {size} bytes, over the 15 MiB upload limit; screenshots were dropped')
    if not all(result.get('ok') for result in results):
        sys.exit('Some pages failed to load; see the table above')


if __name__ == '__main__':
    main()
