# Aircraft

Light planes are the first things in Civ13 that leave the ground. There are two models: the two-seat **light plane** and the four-seat **cabin plane**. Both are built at an **aircraft hangar**, takes off and lands best on a **runway**, and flies on the air level above the map. Flying is only possible on maps that have an air level: at the moment that is **Gaia**, the main Nomads persistent world. Elsewhere the plane rolls along but never lifts off, and the pilot is told that there is no airspace.

![Offline render using Civ13 sprites: two light planes on a tarmac runway laid across grass, one parked and one with its propeller spinning](../images/civ13-light-plane-sprites.png)

Two light planes on a runway, nose to the east. Offline render using Civ13 sprites, not a live screenshot.

## Research and materials

| Part | Cost | [Tech tree](Guide_to_Research.md) node | [Legacy research](../gamemodes/Civilizations_and_Nomads.md#research) |
| --- | --- | --- | --- |
| Aircraft hangar | 40 steel | Powered Flight | Industrial 126 |
| Runway (one tile) | 1 stone | Powered Flight | Industrial 126 |
| Light plane | 50 steel, 6 glass, 4 cloth, 8 cable, 4 unattached wheels | Built at the hangar | Built at the hangar |
| Cabin plane | 65 steel, 8 glass, 8 cloth, 8 cable, 4 unattached wheels | Built at the hangar | Built at the hangar |
| Aircraft bomb casing | 8 steel | Powered Flight | Industrial 126 |
| Airframe section | 4 steel | Powered Flight | Industrial 126 |
| Airframe controls | 12 steel | Powered Flight | Industrial 126 |
| Pilot's seat | 8 steel | Powered Flight | Industrial 126 |

**Powered Flight** is an Industrial node in the Vehicles line. It needs **Automobiles** and **Combustion Engine**, and Aviation & Rocketry is researched after it. The hangar is in the **production** crafting category and runway in **roads**. The hangar only assembles planes for a faction that has finished the Powered Flight node.

## Building the hangar and the plane

1. Lay a power cable, then craft the aircraft hangar from 40 steel while standing on or next to the cable. The **4x4** square to its **northeast** must be dry, open floor: the finished plane appears there. The hangar is not built if the research, the bay or the cable is missing, and you are told which.
2. Feed steel, glass, cloth and cable stacks into the hangar, and drag four unused, unbroken, unattached wheels onto it. Drag an adjacent laid cable onto it to connect a network with **20 available power**, as for the automobile workshop. Examine the hangar to see what it holds.
3. Click the hangar, choose **Light plane** or **Cabin plane** and stay next to it while it works. Loose objects or people in the bay stop the assembly, and nothing is spent until the plane is finished. **Unload inputs** returns the stock.
4. The plane is delivered with a gasoline engine, an **empty** fuel tank and its key. Fill the tank with gasoline before you try to taxi; see [Engines](Guide_to_Crafting.md#engines) for fuel.

The plane can also be built **piece by piece**, by several people. Choose **Start a Light plane piece by piece** with the bay clear. Then bring each piece in turn to the hangar or to the airframe in the bay: the **airframe** (2 pieces, 10 steel each), **landing gear** (4 wheels, dragged on), the **engine and propeller** (10 steel and 8 cable), the **skin** (2 pieces, 10 steel each), the **canopy** (6 glass) and the **seats** (4 cloth). The plane takes shape from the tail to the nose. Fitting pieces needs no power. When the last piece is on, choose **Roll out**, which needs 20 power and gives the same plane, key and empty tank as a one-go build. A half-built plane survives saves, and **Abandon** loses everything fitted so far. The bay cannot hangar a plane while a project is in it. See [Building a car piece by piece](Guide_to_Crafting.md#building-a-car-piece-by-piece) for how stacks and wheels are taken.

The light plane is four tiles long and three wide: the nose with the engine and propeller, the cockpit between the wings, a fuselage section with one passenger seat, and the tail. The pilot sits in the cockpit and flies from the **control column**.

The **cabin plane** has the same airframe and size, so it fits the same hangar bay and carrier elevators, but its whole fuselage row is a cabin with **three passenger seats**. The extra weight needs a longer take-off roll: **10 tiles** of runway or **20** of open ground. Built piece by piece, it takes the same pieces as the light plane, with 8 cloth for the seats.

## Building a plane by hand

Without a hangar, a plane can be put together from loose parts like a [hand-built vehicle](Guide_to_Crafting.md#modular-tanks). Craft the airframe sections, airframe controls and pilot's seat in the **vehicle parts** category.

1. Lay airframe sections side by side in a rectangle **3 sections wide** and **3 to 5 long**. The 3 is the wingspan; the long side runs from nose to tail.
2. Stand the parts on the sections: an engine and a fuel tank (on the middle of the front row, so the engine turns the propeller), the **pilot's seat** on the middle of the second row, a wheel on each of the four corners, and passenger seats anywhere behind. A car's driver's seat does not fly a plane.
3. Put the airframe controls on any section and click them. The survey says what the airframe still needs. Choose **Assemble it**, then pick which way the nose points: along the long side.

Every section takes the shape its place calls for: the front row becomes the nose, the second row the wings with the cockpit under the pilot, the last row the tail and anything between the fuselage. A **3 by 3** plane is a short trainer, **3 by 4** has the light plane's shape, and **3 by 5** is a long transport. Planes longer than the light plane need a longer take-off roll, one more runway tile for every two extra sections, and a 5-long plane does not fit a 4x4 hangar bay. Parts stood on it later are fitted with **Fit new parts**, and its builders can **Take it apart** again. Fill the tank and it flies like any other plane.

## Laying a runway

Runway is a road cover crafted from **1 stone per tile** in the roads category, like a modern road. A take-off needs **8 tiles** of straight runway in front of the plane at full throttle, against **16 tiles** of open ground without one, after pressing **Climb** to line up. A runway is not needed to land: flat, smooth ground works too. A long runway is just the easiest target. Lay it three tiles wide so the whole plane is over tarmac, and keep the ends clear of walls, trees and vehicles.

## Taxiing

On the ground a plane drives like a car. Start the engine with the control column, throttle up a gear, steer with the arrow keys and switch to reverse while stopped with the down arrow or the HUD button. You can taxi in any gear along roads, aprons and runways, into and out of a hangar bay, without lifting off by accident: away from a runway the plane only leaves the ground once you have lined it up for a takeoff (see below). The HUD shows **PARKED** or **TAXI** while you are on the ground, and **TAKEOFF** once you have lined up. A plane that has just landed rolls on at first gear, ready to taxi.

## Flying

| Control | What it does |
| --- | --- |
| Use the control column | Throttle up one gear |
| Right-click the control column | Throttle down one gear |
| Arrow keys | Steer |
| **Climb** (verb on the control column, or the HUD button) | In the air, aim 5 height levels higher. On the ground, with the engine running, it lines the plane up for takeoff and tells you what is still needed |
| **Descend** (verb or HUD button) | Aim 5 height levels lower; just above the ground at low speed, land |

The HUD shows the plane's height while you are in the pilot's seat, such as **LOW 7** or **HIGH 18**. Examining the control column also shows how far above the ground you are and the height you are heading for.

- **Take-off:** on a runway, throttle to full and roll straight ahead: after 8 tiles of runway the plane takes off by itself. Off a runway, press **Climb** first to line up, then roll 16 tiles of open ground at full throttle. Without that, a full-throttle roll over open ground just keeps taxiing. The wheels leave the ground two levels up and the plane climbs on to height 6 in **low flight**. Coming to a stop against something stands the takeoff down again.
- **Height:** a plane's height uses the same 0 to 15 scale as the hills. It climbs or sinks 2 levels for every tile it flies, toward the height you set with Climb and Descend.
- **Low flight (height 15 and below):** the plane flies among the hills. Anything ahead that reaches its height is flown into: a hillside, a tree or a wall (3 levels above the ground it stands on), or an upper storey. A **Terrain ahead** warning tells you the height of ground within 5 tiles in front of you that you would hit, so climb above it in time. Anyone can shoot at a plane in low flight.
- **Cruise (above 15):** past the top of the hill scale the plane cruises over every hill, tree and rooftop, and only heavy weapons reach it. It cannot sink back into low flight over an upper storey or the highest peaks, and you have to come down to low flight before you can land. The pilot sees the ground below from the cockpit, and people on the ground see the plane's shadow pass over them.
- **Stalling:** a plane that flies slower than **second gear** for 3 seconds, or whose engine stops, stalls and crash-lands on the nearest clear ground below. You get one warning to throttle up first.
- **Map edge:** the plane stops at the edge of the world and warns you. Turn back at once, because a plane that stays there stalls.
- **Fuel:** flying burns fuel faster than driving, and low flight burns the most. A full tank lasts about four minutes of low flight. Watch the tank, because an engine that runs dry in the air is a stall.

## Landing

Descend until the plane skims just above the ground, then fly at **second gear or slower** and **Descend** once more. Too fast, and the plane stays in the air and tells you to slow down.

- **On a runway:** a smooth landing. At least half of the airframe has to be over runway for the wheels to find it. The flight deck of an [aircraft carrier](Guide_to_Aircraft_Carriers.md) is a runway too, and its arresting wires stop the plane on the spot.
- **On flat open ground:** with no runway below, the plane can set down on dry, open ground such as grass, dirt, sand, snow, roads or floors, with nothing standing in the way under any part of the airframe. Where that ground is **perfectly level** under the whole plane (no step in height between neighbouring tiles; built floors and roads count as level) and has no loose rock or gravel, the landing is as smooth as on a runway: no damage, and the plane rolls on at taxi speed.
- **On a gentle slope or rocky ground:** where the ground under the plane differs by one height level, or there is rock or gravel under it, the plane still lands, but in a **rough landing**: it bounces down, stops dead and the airframe takes damage, which a weld repairs. A plane whose airframe is already badly torn also breaks its landing gear. Steeper ground than that is no place to land.
- **Over water, trenches or obstacles:** the plane warns you and keeps flying so you can go round again.

Where you cannot land, **Descend twice within 5 seconds** to force a crash landing. The plane comes down on the nearest clear ground with its engine off and its landing gear broken, and the crew are bruised. With no clear ground within reach the airframe breaks up and everyone aboard falls.

## Arming the plane

A light plane can carry a gun and two bombs:

- **Nose gun:** take any light machine gun, such as a Madsen or a Type 99, and use it on the **nose** section of the plane to bolt it in. Use a magazine on the nose section to load it, and a **wrench** to take the gun out again. Examine the nose to see what is mounted and how many rounds are left.
- **Firing:** with the control column in one hand and the other free, choose **Fire guns** on the column. The burst goes straight along the plane's heading from the nose: down the runway on the ground, or onto the ground ahead of the nose in low flight, so you strafe by flying low over the target. From cruise height you are too high to aim.
- **Bombs:** craft an **aircraft bomb casing** from steel (in the **weapons** menu, after Powered Flight) and fill it with ten units of [nitroglycerin](Guide_to_Chemistry.md) from any container. Use the filled bomb on a **wing** section to hang it; each wing takes one. A wrench takes a bomb down again.
- **Bombing:** in the air, choose **Drop bomb** on the column. The bomb falls onto the ground directly under the middle of the plane and bursts there, so fly low and straight over the target. Bombs cannot be dropped on the ground.

Filled bombs go off when a heavy blast reaches them, on the plane or in a store, so keep them apart from anything else that explodes. An empty casing is harmless.

## Damage and repair

People on the ground can shoot at a plane as it passes over them:

- In **low flight** any gun that fires across the ground under the plane has a **40%** chance of hitting it.
- At **cruise** height only heavy weapons reach it, such as heavy machine guns, cannon and shells, with a **20%** chance.

Every hit tears the airframe and can break a wheel, and hits on the nose can stop the engine. When accumulated damage reaches the airframe's limit the plane fails and comes down as a crash landing. Examine the plane to read its damage, and **weld** any frame section on the ground to mend the airframe. A crash breaks the landing gear, and the plane will not roll until it is fixed. The landing gear counts as one part: once the airframe is whole, one more weld on any frame section, or welding any one wheel, fixes every wheel.

## Hangaring a plane

The aircraft hangar also stores up to **2 planes** off the map. A plane in the hangar is not on the airfield, so it cannot be shot, stolen or caught by a save while it is in the air.

1. Land, then taxi the plane into the 4x4 bay to the northeast of the hangar, where planes are built. The whole airframe has to be inside the bay. Runway under the bay is fine.
2. Switch the engine off, get everyone out and take loose items off it.
3. Click the hangar and choose **Hangar the parked aircraft**. Stay next to it for a few seconds.
4. To fly again, clear the bay and choose **Roll out a hangared aircraft**. The plane comes back where it was parked, with the same fuel and damage.

You need to hold the plane's key to hangar it and to roll it out. Examine the hangar to see which planes it holds. Cars go in a [vehicle garage](Guide_to_Crafting.md#vehicle-garage).

## Towing a plane

A plane on the ground can be towed like a car. Park it in line behind a truck or another vehicle, both facing the same way and standing still, within 2 tiles, and use a **rope** on the plane. It then rolls and turns wherever the tug goes, which is handy for pulling a plane out of a hangar bay or along a taxiway without starting its engine. The tug pulls the plane's weight too: a light plane is too heavy for a small car, so use a truck. A plane cannot take off while it is on a tow line, and a plane in the air cannot take one. Right-click either vehicle and choose **Cast Off Tow Line** to let go.

## Tips

- Hangar the plane when you are done flying. A hangared plane is kept safe across saves.
- Land before a save. A plane saved in the air is set down on the ground below when the world loads, and that is a hard landing with broken wheels unless the ground directly beneath it is clear.
- Pick a flat meadow or a road when there is no runway. Level, smooth ground is a free landing; a slope or rocky patch costs airframe damage every time, and a torn plane lands on broken wheels.
- Build the runway right out of the hangar bay. The plane is delivered facing south on the 4x4 square northeast of the hangar, so a strip running south from there is the shortest taxi.
