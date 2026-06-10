# Subcom13 (Submarine Commander)

```admonish warning
This game mode is currently a **Work In Progress**. Mechanics, balance, and vessel stats are subject to change. Report bugs and feedback on the Civ13 GitHub.
```

---

## Introduction

**Subcom13** is a submarine warfare simulation mode set on a fictional 1000x1000 nautical mile coordinate grid. You command a submarine (or crew one with other players) and must navigate the open ocean, engage hostile surface and air contacts, manage your ship's reactor and crew survival, and complete objectives relayed to you over encrypted radio.

The mode features:

- **Real-time navigation** on a virtual overworld map with heading, speed, and depth control
- **Nuclear and diesel-electric** submarine propulsion options
- **Weapons systems**: torpedoes with acoustic homing, fire control consoles
- **Sensor suites**: passive and active sonar, surface radar
- **Environmental simulation**: hull breaches, flooding, water accumulation, and atmospheric pressure
- **NPC hostile contacts**: surface combatants, aircraft, and enemy submarines with AI
- **Mission objectives**: sink cargo ships, patrol sectors, escort allies, recon, rescue, and ambush
- **Crew management**: track individual crew health, oxygen status, injuries, and assignments
- **Single-player mode**: toggle via admin panel to allow ghosts to operate machinery

---

## Submarine Controls

Your submarine is controlled from the bridge consoles. Each console is an `Alt+Click` interaction.

### Helm Control Station

The primary navigation console. Controls heading, speed, and depth.

| Control | Description |
| :--- | :--- |
| **Target Heading** | Set in degrees (0-359). The sub turns toward this heading automatically. |
| **Target Speed** | Set in knots. Your sub accelerates/decelerates toward this value. |
| **Target Depth** | Pre-set depth buttons: Surface (0m), Periscope (15m), Deep (150m), Crash Dive (250m). |
| **Emergency Blow Ballast** | Instantly vents all ballast tanks and surfaces the sub. |

```admonish tip
Diesel-only submarines can only produce propulsion power when surfaced. Submerged, you run on battery at reduced speed (8 knots max).
```

### Reactor Control Station

Manages the two nuclear reactors. Each reactor operates independently.

| Control | Description |
| :--- | :--- |
| **Control Rods** | 0-100%. Lower = more heat, more power. 100% = fully inserted (shutdown). |
| **Primary Pump** | Coolant flow rate (0-18 RPM). Higher = better heat dissipation. |
| **Secondary Pump** | Turbine steam flow (0-10 RPM). Determines power output in MW. |
| **SCRAM** | Emergency shutdown. Inserts rods to 100% instantly. |

**Reactor Meltdown**: If core temperature exceeds 1000 C, the reactor melts down. This causes radiation damage in the reactor room and permanently disables that reactor. There is no recovery from a meltdown.

```admonish danger
Never pull control rods below 25% without sufficient primary pump speed. Heat will spiral out of control and cause a meltdown within seconds.
```

**Power Output**: You need at least 5 MW total (combined from both reactors) to run the nuclear turbines for full-speed propulsion (30 knots).

### Auxiliary Systems Console

Controls environmental systems and battery power.

| Control | Description |
| :--- | :--- |
| **O2 Generator** | Toggles electrolysis. Generates oxygen across all compartments. |
| **Battery** | Current charge / max capacity in kWh. Drains when running on electric power. |
| **Ventilation** | Per-compartment vent controls. Open/close vents to equalize air between rooms. |
| **Fire Suppression** | Activates fire suppression in a compartment. |

### Radar Console

Surface detection system. **Only works when surfaced.**

| Control | Description |
| :--- | :--- |
| **Power** | Toggle radar on/off (surface only). |
| **Range** | Toggle between Short (20km) and Long (50km). Long range uses more power. |
| **Detected Contacts** | Shows surface contacts: name, range, bearing. |

### Sonar Console

Underwater detection system. Works at any depth.

| Control | Description |
| :--- | :--- |
| **Power** | Toggle sonar on/off. |
| **Mode** | Toggle between **Passive** (stealth, only detects submerged contacts) and **Active** (loud ping, detects all contacts but reveals your position). |
| **LOFAR Analysis** | Frequency analysis display. Shows propeller cavitation and engine harmonics. |
| **Detected Contacts** | Shows submerged contacts: name, range, bearing, noise signature. |

```admonish warning
Active sonar emits a loud ping that hostile NPCs can detect from long range. Use passive sonar when trying to remain undetected.
```

