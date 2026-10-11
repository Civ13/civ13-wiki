# Power & Batteries

Use an [engine and cable network](Guide_to_Crafting.md#engines) to run electrical machinery. Batteries provide limited cable power; they are not mechanical engines and cannot propel modular vehicles. For vehicle construction, use the [Crafting guide](Guide_to_Crafting.md) and [Tanks guide](Guide_to_Tanks.md).

## Choose a battery

These recipes are in the global crafting catalog. Map catalogs, era and character skill requirements still apply; do not assume a Carib or other specialized map offers them. Tech-tree cable recipes require **Electricity**, so an early battery recipe alone does not create a usable electrical network.

| Device | Crafting and commissioning | Capacity / output limit |
| --- | --- | --- |
| Baghdad-style jar cell | Craft an assembly from 2 copper. Fit a fired clay vase, then 1 iron sheet and 10 units of grape juice. | 600 PU s / 1 PU |
| Iron-copper voltaic-style pile | Craft from 5 copper, then add 5 iron sheets and 50 units of grape juice. | 3,000 PU s / 5 PU |
| Lead-acid accumulator | Craft from 5 lead. Add 20 units of sulfuric acid to commission it; it remains empty until electrically charged. | 12,000 PU s / 10 PU; charge limit 10 PU |

PU is the game's abstract power unit; PU s is stored energy. The jar is a speculative interpretation and the iron-copper pile is a gameplay substitute, not a claim about historical battery construction.

## Connect and operate

1. Assemble and commission the battery. Use a wrench to secure it.
2. Stand beside it and use a cable coil on it. Continue the cable network in the matching direction; battery attachment joins neighboring straight cables of the same color and orientation. A cable merely lying nearby does not establish a connection.
3. Click the battery to select its mode. Primary cells cycle **off → discharge → off**. The accumulator cycles **off → charge → discharge → off**.
4. Examine it to read stored energy, output limit and mode. Switch it off when finished: discharge consumes energy each second even when no machine uses it.

The jar and pile cannot recharge electrically. When empty, switch off, replace the iron electrode and grape juice using the amounts above. The accumulator charges from spare output of running engines on its cable network, after machine loads; another battery cannot charge it.

Cut its cable before unanchoring. Moving or disconnecting a battery turns it off. After a world save is loaded, stored chemical state is retained, but mode, output and wiring must be rebuilt by players. This describes battery save behavior where server world saves are enabled; it does not promise that every round or server retains your settlement.

## Troubleshooting

- **No power:** check commissioning, anchoring, cable attachment, mode and remaining energy. For an accumulator, adding acid does not supply charge.
- **Machine exceeds output:** one accumulator supplies at most 10 PU. The laboratory centrifuge requires 30 PU, so one battery cannot run it. Provide sufficient connected generation; stored capacity alone does not raise output.
- **Cannot craft cables:** check the map catalog, era, skill and Electricity research. Battery availability does not bypass those gates.
- **Engine will not run a vehicle:** inspect its accepted fuel and installation. The chemistry guide's [9:1 blend](Guide_to_Chemistry.md#engine-fuel) is accepted by internal engines that already accept gasoline; it does not add compatibility to diesel-only engines.
