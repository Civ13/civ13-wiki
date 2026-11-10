# Power & Batteries

Use an [engine and cable network](Guide_to_Crafting.md#engines) to run electrical machinery. Batteries provide limited cable power; they are not mechanical engines and cannot propel modular vehicles. For vehicle construction, use the [Crafting guide](Guide_to_Crafting.md) and [Tanks guide](Guide_to_Tanks.md).

## Choose a battery

These recipes are in the global crafting catalog. Map catalogs, era and character skill requirements still apply; do not assume a Carib or other specialized map offers them. Tech-tree cable recipes require **Electricity**, so an early battery recipe alone does not create a usable electrical network.

| Device | Crafting and commissioning | Capacity / output limit |
| --- | --- | --- |
| Baghdad-style jar cell | Craft an assembly from 2 copper. Fit a fired clay vase, then 1 iron sheet and 10 units of grape juice. | 600 PU s / 1 PU |
| Iron-copper voltaic-style pile | Craft from 5 copper, then add 5 iron sheets and 50 units of grape juice. | 3,000 PU s / 5 PU |
| Lead-acid accumulator | Craft from 5 lead. Add 20 units of sulfuric acid to commission it; it remains empty until electrically charged. | 12,000 PU s / 10 PU; charge limit 10 PU |
| Lithium-ion battery bank | Digital Age, Consumer Electronics research. Craft from 25 electronics. It arrives sealed and commissioned, but empty: charge it like the accumulator. | 48,000 PU s / 40 PU; charge limit 40 PU |

PU is the game's abstract power unit; PU s is stored energy.

## Wind, water and solar generators

These feed the cable grid from the weather instead of fuel. Build them outdoors under open sky; they produce nothing indoors.

| Generator | Era and research | Built from | Peak output |
| --- | --- | --- | --- |
| Wind charger | Early Modern, Electricity | 15 iron | 12 PU |
| Waterwheel generator | Early Modern, Electricity | 15 iron | 12 PU while its river flows |
| Photovoltaic panel | Cold War, Automation | 10 electronics | 10 PU in daylight, nothing at night |
| Wind turbine | Modern, Digital Computing | 30 steel | 45 PU |

Wind output follows the wind speed shown when you examine the generator. The wind charger gives nothing in calm air, its full output in a strong wind, and furls to a fraction of it in a gale. The wind turbine reaches full output in strong winds and keeps it in a gale. Two rotors closer than three tiles share the same air and each loses half its output, so space them out.

The **waterwheel generator** runs on a river current. Rivers flow on Gaia, Europe, Jungle and Asia; lakes, ponds, swamps and the sea are still. Examine the water to see which way it flows. To build a wheel, stand on the bank, face a flowing river tile and craft it: the wheel goes into the water in front of you and turns to face the current. It gives its full output day and night as long as its own tile flows, and nothing in still water. Use a cable coil on the wheel from the bank to run the cable ashore.

**LED panels** (Digital Age, Consumer Electronics, 2 electronics) are light fixtures built like a [light tube](Guide_to_Construction.md#lighting). They light a little farther than a tube, with a whiter light, on a third of the power, and take ordinary replacement tubes.

Machines that use the cable grid include [hydroponics trays](Guide_to_Farming.md#hydroponics) and the belts, arms and fabricators in [Factory Automation](Guide_to_Factory_Automation.md).

## Connect and operate

1. Assemble and commission the battery. Use a wrench to secure it.
2. Stand beside it and use a cable coil on it. Continue the cable network in the matching direction; battery attachment joins neighboring straight cables of the same color and orientation. A cable merely lying nearby does not establish a connection.
3. Click the battery to select its mode. Primary cells cycle **off → discharge → off**. The accumulator and the lithium-ion bank cycle **off → charge → discharge → off**.
4. Examine it to read stored energy, output limit and mode. Switch it off when finished: discharge consumes energy each second even when no machine uses it.

The jar and pile cannot recharge electrically. When empty, switch off, replace the iron electrode and grape juice using the amounts above. The accumulator charges from spare output of running engines on its cable network, after machine loads; another battery cannot charge it.

Cut its cable before unanchoring. Moving or disconnecting a battery turns it off. After a world save is loaded, stored chemical state is retained, but mode, output and wiring must be rebuilt by players. This describes battery save behavior where server world saves are enabled; it does not promise that every round or server retains your settlement.

## Troubleshooting

- **No power:** check commissioning, anchoring, cable attachment, mode and remaining energy. For an accumulator, adding acid does not supply charge.
- **Machine exceeds output:** one accumulator supplies at most 10 PU. The laboratory centrifuge requires 30 PU, so one battery cannot run it. Provide sufficient connected generation; stored capacity alone does not raise output.
- **Cannot craft cables:** check the map catalog, era, skill and Electricity research. Battery availability does not bypass those gates.
- **Engine will not run a vehicle:** inspect its accepted fuel and installation. The chemistry guide's [9:1 blend](Guide_to_Chemistry.md#engine-fuel) is accepted by internal engines that already accept gasoline; it does not add compatibility to diesel-only engines.