### Weapons Control Station

Torpedo fire control system.

| Control | Description |
| :--- | :--- |
| **Master Arm** | Must be ON to fire torpedoes. |
| **Tube Status** | Shows which of the 4 tubes are loaded/empty. |
| **Target Selection** | Select a detected contact as your target. Torpedoes home toward the selected target. |
| **Launch** | Fires a torpedo from a loaded tube toward the selected target. |

**Torpedo Stats**: 40 knots, 800 unit range, 150 base hull damage. Homing torpedoes track the target automatically.

### Radio Console

Encrypted command communications. Receives mission objectives and displays mission status.

| Control | Description |
| :--- | :--- |
| **Transmission Log** | Shows all received messages with timestamps. |
| **Mission Status** | Shows current objective type, target coordinates, and target integrity. |
| **Fast Travel** | Engages 10x speed multiplier. Auto-disables when a hostile contact is nearby or if speed drops below 5 knots. |

---

## Flooding & Water Physics

When your submarine takes damage (torpedo hits, depth charges, crush depth), hull breaches can occur, flooding compartments with seawater.

### How Flooding Works

1. **Hull Breach**: A damaged hull wall loses integrity. When it fails, water begins pouring in.
2. **Water Accumulation**: Deck tiles accumulate water measured in centimeters (0 = dry, 200 = fully flooded).
3. **Water Spreading**: Water flows to adjacent tiles within the same compartment, equalizing depth.
4. **Bulkhead Containment**: Internal bulkheads are watertight by default. If a bulkhead is destroyed, water flows through it to adjacent compartments.

### Water Depth Effects

| Depth | Effect |
| :--- | :--- |
| 0-29 cm | Thin film. No gameplay effect. |
| 30-49 cm | Ankle-deep. Visual change. |
| 50-99 cm | **Drowning risk begins**. Minor respiratory stress. |
| 100-149 cm | **Waist deep**. Movement is difficult. Continuous breathing difficulty. |
| 150-199 cm | **Chest deep**. Heavy damage, severe drowning, CO2 buildup. |
| 200 cm | **Fully flooded**. Tile is underwater. |

### Bilge Pumps

Located in various compartments. Activate by clicking them.

- **Standard Bilge Pump**: Drains water from its tile and adjacent tiles. Uses 15 kW.
- **Emergency Bilge Pump**: Drains water from a single tile only. Uses 8 kW.

```admonish note
Bilge pumps require battery power. If your battery is dead, the pumps will not function. Prioritize keeping the diesel generators running if your reactors are offline.
```

### Hull Breach Sealant Sprayer

An automated device that scans for breached hull walls and seals them with fast-curing polymer. Each use consumes one unit of sealant (100 units total). Requires power to operate.

---

## Atmospheric System

Each compartment has independent atmospheric simulation:

- **Oxygen (O2)**: Consumed by breathing. Depleted O2 causes suffocation. Replenished by the O2 generator.
- **Carbon Dioxide (CO2)**: Produced by breathing. High levels cause respiratory distress and CO2 poisoning.
- **Pressure**: Normal = 1 atm (101.325 kPa).

### Ventilation Ducts

Link compartments together for air sharing. All ducts with the same vent ID form a network. Air gradually equalizes across the network.

| Object | Function |
| :--- | :--- |
| **Ventilation Duct** | Passive air equalization. Click to open/close. |
| **CO2 Scrubber** | Active CO2 removal. Optionally injects O2. Uses 25 kW. |

```admonish tip
If a compartment is flooding, the water displaces oxygen. A fully flooded compartment will have almost no breathable air. Prioritize evacuation or O2 injection.
```

---

## Vessel Roster

### Player Submarine

| Stat | Nuclear Sub | Diesel Sub |
| :--- | :--- | :--- |
| **Max Speed (surfaced)** | 30 knots | 18 knots |
| **Max Speed (submerged)** | 30 knots | 8 knots (battery) |
| **Propulsion** | Nuclear reactors | Diesel generators (surfaced only) |
| **Battery** | 3000 kWh | 3000 kWh |
| **Diesel Fuel** | 40000 L (backup) | 40000 L (primary) |
| **Crush Depth** | 300m | 300m |
| **Torpedo Tubes** | 4 | 4 |

### Hostile Surface Combatants

