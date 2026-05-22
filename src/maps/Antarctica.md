# Antarctica

![Antarctica Map](https://raw.githubusercontent.com/Civ13/Civ13/refs/heads/master/icons/lobby/antarctica.png)

## Overview
A desolate tundra survival scenario where players must keep a central furnace burning to survive. Rescue arrives after 90 minutes of maintaining heat.

**Duration:** 90 minutes (if furnace survives)  
**Objective:** Keep the furnace burning until rescue  
**Difficulty:** High 
**Minimum Players:** 2-3

---

## Starting Equipment

- **Walkie-Talkie** (Faction radio)
- **Flashlight**
- **Survival Knife**
- **Backpack** (empty, for resource gathering)

---

## Key Mechanics

### The Furnace
- **Fuel Requirement:** Furnace consumes fuel over time
- **Critical Point:** If furnace runs out of fuel for **more than 1 minute**, the team loses immediately
- **Win Condition:** Furnace must stay burning for 90 minutes until rescue arrives
- **Status:** Visible to all players in real-time (current win condition display)

### Weather & Environment
- **Time:** Perpetual night
- **Weather:** Random between snowing and blizzards
- **Cold Damage:** Constant environmental hazard; stay near heat sources

---

## Hostile Creatures

### Wendigo
<div style="text-align: center;"><img class="pixelated" src="../images/entities/wendigo.png" width="128" height="128" alt="Wendigo"></div>

**The Hungry Predator**

- **Behavior:** Slow but relentless supernatural hunter with immense damage output
- **Threat Level:** Extreme damage, slow movement

**Stats:** 220 HP | 1 tile/second movement | 30-45 damage | Can bite limbs

### Boreas
<div style="text-align: center;"><img class="pixelated" src="../images/entities/boreas.png" width="128" height="128" alt="Boreas"></div>

**The Hearth-Eater**

- **Behavior:** Massive elemental ice beast that actively hunts and extinguishes fire sources
- **Weakness:** **ONLY takes damage from FIRE** (1.5x multiplied)—all other damage is negated
- **Threat Level:** Extreme danger
- **Strategy:**
  - **CRITICAL:** This creature is immune to physical weapons
  - Use Molotov cocktails, flames, or fire-based weapons ONLY
  - It actively seeks out and extinguishes ovens by consuming their fuel
  - Can open doors to reach furnaces inside buildings
  - Extremely slow (0.7 tiles/second) but relentless
  - DO NOT engage without fire weapons
  - Protect fuel supplies and furnaces with fortifications

**Stats:** 300 HP (takes 1.5x FIRE damage only) | 0.7 tiles/second movement | 20-35 damage | Immune to BRUTE | Extinguishes nearby fuel sources

### Fata Morgana
<div style="text-align: center;"><img class="pixelated" src="../images/entities/fata_morgana.png" width="128" height="128" alt="Fata Morgana"></div>

**The Blizzard Mirage**

- **Behavior:** Disguises itself as other objects; vanishes when touched
- **Effect:** Contact inflicts severe cold damage and disables cold protection for 2 minutes
- **Threat Level:** Deceptive
- **Strategy:**
  - Appears as innocent debris scattered in the environment
  - Deals massive cold damage when touched (100 cold damage units)
  - Disables all cold protection for 2 minutes after contact—exposure is deadly
  - Can appear as anything - assume all debris is suspicious
  - Prioritize staying in heated areas if you encounter one

**Stats:** 1 HP (dies on touch) | Contact effect: 100 cold damage + 2-minute cold protection disable

## Resource Management

### Fuel
- **Primary Resource:** Essential for furnace operation
- **Sources:**
  - Initial furnace inventory (limited)
  - Wood, coal from the map
  - Anything that burns, in an emergency
- **Consumption:** Furnace burns continuously when active
- **Planning:** Establish supply runs to maintain fuel

### Cold Protection
- **Risk:** Constant exposure to extreme cold
- **Mitigation:** Stay near the furnace or indoors
- **Hazard:** Fata Morgana can temporarily disable protections—avoid contact

## Survival Tips

1. **Furnace is King** - Everything revolves around keeping it burning. Plan all activities around fuel collection and furnace maintenance.
2. **Fuel Collection Protocol** - Organize team rotations to gather fuel while others defend the furnace and base.
3. **Watch the Timer** - The furnace status is displayed to everyone
   - If status changes to yellow (off), immediate action is required
   - You have 1 minute to relight it or face defeat
   - No second chances after 1 minute of darkness
4. **Team Coordination** - Communicate constantly
   - Fuel supply status
   - Creature sightings (especially Boreas)
   - Internal base assignments

## Key Takeaway

**Protect the furnace. It is your lifeline. Every other objective is secondary.**
