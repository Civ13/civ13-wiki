# Wiki agent policy

Before adding or updating player-facing entries, follow the [player documentation policy](CONTRIBUTING.md#player-documentation-policy). It applies to text, recipes, tables, diagrams, images, captions and generated content.

Document only features currently available to players on the relevant public game server. Verify availability separately from source review: a merge, passing CI, local test or published API reference does not prove a feature is deployed or enabled. Hold unverified or upcoming entries outside the published wiki until availability is confirmed.

Do not reveal gameplay secrets or private information. Public source code is evidence for accuracy, not permission to publish hidden discoveries. If a detail may be deliberately secret, omit that detail and continue with ordinary public player guidance; ask a maintainer only when resolving it is necessary.

Accepted availability evidence, so agents do not stall on a rule they cannot verify from a cloud session:

- A gameplay feature merged to Civ13/Civ13 `master` counts as available when it is reachable in ordinary play: its recipe or verb is active (not commented out, not admin-only, not behind a default-off flag or disabled research node). Cite the merged PR in this wiki PR.
- A map counts as available when it has an active entry in the vote lists in `code/processes/mapswap.dm`. Commented-out maps are out of rotation.
- If neither applies, leave that detail out and publish the rest of the page. Ask in the PR only when the missing detail blocks the page.

After editing a guide that the in-game Help pins (`WIKI_REVIEWED_GUIDES` in Civ13's `scripts/player_help_bridge.py`), note in the PR that Civ13 needs a re-pin: `python3 scripts/agent_preflight.py wiki-pins --wiki-root <this checkout> --write` in Civ13.

Keep availability evidence and editorial decisions in the PR or private task record. Published guides should describe the current game directly, without source/version banners or unreleased-feature notices. Preserve unrelated work and follow the repository's existing build and PR workflow.
