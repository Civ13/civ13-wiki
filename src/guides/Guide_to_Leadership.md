# Leading a Squad

In [Team Combat](../gamemodes/Team_Combat.md) rounds, many factions are split into numbered squads, each with a squad leader, and some roles are officers, commanders or radio operators. This page explains the tools those roles get and how to use them. If you are a regular soldier, the first section is all you need.

Leadership commands appear in extra tabs at the top-right of your screen: **Officer** for officers, squad leaders and commanders, and **Scout** for scouts. You can also type a command's name into the command bar.

## Squads

When you join a faction that uses squads, the game tells you **"You have been assigned to Squad N!"** and names your squad leader. If no squad leader has joined yet, the first squad leader to join takes the first free squad.

| Command | Who gets it | What it does |
| --- | --- | --- |
| **Find Squad Leader** | Everyone in a squad | Tells you how many meters away your squad leader is, and in which direction. |
| **Squad Announcement** | Squad leaders | Sends a message to every member of your squad. One announcement per minute. |
| **Faction Announcement** | Officers and commanders | Sends a message to everyone on your side. |
| **Tactical Map** | Officers, commanders and squad leaders | Opens a live map of your side's positions and your officers' markers. See [Tactical map](#tactical-map). |

On maps set in the twentieth century before the modern era, officers and squad leaders also spawn with a backpack radio. See [Communications](Guide_to_Communications.md) for using radios.

## Leading as a squad leader

1. **Announce a plan early.** One short Squad Announcement before the grace period ends ("Squad 2, follow me to the north trench") keeps people together.
2. **Keep the squad together.** Your soldiers can find you with Find Squad Leader, so move with purpose and avoid running off alone.
3. **Assign jobs.** Name who carries ammunition, who covers the flanks and who helps casualties.
4. **Update the plan.** When the situation changes, announce it. Announcements are limited to one a minute, so make each one count.
5. **Hand over if you must.** If you are badly wounded, tell your squad who is in charge until you return.

## Tactical map

Officers, commanders and squad leaders have **Tactical Map** in the **Officer** tab. It opens a map of the level you are standing on, with north at the top, and keeps it up to date every 2 seconds while the window is open.

![The tactical map as an officer sees it, with four soldiers and four markers](../images/civ13-tactical-map.png)

- **Squares** show the living members of your own side on that level: white is you, gold are officers and commanders, blue are squad leaders (with their squad number), green are other soldiers and grey are soldiers who are down. The other side never appears.
- **Circles** are markers your officers have placed: **A** Attack, **D** Defend, **R** Rally point, **!** Danger and **O** Objective.
- The faint grid lines are 20 tiles apart, which helps when you pass coordinates by radio.

Officers and commanders can draw on the map. Pick a marker from the buttons above the map, then click where it goes. **Erase** removes the marker nearest your click (within a few tiles), and **Clear all** removes every marker. Your side keeps up to 24 markers on each level; placing another removes the oldest. Other officers and squad leaders on that level are told in chat when a marker is placed or the map is cleared, and anyone with the map open sees the change at once. Squad leaders can read the map but not draw on it.

The map closes if you are knocked out or die. If you change level, it switches to the new level.

## Officers, scouts and coordinates

Officers use **Check Coordinates** and **Reset Coordinates** from the **Officer** tab. Scouts have the same commands in the **Scout** tab. Both can report positions for artillery and air support.

1. Stand at a known location and use **Check Coordinates**. This starts tracking from where you stand.
2. While tracking, click a distant tile to learn its coordinates and offset from you. Each tile you check is reported to your side.
3. Use **Check Coordinates** again to finish at your current position, which also reports it.
4. Use **Reset Coordinates** to stop tracking.

Every reported position lets your side request support within **15 tiles** of it. These commands only work once the teams are allowed to cross the starting barriers.

## Radio operators and air support

On maps that include artillery or air support, radio operators get **Order Airstrike**:

- You need a working radio within one tile of you, either carried or a radio set.
- The target must be within 15 tiles of a position an officer or scout has reported. Otherwise the request is refused.
- Requests are refused if any of your living teammates are within 7 tiles of the target.
- Each map has a limited number of strikes and a cooldown between them. The game tells you how many minutes remain.

Choose the strike type when prompted, then enter the X and Y coordinates. The strike arrives after a short delay, so warn your teammates.

## Artillery pieces

Field guns and artillery pieces are operated directly, not ordered by radio. See [How to use artillery](Guide_to_Weapons.md#how-to-use-artillery).
