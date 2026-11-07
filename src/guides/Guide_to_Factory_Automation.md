# Factory Automation

From the industrial eras on, a faction can build production lines that run without anyone standing at the machines. Belts carry loose items, powered arms move items between belts, crates and machines, fabricators turn parts into goods, and pipe networks move liquids between wells, refineries, tanks and reaction vessels.

Everything here is built from the crafting menu and needs research on your faction's [tech tree](Guide_to_Research.md). Most pieces need cable power; see [Power & Batteries](Guide_to_Power.md) for generators.

## Research and parts

| Research | Unlocks |
| --- | --- |
| **Factories** | Barrel station, fluid pipe, pipe valve, fluid pump, holding tank, reaction vessel, water intake, water tap, piped shower |
| **Assembly Line** | Factory belt, parts bin, belt drive, assembly fabricator |
| **Automation** | Feeder arm, sorting arm, sorting gate, reagent gate, belt splitter, belt tunnel entrance and exit, fast factory belt, factory monitor, automated fabricator, bottler, fast reaction vessel, pipe meter |
| **Digital Computing** | Stack arm, computerized fabricator, industrial reaction vessel |
| **3D Printing** | 3D printer |
| **Pharmacology** | Automatic tablet press |

Belts, drives, bins, gates, splitters, tunnels, fabricators and all the pipe machines are crafted from steel. Arms, the factory monitor and the higher fabricators also need electronics.

Arms, fabricators, belt drives, the factory monitor, pipes, pumps, tanks, bottlers and the other pipe machines can be unfastened with a wrench and moved, then wrenched down again. An unfastened part does no work: an unfastened pipe joins nothing, and an unfastened tank or pump drops out of its network until it is fastened again. Switch an arm off before wrenching it.

## Belts

A **factory belt** carries loose items toward its arrow and hands them to the next belt, a machine or a crate in front of it. Each belt tile holds up to four items, and items move about two tiles a second. Items on a belt are ordinary floor items, so you can pick them up or examine them at any time.

- Craft a belt, then use it on an adjacent floor tile to lay it running away from you. Turn a laid belt with a wrench; pry it up with a crowbar.
- Belts only run near a running **belt drive**. One drive, cabled and switched on, runs every belt within seven tiles. Belts outside the range of a running drive stand still.
- A **fast factory belt** moves items twice as fast as a plain belt.
- Belts and their direction are kept across server restarts.

### Routing

| Piece | What it does |
| --- | --- |
| **Sorting gate** | Items that match its filter leave by the side; everything else goes straight on. Hold an item and use the **Set Gate Filter** verb to choose the filter. A screwdriver swaps the side. |
| **Reagent gate** | Like a sorting gate, but it sorts containers by the main reagent inside them. Set the filter while holding a container; an empty container makes it sort out empties. |
| **Belt splitter** | Sends items alternately straight on and to the side. A screwdriver swaps the side. |
| **Belt tunnel** | A tunnel entrance carries items underground to a tunnel exit facing the same way, up to six tiles ahead. Use it to cross another line or a wall. |

## Arms and bins

An arm takes items from the tile behind it and sets them down on the tile in front: onto a belt, into a crate or machine, or onto the floor (up to twelve loose items). Wrench it in place, cable it, then click it to switch it on. While it is off, right-click it and use **Rotate Left** or **Rotate Right** to turn it.

| Arm | Moves |
| --- | --- |
| **Feeder arm** | One item of anything per swing. |
| **Sorting arm** | One item per swing, only of its filter kind. Hit it with an item to set the filter; it moves nothing until a filter is set. Use **Clear Filter** to reset it. |
| **Stack arm** | Up to ten items of one kind per swing. It can be given a filter the same way, or left without one to move anything. |

A **parts bin** is a steel crate for a production line. Once it holds something, it only accepts more of the same kind, so each bin stays sorted.

Arms can load and unload:

