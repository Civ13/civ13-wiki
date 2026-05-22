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
* **Multiple preprocessors**—admonitions, emoji codes, template expansion, and more
* **Simple Git workflow**—edit files directly or via GitHub web editor

## Quick Start

### Prerequisites

* [Rust & Cargo](https://rustup.rs/) (for mdBook)
* [Node.js](https://nodejs.org/) (optional, for preprocessor scripts)

### Building the Wiki

Install mdBook and dependencies:
```bash
cargo install mdbook
```

Build the static site:
```bash
mdbook build
```

The compiled wiki will be in `book/html/`.

### Local Development

Serve the wiki locally with live reloading:
```bash
mdbook serve
```

Open your browser to `http://localhost:3000` and changes will auto-refresh.

### Project Structure

```
src/              # Markdown source files
├── SUMMARY.md    # Navigation structure
├── index.md      # Home page
├── guides/       # User guides
├── gamemodes/    # Game mode documentation
├── maps/         # Map information
├── rules/        # Game rules
└── images/       # Wiki images and sprites
theme/            # mdBook theme customization
├── head.hbs      # HTML head injection (DMI sprites, scripts)
├── index.hbs     # Main template
└── compiled/     # Generated CSS
scripts/          # Additional JavaScript
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
* **Preprocessors**—Admonitions, emoji codes, template expansion
* **Additional CSS/JS**—Custom styling and functionality
* **Features**—Syntax highlighting, MathJax support, etc.

### Preprocessors

The wiki uses several mdBook preprocessors:

* **admonish**—Note, warning, and info boxes
* **emojicodes**—Emoji shorthand support
* **template**—Template expansion in markdown
* **embedify**—Content embedding

## Troubleshooting

### DMI Sprites not rendering?
The wiki must be served via HTTP (not `file://`). Use `mdbook serve` for local testing or host via GitHub Pages.

### Build errors?
Ensure you have the latest mdBook version:
```bash
cargo install mdbook --upgrade
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
