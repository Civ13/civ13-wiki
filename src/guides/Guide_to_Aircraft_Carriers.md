# Aircraft Carriers

An aircraft carrier is a ship forty tiles long and nine wide that is laid down whole at a **shipyard office** and sails as one block across the ocean. It has three decks on three levels: a **hangar deck** below the waterline with six watertight compartments, the **flight deck** at the surface, which is a runway from stern to bow, and an **island** on the level above with the ship's wheel. [Light planes](Guide_to_Aircraft.md) take off from the deck, land on its arresting wires and ride two elevators down to the hangar. Carriers need a world with a level below the sea and open sky above it: at the moment that is **Gaia**, the main Nomads persistent world.

## Research and materials

| Part | Cost | [Tech tree](Guide_to_Research.md) node | [Legacy research](../gamemodes/Civilizations_and_Nomads.md#research) |
| --- | --- | --- | --- |
| Shipyard office | 60 steel | Naval Aviation | Industrial 150 |
| Aircraft carrier | 400 steel, 20 glass, 40 cable | Laid down at the office | Laid down at the office |

**Naval Aviation** is an Industrial node in the Vehicles line. It needs **Powered Flight** and **Submarines**. The office is in the **production** crafting category and only works for a faction that has finished the node.

## Laying the ship down

1. Stand on the shore with the open sea to your **north-east**, lay a power cable, and craft the shipyard office from 60 steel. The ship's stern corner goes on the tile diagonally north-east of the office, and from there it needs a clear box of **deep sea** 40 tiles long and 9 wide along the heading you pick: bow east or west for a box lying east to west, bow north or south for one lying north to south. The office is not built if the research, the cable or the sea is missing, and you are told which heading fails and why.
2. Feed steel, glass and cable stacks into the office, and drag an adjacent laid cable onto it to connect a network with **20 available power**, as for the automobile workshop. Examine the office to see what it holds.
3. Click the office and choose **Aircraft carrier, bow** east, north, west or south. Stay next to it while it works. Nothing is spent until the ship is laid down, and **Unload inputs** returns the stock.
4. The carrier appears anchored, with empty bunkers. Walk onto the flight deck from the shore, or row out to it, climb the ladder on the **starboard** side amidships to the island, and go down the hatch ladder amidships to the hangar deck.

## The decks

- **Hangar deck** (one level down): from stern to bow the engine room, the fuel bunker with the **bunker filling point**, the crew quarters, the hangar, the magazine and the forward compartment, each behind a steel bulkhead with a blast door on the centreline. The two **aircraft elevator** floors are on the port side of the hangar, with a lever beside each. The hangar deck keeps its own air pocket: a hull breach floods the compartment but the ship does not vent.
- **Flight deck** (the surface): steel plating that counts as runway everywhere. The **arresting wires** cross the after deck four tiles wide; the two 4x4 **elevator platforms** lie on the port side with their levers beside them; a hatch ladder amidships goes down to the hangar and a ladder on the starboard side goes up to the island.
- **Island** (one level up): a 5x3 superstructure on the starboard side with the **ship's wheel**.

## Sailing

The ship moves in **hops**: every 30 seconds it shifts along its heading by 2 tiles at slow ahead, 4 at half and 6 at full, with everything and everyone aboard, and the sea closes behind it. Click the **ship's wheel** on the island:

| Choice | What it does |
| --- | --- |
| **Chart** | Position, heading, telegraph, anchor, fuel and hops left, what lies up to 12 tiles ahead of the bow, and why the ship last stopped |
| **Full / Half / Slow ahead**, **All stop** | Ring down a speed; the ship sails only with the anchor up and fuel in the bunkers |
| **Head north / east / south / west** | Come about on the spot; the ship turns about its centre and needs clear sea for the new box |
| **Weigh anchor / Drop anchor** | A ship at anchor never hops, whatever the telegraph says |

The ship stops by itself, with the reason sent to everyone aboard, when land, a pier, another ship or the edge of the world lies in its way, when the bunkers run dry, and while the world is being saved. A blocked full hop tries shorter ones first, so the ship closes up to an obstacle instead of stopping short of it.

### Fuel

The bunkers hold **1000 units** of fuel oil and every hop burns **2 units per telegraph step**: 6 at full ahead, so a full load is about 170 hops at full speed. Pour **diesel** or **petroleum** from any container into the **bunker filling point** in the fuel bunker compartment on the hangar deck; other liquids stay in the container. Examine the valve or read the chart for the level. A dry ship will not take a speed at the wheel until it is bunkered again.

## Flying from the deck

The flight deck is a runway, so the [usual rules](Guide_to_Aircraft.md#flying) apply with a few differences:

- **Take-off:** line up along the deck with 8 clear tiles ahead at full throttle. Keep to the port side of the deck: the island stands on the level you climb into, and a plane lined up under it is refused its climb until it rolls clear.
- **Landing:** fly down the deck in low flight at second gear or slower and **Descend** over the after deck. A plane that touches down on the **arresting wires** is caught by its tailhook and stops at once. One that lands beyond them rolls on at taxi speed, and the **crash barrier** stops it at the deck edge instead of letting it roll into the sea.
- **Elevators:** taxi the plane fully onto one of the 4x4 platforms, switch off, and pull the **lever** beside it. The platform takes the plane and anything else on it down to the hangar; the lever in the hangar brings it back up. The elevator refuses a plane that is half on the platform or still rolling, and a blocked hangar floor below.
- **Hops:** parked planes, crew and cargo ride every hop with the deck. A plane in the air over the ship does not, so land before the ship moves far.

## Tips

- Drop anchor before flying operations: a hop in the middle of a landing roll moves the deck under the plane.
- Keep diesel aboard. The bunker filling point is in the fuel bunker, the second compartment from the stern.
- The carrier survives world saves where it lies, with its fuel, heading and telegraph. Planes left on the deck are saved on it.