- belts, crates, parts bins and fabricators;
- **bloomeries and blast furnaces**, which take iron ore and fuel and start smelting on their own once both are loaded;
- the **powered saw mill**, which holds up to 20 logs and cuts one log a second into planks while powered;
- the **powered stamp mill** (see [Stone crushing](#stone-crushing));
- **train wagons and shopping carts**, with the same limits as a person filling them by hand;
- **barrels**, to and from oil wells, refineries, engines and barrel stations.

Machines leave their output on their own tile for an arm to collect. They wait once about twelve stacks have piled up.

## Fabricators

A fabricator turns belt-fed parts into goods from a fixed factory recipe list. Wrench it in place, cable it, then click it to choose a recipe; you can only choose recipes your faction has researched. Arms and belts fill its input buffer, it consumes inputs only when a cycle finishes, and a power cut pauses it without losing anything. Output is left on its tile.

| Fabricator | Research | Speed | Recipes |
| --- | --- | --- | --- |
| Assembly fabricator | Assembly Line | Normal | Tier 1 |
| Automated fabricator | Automation | 25% faster | Tiers 1-2 |
| Computerized fabricator | Digital Computing | Twice as fast | Tiers 1-3 |
| 3D printer | 3D Printing (Digital Age) | Half speed | Printing recipes only |

| Recipe | Makes | From | Tier | Research |
| --- | --- | --- | --- | --- |
| Rolled steel | 4 steel | 5 pig iron | 1 | Assembly Line |
| Barbwire | 3 barbwire | 2 iron | 1 | Assembly Line |
| Bronze | 4 bronze | 3 copper, 1 tin | 1 | Assembly Line |
| Glass | 1 glass | 2 sand | 1 | Assembly Line |
| Metal rods | 2 rods | 1 steel | 1 | Assembly Line |
| Cable coil | 30 cable | 2 copper | 1 | Assembly Line |
| Rifle casings | 3 casings | 1 copper | 1 | Assembly Line |
| Pistol casings | 3 casings | 1 copper | 1 | Assembly Line |
| Iron bullets | 3 bullets | 1 iron | 1 | Assembly Line |
| Ammo clips | 1 empty clip | 1 copper | 1 | Assembly Line |
| Stone bricks | 2 stone bricks | 2 stone | 1 | Assembly Line |
| Wrench | 1 wrench | 5 iron | 1 | Assembly Line |
| Screwdriver | 1 screwdriver | 2 iron | 1 | Assembly Line |
| Claw hammer | 1 hammer | 3 iron | 1 | Assembly Line |
| Wirecutters | 1 wirecutters | 4 steel | 1 | Assembly Line |
| Electronic circuits | 3 electronics | 2 copper, 1 plastic | 2 | Automation |
| Ammo belt | 1 empty belt | 7 copper | 2 | Automation |
| Electronic components | 1 component | 3 electronics, 1 gold | 3 | Digital Computing |

Examine a fabricator to see its recipe, inputs and cycle time.

### 3D printer

The **3D printer** (12 electronics) prints plastic goods. Wrench it down, cable it, choose what to print, then load plastic sheets by hand or with arms and belts. Prints are left in front of it. You can make plastic in a [bakelizer](Guide_to_Crafting.md#bakelizer).

| Print | Makes | Plastic |
| --- | --- | --- |
| Screwdriver | 1 | 1 |
| Dice (d20) | 2 | 1 |
| Bug swatter | 1 | 1 |
| Bottle | 2 | 1 |
| Gallon jug | 1 | 2 |
| Pill pack | 2 | 1 |
| Blood bag (empty) | 1 | 1 |
| Surgical mask | 2 | 1 |
| Bag valve mask | 1 | 2 |
| Hard hat | 1 | 3 |
| Gas mask | 1 | 3, plus 1 glass |
| Traffic cone | 1 | 2 |

## Factory monitor

The **factory monitor** is a terminal that lists every arm, fabricator, belt drive and belt within seven tiles, with what each one is doing (running, waiting, unpowered) and how many items it moves or makes a minute. Use it to find the bottleneck in a line.

## Stone crushing

Surplus stone can be turned into a chance of sand, ore and rare minerals.

- The **stone crusher** is a hand-worked stone wheel (Resource Processing research, 10 stone). Anchor it and use stone blocks on it; it keeps crushing your stack one stone at a time until the stack runs out or you stop. Roughly one stone in five gives sand and, from the Medieval age, about one in seven gives ore; the rest is rubble. Clear the output under it before twelve stacks pile up.
- The **powered stamp mill** (Electricity research) holds up to fifty stone blocks, needs 150 cable power and crushes one stone every four seconds with better recovery than the hand crusher. Arms can load it.

The **primitive saw mill** works the same way as the hand crusher: it keeps cutting your held log stack one log at a time until the stack or the blade runs out, or you stop.

## Pipe networks

Pipes move liquids between machines. A pipe network does nothing until a **powered pump** on it is switched on; then, every two seconds, machines that want a liquid pull it from machines that offer it.

- **Sources** offer liquid: oil wells, water intakes (set beside open water), refinery output, barrel stations set to drain and steel barrels fitted to a pipe.
- **Holding tanks** store liquid. Hold a container and use **Set Tank Filter** to keep a tank to one reagent. Tanks never feed other tanks.
- **Sinks** take liquid: refinery feed, engine fuel tanks, barrel stations set to fill, bottlers, reaction vessels, the automatic tablet press, water taps and piped showers.
- A **pipe valve** splits the network in two while closed. Click it to open or close it.
- A **pipe meter** clamped on a pipe reports that network's pumps, what moved and each machine's state. Its dial lights while liquid is moving.

Contents of tanks and machines are held inert, so they do not react while stored.

### Barrels and the barrel station

Barrels ride belts and arms like any item. Arms can hand barrels to oil wells (which hand them back once full), refineries and engines. A **barrel station** drains barrels that automation brings it into its own tank, or fills them from it, then hands each barrel back out. Use **Switch Station Mode** to choose. A **reagent gate** sorts barrels by their contents.

### Water supply

A **water tap** and a **piped shower** run on whatever the pipes bring them, and go dry when the network stops supplying them. Fill a container at a tap, drink from it on grab intent, or wash your hands in it. A tap gives exactly what came down the pipe, so river water from an intake is still unboiled at the tap. A piped shower only takes water.

To feed the network from a barrel, stand a **steel barrel** on or next to a fastened pipe and use a wrench on it. A fitted barrel offers everything it holds to the network while a pump runs, but it never fills from the pipes. Moving or picking up the barrel, or using the wrench on it again, detaches it. An open barrel left outdoors with nothing overhead catches rain, and dew on clear nights, so a fitted steel barrel can keep a tap supplied. Wood barrels and jerrycans do not fit pipes.

### Reaction vessels

Pipe a **reaction vessel** to your tanks and choose a laboratory recipe. It draws a full batch of that recipe's inputs in the right ratio, reacts them with power, then lets everything except the catalysts out to the network. Use holding-tank filters to separate the product from leftovers. Fast (Automation) and industrial (Digital Computing) reaction vessels work bigger batches faster. See [Chemistry](Guide_to_Chemistry.md) for the recipes.

### Packaging

- The **bottler** takes open containers from belts and arms, fills each one with its chosen reagent from the pipes and hands it back full. Hold a filled container and use **Set Bottler Reagent** to choose the reagent.
- The **automatic tablet press** draws calcium carbonate and aspirin from its pipes and presses aspirin tablets onto its tile for arms to take.
