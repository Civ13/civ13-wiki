# Held leather-tanning wiki update

This is a reviewable proposal, not published player documentation. The tanning
implementation is in Civ13 commit
`02449628a1359c709f3fd298f4d3468902c6b161` (PR 3279). It has not been established
as available through normal play on Gaia. The existing live game remains on
`1650445ede7924070698de31d34e8e8afb913d29`.

[AGENTS.md](../../AGENTS.md) requires: "Document only features currently available
to players on the relevant public game server" and "Hold unverified or upcoming
entries outside the published wiki until availability is confirmed." The
[player documentation policy](../../CONTRIBUTING.md#player-documentation-policy)
also requires deployment, enablement, and normal player reachability evidence.
This proposal therefore leaves `src/` unchanged and stays outside mdBook's input.
No game deployment or wiki publication is authorized by these files.

## Proposed source edits

`wiki-source.patch` uses zero-context hunks with full source blob hashes; apply
with `--unidiff-zero` only after checking its base and the source. It applies to wiki base
`ea3d710ff27ae1a0960c1a0fe50ab0acbaf3e2de` and changes three existing manual pages:

- `src/guides/Guide_to_Ranching.md`: replace direct leather drops with raw hides,
  retain species pelts and existing meat/byproducts, document adult male/female
  turkey skin and the no-hide chick policy, and link the complete process.
- `src/guides/Guide_to_Crafting.md`: replace obsolete pelt/leather/rack
  instructions, remove the extra-leather claim, and add tanning links in the
  existing quick links and wood resource section.
- `src/Miscellaneous_Crafting.md`: add one complete leather-tanning section with
  prerequisites, one-piece processing, 5-water washing, 300-tick rack drying,
  5-tannin finishing, bark extraction, cancellation, restart behavior, and fur
  preservation. Link back to Ranching and the existing rack section.

The proposal preserves existing finished-leather recipes and their costs.
It does not edit `src/Full_Crafting_List.md`: that is a dated recipe export,
not the owner of acquisition prose. Civ13's admin-only
`print_crafting_recipes()` in `code/game/objects/items/stacks/civ_recipes.dm`
exports those recipe tables; no native export was invoked.
The proposal does not regenerate the Crafting Atlas,
touch `book/`, change navigation/theme settings, or import additional assets.

## Local checks

- `git apply --unidiff-zero --check` passes against the stated wiki base.
- The patch was applied only in a private preview worktree. The held branch's
  `src/`, `book.toml`, themes, and scripts remain unchanged.
- Proposal patch SHA-256:
  `0ad502c90863845f7d870d42de5ea5ed444b1d7244ff0ea812ba8c3f0955feee`.
- Existing preview tests: 3 passed.
- Existing build/output validation: 111 chapter previews generated and validated.
- Existing player-guide checks: 112 rendered pages and 395 local Markdown links,
  including anchors, checked successfully.
- An additional check resolved 13 rendered tanning/rack/harvesting links,
  including the raw HTML links added to Crafting table cells, to existing pages
  and destination anchors.
- The bundled local mdBook is 0.4.48; CI pins 0.4.36. The build succeeded with a
  bundled admonish version warning and the linkcheck backend's existing warning
  that it does not resolve fragments. The rendered link checks above cover the
  proposed anchors. CI's exact toolchain was not run.

These checks validate the proposed documentation, not game behavior or public
availability. The preview is wiki base plus the recorded patch, not an unchanged
checkout of the base; its generated revision manifest alone is not a content pin.

## Promotion after availability is confirmed

1. The parent/maintainer reviews the game implementation and its acceptance
   evidence. Native compilation, fixtures, saves, and client interaction have
   not been verified by this wiki work.
2. Confirm separately that the relevant public server has the implementation
   deployed, enabled, and reachable, including its mode/research prerequisites.
   Record that evidence in the wiki PR or private task record. Source commits,
   merges, builds, and atlas publication alone do not satisfy this requirement.
3. Rebase a promotion branch onto the current wiki master. Recheck the cited
   game behavior against the deployed revision and refresh the patch if either
   source has changed.
4. From the wiki checkout, inspect and apply the proposal:

   ```powershell
   git apply --unidiff-zero --check drafts/leather-tanning/wiki-source.patch
   git apply --unidiff-zero drafts/leather-tanning/wiki-source.patch
   ```

5. Use the repository's documented pinned mdBook toolchain and run its existing
   `scripts/test_previews.py`, `scripts/build.py`, and
   `scripts/check_player_guides.py`. Inspect the rendered three pages, links,
   anchors, and quantities. These checks build documentation, not BYOND.
6. Keep the player prose direct. Do not add source/version banners or
   unreleased-feature notices to published pages. Remove the held proposal from
   the promotion change once its source edits and review evidence are retained.
7. Open a reviewed wiki PR. Merging master triggers GitHub Pages publication;
   do not merge or trigger deployment as part of the held proposal.

The existing wiki workflow builds PRs without deployment. Master pushes can
deploy. This local branch is intentionally not pushed pending parent review.
