# Designing maps for Civ13

This guide is for map contributors. Start with an authored Civ13 map that already
supports your intended game mode, then change one system at a time. A map's terrain,
metadata, areas, landmarks and saved-world behavior must agree before it is ready
for players.

For editor controls and DM syntax, use the official [BYOND Guide](https://www.byond.com/docs/guide/)
and [DM Reference](https://www.byond.com/docs/ref/). The instructions below concern
Civ13's mapping contracts. The source links identify a reviewable implementation;
they do not certify a server deployment or a successful playtest.

## 1. Choose a donor map and define the change

Choose by **gameplay rules**, not appearance. For example, Europe is a Nomads map:
its metadata inherits Nomads behavior and enables research. Mountain has a different
season implementation and uses indoor cave areas. Copying a familiar landscape
while changing its map ID can change jobs, farming, equipment and other map-specific
branches elsewhere in the code.

Write down the donor, game revision, intended mode/factions, research and age rules,
fresh-world or saved-world target, grid dimensions and required travel routes. Keep
the original available in Git. Work in an isolated checkout rather than an operator's
running server directory.

Follow [the map-directory conventions](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/maps/README.txt):
lowercase filenames with underscores, WIP maps in the WIP folder, and additional
authored z-levels the same size as the main level. Use spare space on an existing
level when it meets the design; another level adds a full grid.

## 2. Register the map, not just the filename

For an existing map, inspect these together before changing them:

| Part | Europe example | What it controls |
| --- | --- | --- |
| Authored grid | `maps/nomads/nomads_europe.dmm` | Placed turfs, areas, objects and landmarks |
| Metadata subtype | `/obj/map_metadata/nomads/europe` | Inherited mode rules and map overrides |
| ID constant | `MAP_NOMADS_EUROPE` in `code/__defines/maps.dm` | Identity used by map-specific code |
| DM include | Metadata file included by `civ13.dme` | Makes the subtype part of the compiled project |
| DMM include | Selected map include in `civ13.dme` | Chooses the authored grid for that build |
| Rotation entry | `code/processes/mapswap.dm` | Operator map-selection policy, separately maintained |

The metadata object's `New()` assigns the global `map`. Preserve the intended
metadata placement when editing a donor; a stray second metadata object can replace
that global and run another initializer. A new ID also needs a search for existing
ID-specific branches. Adding a `.dmm` alone does not add a mode or enroll a map in
rotation. Review selection-policy changes separately with the maintainer.

[Europe metadata](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/game/objects/map_metadata/nomads/nomads_europe.dm),
[metadata initialization](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/game/objects/map_metadata/_map_metadata.dm#L283-L290),
[ID definitions](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/__defines/maps.dm),
[project includes](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/civ13.dme)
and [rotation source](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/processes/mapswap.dm#L320-L335)
are the starting points.

When editing DMM text, keep tile-key lengths and row widths consistent and check for
undefined keys and overlapping coordinate blocks. Use numeric literals such as
`locked = 1` in authored object overrides rather than assuming DM macros are valid
there. Prefer the editor for substantial layout changes and review the resulting
diff for accidental area or object replacements.

## 3. Give every turf the right area and climate

A turf belongs to **one native `/area`**. Country, biome and room are not three
independent area layers. Choose an existing area subtype whose inherited fields
match the intended behavior; a display name alone does not establish that behavior.

For example, `/area/caribbean/forest` has temperate climate and a grass base turf,
and inherits outdoor location. `/area/caribbean/roofed` is indoors, with climate
variants. `/area/caribbean/void/caves/level1` and the other cave levels are indoors.
Mountain's authored cave levels and its Wet/Dry calendar do **not** implement
altitude. Naming an area "mountain" or painting white turf does not supply an
elevation model.

Trace both the type's own assignments and its parents in
[area defaults](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/game/area/areas.dm)
and [Civ13 area types](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/game/area/caribbean.dm).
Then inspect the donor's metadata: area `climate`, map season/calendar, weather
policy and research age are different inputs. See
[Mountain metadata](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/game/objects/map_metadata/nomads/nomads_mountain.dm)
and the contributor notes on [seasons](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/docs/season-flow.md)
and [weather policy](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/docs/weather-policy.md).

Check gameplay consumers of those fields. Outdoor crop behavior has an explicit
map-ID gate for Continental, Pangea, New World, Mediterranean, Europe and Gaia;
matching the grass sprite on another map does not grant the same farming rules.
Use the [outdoor crop bootstrap trace](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/docs/outdoor-crop-bootstrap.md)
when designing that resource chain.

## 4. Design z-level connections explicitly

Numbered z-levels can represent different places. Do not assume `z + 1` is the sky
above a room or that two nearby levels are traversable.

The generic `GetAbove`/`GetBelow` helpers use an adjacent-level bitmask. The
`map_data.New()` code that would fill it from `height` is commented out in
[the helper implementation](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/modules/multiz/helpers.dm).
Placing `map_data` with a height therefore does not establish those connections.

Ladder subtypes have different target rules. Generic ladders use the vertical
helpers; the `ww2` family assigns matching IDs using `area_id` and enumeration order
at round start. Copying one end or reusing a default `area_id` across unrelated
routes is insufficient evidence of a correct pairing. Trace the exact donor
subtype in [multiz structures](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/modules/multiz/structures.dm)
and record both endpoints, direction and expected return route. Keep destinations
clear and inspect special movement restrictions before calling a connection ready.

Building roof floors use a separate coordinate/pair-ID contract in
[building levels](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/game/objects/building_levels.dm).
Runtime level growth also passes a world-grid budget. A small roof does not mean a
small new level: allocation covers a full plane. With an unmeasured production
profile, new grid growth is refused; shelter can still exist without a newly
allocated upper floor. Follow the [z-budget contract](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/docs/new-z-budget.md),
and distinguish an authored extra plane from runtime roof allocation.

## 5. Treat roofing as behavior

An indoor area, a floor, a roof object and a walkable upper floor are separate
things. In the ordinary `switch_area` roof path, construction records the former
area type and switches the turf to a supported climate-specific roofed area;
removal restores the recorded type. A decorative roof image cannot substitute for
that lifecycle. Inspect [roof construction and removal](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/game/objects/roof_stuff.dm#L174-L254)
before placing custom roof variants or altering indoor boundaries.

For an authored building, check the intended area, climate, entrances, roof objects
and any upper-floor transfer together. Later visual acceptance must cover the
interior, exterior and roof removal: correct area fields alone do not prove correct
lighting, overlays or movement.

## 6. Trace every arrival route

Landmark names are case-sensitive lookup keys. The
[landmark initializer](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/game/objects/effects/landmarks/normal.dm#L13-L41)
treats `start`, `JoinLate`, `Paradrop` and ordinary named landmarks differently;
many landmarks populate runtime lists and then delete themselves.

For a Nomads civilian route, follow `spawn_location = "JoinLateCiv"` in the
[job definition](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/modules/1713/jobs/nomads.dm#L1170-L1195),
check map/job overrides, and then inspect
[job relocation](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/game/jobs/job_controller.dm#L207-L310).
Faction variants use other keys; copying only the civilian marker does not cover
every job.

This illustrates the DMM structure using existing types; it is one tile definition,
not a complete or playtested map:

```text
"aa" = (/obj/effect/landmark{name = "JoinLateCiv"},/turf/floor/grass,/area/caribbean/forest)
```

Provide enough clear arrival tiles. Relocation rejects candidates containing mobs
or structures, and a missing key can send a job through a hardcoded fallback rather
than the intended settlement. Check the lobby, each playable faction/job, relevant
latejoin/paradrop or squad routes, and supplies separately. An area named "Supply
Arrival" does not create a supply landmark or delivery system; trace the applicable
[supply code](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/modules/1713/supplysystem.dm).

## 7. Plan saved-world compatibility before changing layout

An authored `.dmm` is the starting layout; a persistent save is runtime state.
Loading a generation restores saved turf types over the grid. A DMM edit therefore
does not automatically update an already saved settlement. Preflight checks map
identity, generation and dimensions; changing the ID or grid can invalidate an
existing generation. See [save validation and restoration](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/code/modules/persistence/loading.dm#L367-L500).

Native area references use an anchor and type. Supported saved roof-area topology
has a specific reconstruction path; this is not a general facility for inventing
new area identities during load. Arbitrary area subdivision, changed anchors and
new cross-level references need their own migration review. The
[zone persistence audit](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/docs/zone-persistence-audit.md)
records the supported cases and remaining limits.

For a persistence-targeted change, retain the original save generation and source
revision. Specify whether the proposal starts a fresh world or requires a migration;
test any migration only on an authorized disposable copy. Verify restored players,
fresh joins after restore, spawn registries, roof areas and travel routes separately.
A fresh-start landmark check does not establish their durability. Never delete a
save or change a live configuration to make a mapping test pass. Operator procedures
belong in the [save/restart documentation](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/docs/world-save-restart.md).

## 8. Check the gameplay chain, not just resource counts

Sketch a route from each intended starting position to water, food, shelter and the
tools needed for progression. For an outdoor farming scenario, that includes usable
water, accessible wood/stone, tool acquisition, the required workbench/research,
ploughable soil and compatible crops. Check both faction access and the intended
era. An item behind an impassable boundary or a recipe locked behind unavailable
research cannot bootstrap the settlement.

Use [Crafting](../guides/Guide_to_Crafting.md), [Research](../guides/Guide_to_Research.md) and
[Farming](../guides/Guide_to_Farming.md) for player-facing context, then verify the donor's
actual source gates. Avoid balancing from a count of unused DMM tile definitions:
count placed tiles and review routes. The existing
[read-only outdoor inventory](https://github.com/Civ13/Civ13/blob/fa363b8a01ed7d936c10a6303ce1be4c26d82ab0/scripts/check-outdoor-bootstrap.py)
checks six named outdoor maps and supported DMM formatting. Its static counts do
not prove accessibility, tool/research progression, season suitability or save/load
behavior. Keep protected resource and spawn coordinates out of public reports.

## 9. Submit evidence in stages

For documentation or layout review, start offline: inspect the diff, verify type
paths and inheritance, registration, placed landmark keys, grid shape and resource
dependencies. Run the existing documentation/link checks for documentation changes.
The code repository has a [short contributor checklist](https://github.com/Civ13/Civ13/blob/master/docs/mapping.md).

Native compilation and gameplay testing require their own authorized, isolated
environment. `launch_map` and `select_map` scripts edit the project selection,
compile and launch; they are not read-only validators. Production map-swap helpers
also perform operational work. Do not run them as an offline check.

When native testing is authorized, record the exact source/map revision and mode,
then cover fresh joins, each travel direction, roof construction/removal, weather
and lighting, progression, and persistence restore where applicable. Include visual
evidence and failure cases. Until then, label the result **source reviewed / native
behavior unverified** in the PR; do not report a map as gameplay-ready.

## Troubleshooting

| Symptom | First checks |
| --- | --- |
| Wrong mode, age or research | Metadata subtype/placement, inherited defaults, ID-specific overrides and selected DMM include |
| Spawn outside the intended settlement | Exact job/override key, placed landmark, blocked candidates and fresh versus restored startup |
| A supply area does nothing | The delivery route's expected landmark/treasury key and mode setup |
| Ladder has no destination or reaches the wrong place | Exact subtype, helper connections or pairing IDs/order, both endpoints and movement restrictions |
| A roof shelters but has no usable upper floor | Roof's area lifecycle, pair contract, existing-plane eligibility and grid-budget refusal |
| Crops differ from the donor | Native area climate, map-ID gate, water/soil, research, season and indoor/outdoor status |
| Edited terrain disappears after restart | Saved generation restores its terrain; a source edit is not a migration |
| A save refuses to load | Preserve it; review map ID, dimensions, generation completeness and supported area references |

## Design work outside the current workflow

These are contributor design boundaries, not instructions for enabled map features:

| Proposal | Prerequisite before adding authoring instructions |
| --- | --- |
| Optional elevation (planned default `0`) | Merged field/API and verified consumers; no current altitude setting is prescribed here |
| Separate logical geography and durable zone/spawn registry | Published, reviewed implementation and migration contract; native `/area` remains one membership per turf |
| Generated seasonal ground snow | Snow proposal [#3300](https://github.com/Civ13/Civ13/pull/3300) accepted and available; its proposed dirt/grass accumulation and shovel restoration are distinct from authored snow |
| Saved-world-to-map export | Implemented and reviewed exporter; planned defaults exclude player/runtime/private state and preserve original saves. No automatic save-to-compiled-map workflow is available here |
| Sharded travel | A supported server travel protocol; it is not established by adjacent z-levels or an area name |

Keep proposal examples out of a playable map's required dependencies until their
version and availability prerequisites have been established.