| Vessel | Type | Speed | Hull | Sensors | Weapons |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Oliver Hazard Perry FFG** | Frigate | 30 kts | 800 | Sensor 40km, Sonar 25km | Harpoon Missiles, Mk 46 Torpedoes |
| **Kirov CGN** | Battlecruiser | 28 kts | 1200 | Sensor 50km, Sonar 30km | P-700 Granit, SS-N-14 Silex, 53-65 Torpedoes |
| **Krivak FFG** | Frigate | 26 kts | 600 | Sensor 35km, Sonar 20km | RBU-6000 Depth Charges, SET-65 Torpedoes |
| **Nanuchka Corvette** | Corvette | 32 kts | 450 | Sensor 25km, Sonar 15km | P-120 Malakhit, 40mm CIWS |
| **Grisha MPK** | Patrol Boat | 24 kts | 350 | Sensor 20km, Sonar 18km | RBU-2500 Depth Charges, SA-N-4 Gecko |

### Hostile Submarines

| Vessel | Type | Speed | Hull | Sensors | Weapons |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Kilo-class SSK** | Diesel Sub | 18 kts | 700 | Sensor 30km, Sonar 35km | TEST-71 Torpedoes, Type 65-76 Torpedoes |
| **Akula-class SSN** | Nuclear Sub | 30 kts | 900 | Sensor 40km, Sonar 45km | SS-N-16 Stallion, 53-65K Torpedoes |
| **Delta III SSBN** | Ballistic Sub | 22 kts | 1100 | Sensor 25km, Sonar 30km | R-29 Vysota SLBM, 53-65M Torpedoes |

### Hostile Aircraft

| Aircraft | Type | Speed | Hull | Sensors | Weapons |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tu-22M Backfire** | Bomber | 50 kts | 400 | Sensor 80km | AS-4 Kitchen, AS-6 Kingfish |
| **Su-24 Fencer** | Strike | 45 kts | 300 | Sensor 60km | AS-7 Kerry, FAB-500 Bombs |
| **Il-38 May** | ASW Patrol | 38 kts | 350 | Sensor 70km, Sonar 10km | RGB-1N Torpedoes, RGB-2 Depth Charges |

### Neutral / Mission Targets

| Vessel | Type | Speed | Hull | Sensors | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bulk Cargo Freighter** | Cargo | 15 kts | 500 | Sensor 15km | Large radar signature. Common mission target. |
| **Fleet Oil Tanker** | Tanker | 12 kts | 400 | Sensor 12km | Very large signature. Catastrophic explosion on death. |

---

## AI Behavior

Hostile NPCs use a three-state AI with tactical movement:

| State | Behavior |
| :--- | :--- |
| **PATROL** | Moves between random waypoints at patrol speed. Non-hostile until detection. |
| **HUNT** | Triggered when the NPC detects the player. Moves toward the player's last known position at attack speed. |
| **ATTACK** | When within weapon range, the NPC **circle-strafes** around the player while firing weapons. Maintains a tight orbit to avoid torpedo lock. Reverts to HUNT if the player moves out of range. |

**Detection Triggers**:
- **Passive Sonar**: NPC detects you if your noise level exceeds their threshold. Noise increases with speed and active sonar use.
- **Active Sonar Ping**: If you use active sonar within the NPC's sonar range, they instantly know your position.

**Tactical Behavior**:
- NPCs circle in a random direction around you while attacking
- They fire one weapon at a time with cooldown management
- If you move too far away, they switch to HUNT to chase you

```admonish tip
Stay deep and slow to minimize your noise signature. A submarine running at 5 knots at 200m depth is extremely difficult to detect passively.
```

---

## Crew Management

The submarine tracks individual crew members and their status. Crew are automatically detected when they board the submarine.

### Crew Member Status

Each crew member is tracked with:

| Stat | Description |
| :--- | :--- |
| **Health** | Current health percentage (0-100) |
| **Total Damage** | Sum of all damage types |
| **Conscious** | Unconscious or dead |
| **Injured** | Has significant damage |
| **Oxygen Status** | "Nominal", "Low O2", "Suffocating", or "Drowning" |
| **Compartment** | Current location (e.g., "Operations", "Reactor Room") |
| **Assignment** | Job title (Captain, Officer, Crewman) |
| **Role** | Command role (Captain, Officer, or Crew) |

### Crew Tracking

The submarine automatically:
- Detects crew members when they board
- Updates their health, oxygen, and location status
- Removes dead crew from tracking

---

## Mission System

Missions are relayed to you over the radio console. Complete objectives to earn mission points and progress through the game.

### Mission Types

