# Lights Out

<dmi-sprite src="https://raw.githubusercontent.com/civ13/civ13/master/icons/lobby/lights_out.dmi" state="lights_out" dir="south" animated="true" scale="1"></dmi-sprite>

## Overview
A hostile, pitch-black jungle survival scenario where players must reach an extraction zone to escape.

**Objective:** Reach the extraction zone and survive for 30 seconds within it  
**Difficulty:** High
**Minimum Players:** 3-4

---

## Starting Equipment

- **Kevlar Armor** and **Helmet**
- **Walkie-Talkie** (Faction radio)
- **Flashlight** (Low intensity dark red)
- **M9 Beretta Pistol** (loaded)
- **Backpack** containing:
  - 2x M9 Beretta magazines
  - Advanced bruise pack
  - Morphine syringe

---

## Key Mechanics

### Extraction Zone
- **Location:** Randomly selected from 3 possible zones
- **Victory:** Occurs when a conscious human remains in the zone for the full duration (30 seconds)

## Hostile Creatures

### Lightseeker
<div style="text-align: center;"><img class="pixelated" src="../images/entities/lightseeker.png" width="128" height="128" alt="Lightseeker"></div>

**The Light Hunter**

- **Behavior:** Extremely fast but fragile predator that hunts light sources
- **Weakness:** Stays dormant in complete darkness
- **Threat Level:** High speed, low health
- **Strategy:**
  - Turn off your flashlight when you encounter one
  - Only activates when someone is carrying a lit light source or standing adjacent
  - Extinguish all nearby light sources to avoid detection
  - Fight in darkness to gain advantage

**Stats:** 55 HP | 5 tiles/second movement | 8-16 damage

### Echofiend
<div style="text-align: center;"><img class="pixelated" src="../images/entities/echofiend.png" width="128" height="128" alt="Echofiend"></div>

**The Sound Reactor**

- **Behavior:** Blind creature that hunts based on sound; reacts violently to noise
- **Weakness:** Silence and low noise
- **Threat Level:** Medium
- **Strategy:**
  - Move silently when possible
  - Avoid shouting or making loud noises
  - Once it detects you, it will pursue aggressively
  - Can be outrun but will chase up to 6 tiles away

**Stats:** 120 HP | 3 tiles/second movement | 15-25 damage

### Phosphor Beetle
<div style="text-align: center;"><img class="pixelated" src="../images/entities/phosphor_beetle.png" width="128" height="128" alt="Phosphor Beetle"></div>

**The Toxic Scarab**

- **Behavior:** Fast, weak but deadly—explodes in toxic green dye on contact
- **Effect:** Causes a glowing green effect that lasts 60 ticks, marking you as visible
- **Threat Level:** Medium (indirect)
- **Strategy:**
  - The dye makes you visible to other creatures
  - Avoid letting it touch you if possible
  - The dye effect attracts other hunters
  - Kill quickly or avoid engagement

**Stats:** 40 HP | 5 tiles/second movement | 2-5 damage | Explodes on contact

### Canopy Strangler
<div style="text-align: center;"><img class="pixelated" src="../images/entities/vine_strangler.png" width="128" height="128" alt="Canopy Strangler"></div>

**The Ambush Vine**

- **Behavior:** Hangs from the canopy and chokes anything that walks beneath it
- **Weakness:** Can be pulled free or killed from above
- **Threat Level:** Deadly if caught
- **Strategy:**
  - Watch for vines hanging above you as you move
  - Once caught, you cannot move—you are helpless
  - Can be freed by allies with disarm intent (30% success per attempt)
  - The strangler deals continuous damage while choking
  - Walk with caution through dense jungle areas

**Stats:** 80 HP | Anchored/stationary | 5-10 Oxy/Brute damage

---

## Survival Tips

1. **Use Light Strategically** - Your flashlight is essential but attracts Lightseekers. Turn it off in open combat.
2. **Move Carefully** - Echofiends hunt sound. Coordinate with teammates silently when possible.
3. **Avoid the Glow** - Phosphor Beetle dye marks you as an easy target. Stay clean.
4. **Watch Your Feet** - Check overhead before walking through thick jungle (Canopy Stranglers).
5. **Team Up** - Coordinate extraction zone entry so multiple people arrive together.
6. **Medical Supplies** - You have limited morphine and bruise packs. Use them wisely.
7. **Ammunition** - You start with only 3 magazines total. Make your shots count.

---

## Winning Strategy

1. Coordinate a team push toward the extraction zone after grace period ends
2. Cover fire and watch for creatures while team members enter the zone
3. Keep 30+ seconds of continuous presence without leaving the zone
4. Escape successfully. Celebration optional but recommended
