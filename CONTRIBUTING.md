If you want to send a pull request to our project and the **GitHub web editor** is not enough, you can develop locally:

### Quick Start

1. Fork or clone this repository.

2. Clone it to your computer and navigate to the `civ13-wiki/` folder.

3. Install the pinned mdBook toolchain (one time) and serve the wiki:
   ```bash
   python3 scripts/setup_tools.py --run serve   # Windows: py -3 scripts/setup_tools.py --run serve
   ```
   The wiki will open at `http://localhost:3000` with live reloading. The tools
   land in the gitignored `tools/` folder; add it to your PATH to call `mdbook`
   directly.

4. Make your changes in the `src/` folder and they'll automatically rebuild in your browser.

5. Push changes to your fork and create a Pull Request for us to review.

### Local Building

- **Build only:** `python3 scripts/setup_tools.py --run build` (outputs to `book/html/`)
- **Live development:** `python3 scripts/setup_tools.py --run serve` (runs local server with auto-reload)
- **Full CI build and checks:** `python3 scripts/check_tools.py && python3 scripts/nav.py && python3 scripts/check_assets.py && python3 scripts/test_previews.py && python3 scripts/build.py && python3 scripts/check_player_guides.py`
- **Game-source checks:** `python3 scripts/check_decay_times.py --civ13 <path to a Civ13 checkout>` reports Food Decay Times rows that no longer match the source (CI runs it against Civ13 master and prints the report in the job summary).
- **Large files:** full-resolution map renders and videos are in Git LFS and served from the `assets` release; see the README.

For more detailed information, check [Contributing to the Wiki](src/Contributing_to_the_Wiki.md) in the wiki itself.
## Player documentation policy

New and updated wiki entries must describe features that are **currently available to players** on the relevant public Civ13 server. Successful CI and local demonstrations alone do not establish availability; see [AGENTS.md](AGENTS.md) for the evidence maintainers accept, such as a merged Civ13 PR whose feature is active in ordinary play. Confirm the feature is deployed, enabled and reachable through normal player gameplay; check any map, mode or research restrictions. Record that confirmation in the PR, not as a source/version banner in the guide. Keep upcoming, disabled, admin-only and unverified features out of published player guides.

Do not publish **secrets**. This includes deliberately hidden discoveries, secret recipes or interactions, concealed locations or loot, puzzle solutions, unrevealed event content and exploit instructions. Finding something in public game source does not make it appropriate for the wiki. Ordinary intended player guidance, such as publicly available crafting recipes and controls, is welcome; do not classify all gameplay information as secret.

Never include credentials, private server configuration, personal information, private communications or confidential reference material. The same rules apply to screenshots, sprite previews, diagrams, captions, metadata and generated pages. Avoid exposing protected details even as examples of what was omitted.

Before submitting an entry:

- Confirm actual player availability and describe relevant gameplay restrictions.
- Check the wording and media for hidden gameplay details or private information.
- Document the current behavior plainly; omit future plans and unnecessary availability disclaimers.
- If secrecy or availability cannot be established, hold the affected detail for maintainer clarification and continue with confirmed public information.

AI editors must also read [AGENTS.md](AGENTS.md). This policy does not authorize deployment or disclosure of confidential material.