| Type | Objective | Completion | Failure |
| :--- | :--- | :--- | :--- |
| **Sink Cargo** | Destroy a hostile cargo vessel at target coordinates | Sink the target vessel | Target escapes or time runs out |
| **Patrol Area** | Navigate to and patrol a sector | Reach coordinates and survive | Take too much damage or time runs out |
| **Escort** | Protect a friendly cargo vessel to waypoint | Cargo survives to destination | Cargo is destroyed |
| **Recon** | Investigate coordinates and observe | Reach target and maintain position | Take damage or leave area |
| **Rescue** | Find and escort a damaged allied submarine | Escort sub to safe waters | Allied sub is destroyed |
| **Ambush** | Set up and eliminate a hostile patrol group | Destroy all hostiles | Fail to eliminate all or time runs out |

### Mission Frequency

Missions arrive periodically with a brief delay between objectives. Check your radio console regularly for new orders.

```admonish note
Some mission types are rarer than others. Sink and patrol missions are most common, while rescue missions are extremely rare.
```

---

## Single Player Mode

Single-player mode allows ghosts to interact with submarine machinery, enabling solo play without other human crew.

### How to Enable

1. Open the **Server** tab in the game menu
2. Select **"Toggle Single Player Mode"**
3. Requires admin privileges

### Effects

When enabled:
- Ghosts can interact with all submarine consoles and physical machinery
- Dead players can operate systems while observing

When disabled:
- Only living players can interact with machinery
- Ghosts cannot operate systems

```admonish note
Single-player mode is intended for testing and solo gameplay. It can be toggled at any time by an administrator.
```

---

## Physical Machinery (Interior)

These objects exist on the submarine's interior and can be interacted with directly.

| Object | Location | Interaction |
| :--- | :--- | :--- |
| **Reactor Core** | Reactor Room | Visual indicator of reactor status. Emits radiation if damaged. |
| **Coolant Pump** | Reactor Room | Degrades with damage. Damaged pumps reduce cooling efficiency. |
| **Steam Turbine** | Engine Room | Caps max speed based on health. Makes noise at high speeds. |
| **Diesel Engine** | Engine Room | Carbon buildup at low throttle. Overheats at high throttle. |
| **Diesel Propulsion Motor** | Engine Room (diesel only) | Converts diesel power to thrust. Overheats and seizes if damaged. |
| **Torpedo Tube** | Forward/Aft Torpedo Room | Load/unload torpedoes. Click with a torpedo item to load, crowbar to unload. |
| **HTP Fuel Tank** | Torpedo Room | High-test peroxide storage. Volatile if damaged or heated. |
| **Bunk Bed** | Crew Quarters | Rest area. |
| **Galley** | Galley | Food processor. Produces nutritional rations when clicked. |
| **Equipment Locker** | Various | Contains gas masks, welding tools, fire extinguishers, and basic tools. |
| **Stern Plane** | External | Affects steering efficiency. Must be repaired while surfaced. |
| **Bilge Pump** | Various Compartments | Drains water from tiles. |
| **Hull Breach Sealant Sprayer** | Various Compartments | Seals breached hull walls. |
| **Ventilation Duct** | Various Compartments | Equalizes air between compartments. Click to open/close. |
| **CO2 Scrubber** | Various Compartments | Removes CO2, optionally injects O2. |
| **Ballast Control Valve** | Operations | Controls ballast tank flooding/venting for depth control. |

---

## Quick Reference

| Situation | Action |
| :--- | :--- |
| Taking on water | Activate bilge pumps. Seal breaches with welder or sealant sprayer. |
| Running out of air | Turn on O2 generator. Open ventilation ducts. |
| Reactor overheating | Increase primary pump speed. Insert control rods. SCRAM if critical. |
| Enemy detected on sonar | Go deep (150m+), reduce speed to 5 knots, go silent. |
| Need to fire torpedoes | Master Arm ON. Select target from sonar contacts. Load tube. Launch. |
| Battery dead | Surface and engage diesel throttle to recharge. |
| Crush depth warning | Increase target depth. Check ballast. Emergency blow if needed. |
| Crew member injured | Check crew status via submarine console. Move to medical bay. |
| Crew suffocating | Check oxygen status. Inject O2 into compartment or evacuate. |
| Solo play needed | Toggle Single Player Mode in Server tab (admin only). |
| NPC attacking | Go deep and slow. Use passive sonar. Avoid active sonar pings. |
| Mission received | Check radio console for coordinates. Navigate to target area. |
| Multiple hull breaches | Emergency blow to surface. Activate all bilge pumps. Seal breaches. |
