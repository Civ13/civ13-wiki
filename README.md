# Civ13 Wiki

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/civ13/civ13-wiki.svg?style=flat)
![GitHub repo size](https://img.shields.io/github/repo-size/civ13/civ13-wiki.svg?style=flat)

Access it [here](https://civ13.github.io/civ13-wiki)

A **modular and fully featured wiki** powered by [mdBook](https://rust-lang.github.io/mdBook/), [GitHub Pages](https://pages.github.com/) and pull-requests!

## Features 

* **No databases!** Only static files—lightweight and fast to deploy
* **Markdown-based** content with full Git history and version control
* **Offline capable**—download the entire wiki and read it locally
* **Custom theming** with Rust-based mdBook preprocessing
* **DMI Sprite support** for game entity visualization
* **Preprocessors**—admonitions and emoji codes
* **Simple Git workflow**—edit files directly or via GitHub web editor

## Quick Start

### Prerequisites

* Python 3 (standard library only)
* [Git LFS](https://git-lfs.com/) if you need the full-resolution map renders or videos locally (see below)
* [Rust & Cargo](https://rustup.rs/), only for building the `mdbook-emojicodes` preprocessor; everything else is a prebuilt download

### Building the Wiki

Install the pinned toolchain from `tools.json` into the gitignored `tools/` folder:
```bash
python3 scripts/setup_tools.py        # Windows: py -3 scripts/setup_tools.py
```

Then either add `tools/` to your PATH or let the script run mdBook for you:
```bash
python3 scripts/setup_tools.py --run serve
```

Build the static site:
```bash
mdbook build
python3 scripts/previews.py
```

For the complete publishable build, use `python3 scripts/build.py` instead.
It runs mdBook, generates chapter-specific canonical, Open Graph, Twitter and
inline Discord component metadata in the fetched HTML head, writes the Git SHA
to `book/html/revision.json`, and validates every chapter. CI installs the same
pinned versions from `tools.json` (`scripts/check_tools.py` fails the build if
the workflow and `tools.json` disagree). Python 3 uses only the standard library. On Windows, use a verified
full Python interpreter path if the Store alias or `py` launcher is unavailable.

Run `python3 scripts/test_previews.py` for serialization and invalid-payload
regressions, and `python3 scripts/check_output.py` to recheck emitted output.
The reusable `scripts/check_preview.py` validates inline website payloads;
it does not prove Discord client rendering or remote asset availability.
Previews use each chapter's rendered title and first nonempty paragraph (or a
chapter-specific fallback), with the existing public Civ13 banner. Utility
pages do not receive chapter previews. The canonical deployment remains
`https://civ13.github.io/civ13-wiki/`; there is no wiki custom domain.
`mdbook serve` alone is useful for content work, but does not run preview
generation: use the complete build and serve `book/html` to inspect previews.

The compiled wiki will be in `book/html/`.

### Large assets (Git LFS)

Full-resolution map layer renders (`src/images/maps/**/*__full.png`) and videos
(`src/video/`) are stored in Git LFS and are **not** served from GitHub Pages.
Pages link to copies on the rolling [`assets` release](https://github.com/civ13/civ13-wiki/releases/tag/assets),
which `.github/workflows/assets.yml` refreshes whenever an LFS file changes on
`master` (or on manual dispatch). A plain clone only fetches small pointer
files, so clones and CI stay fast; run `git lfs pull` when you need the real
files. To add a new large asset: put it under one of those paths, link it as
`https://github.com/civ13/civ13-wiki/releases/download/assets/<file name>`
(file names must be unique), and run `python3 scripts/check_assets.py`.

### Local Development

Serve the wiki locally with live reloading:
```bash
mdbook serve
```

Open your browser to `http://localhost:3000` and changes will auto-refresh.

### Project Structure

```
src/              # Markdown source files
├── SUMMARY.md    # Navigation structure (single source; scripts/nav.py renders the overview pages from it)
├── index.md      # Home page
├── guides/       # User guides
├── gamemodes/    # Game mode documentation
├── maps/         # Map information
├── rules/        # Game rules
└── images/       # Wiki images and sprites
theme/            # mdBook theme customization (stock templates are not vendored)
├── head.hbs      # HTML head injection (preview marker, DMI sprite component)
└── compiled/     # Site CSS (ss14.css)
scripts/          # Build and check scripts, plus nav-additions.js (page TOC, subpage footer)
book.toml         # mdBook configuration
```

## Editing the Wiki

1. **Fork & clone** the repository
2. **Create a branch** for your changes
3. **Edit markdown files** in `src/`
4. **Test locally** with `mdbook serve`
5. **Commit & push**, then **open a pull request**

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## Configuration

Edit `book.toml` to modify:
* **Theme**—Default and dark theme settings
* **Preprocessors**—Admonitions, emoji codes
* **Additional CSS/JS**—Custom styling and functionality
* **Features**—Syntax highlighting, folding sidebar, etc.

### Preprocessors

The wiki uses several mdBook preprocessors:

* **admonish**—Note, warning, and info boxes
* **emojicodes**—Emoji shorthand support
* **linkcheck**—Internal link validation (warnings only; `scripts/check_player_guides.py` enforces local links and anchors)

## Troubleshooting

### DMI Sprites not rendering?
The wiki must be served via HTTP (not `file://`). Use `mdbook serve` for local testing or host via GitHub Pages.

### Build errors?
Reinstall the pinned toolchain:
```bash
python3 scripts/setup_tools.py --force
```

Clear the build cache and rebuild:
```bash
rm -rf book/
mdbook build
```

## Attribution

Icons made by [Freepik](https://www.flaticon.com/authors/freepik) and [ultimatearm](https://www.flaticon.com/authors/ultimatearm) from [www.flaticon.com](https://www.flaticon.com/)

## License

See [LICENSE](LICENSE) for details.
