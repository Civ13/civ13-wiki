# Resource Extraction

Use underground mining for larger batches from finite deposits, or gather smaller trace batches without consuming terrain. Fossils come from finite deposits only. Check the map's crafting catalog, your skills and your faction's research before planning a machine chain.

## Manual trace gathering

On uncovered, non-mineable dirt or sand, choose **Crafting > Sift soil for resources**. Stay still for three minutes to obtain one random unit. **Basic Toolmaking** unlocks a wooden resource sieve costing **4 wood**; activate it in your active hand for a two-minute, one-unit batch.

Copper, tin, raw sand and stone are available first. Iron joins the soil pool at age 1; coal, saltpeter, sulphur and lead join at age 2. Trace gathering does not supply fossils.

For **Pan river sediment**, hold a wooden bowl in your active hand on eligible soil beside shallow freshwater. A two-minute action yields one random copper, tin, silver or gold ore. Bottled water, salt water and deep water do not qualify. Movement, incapacitation, changing the active hand or replacing the soil interrupts gathering; panning also needs the original water tile to remain valid.

## Powered gathering

**Electricity** unlocks the industrial drill, powered soil sifter and powered river concentrator. Each costs **20 electronics and 20 steel**, reserves **150 cable power**, and produces **2 random units every 2 minutes** while running.

| Machine | Placement | Output |
| --- | --- | --- |
| Industrial drill | Anchored on uncovered surface dirt at z=1 | Mineral pool |
| Powered soil sifter | Anchored on uncovered, non-mineable dirt or sand | Soil trace pool |
| Powered river concentrator | The same soil, beside shallow freshwater | Copper, tin, silver or gold ore |

Connect cable power and activate the machine. Every restart waits a full interval. Loss of power, invalid terrain or anchoring, or blocked output stops extraction. The concentrator also stops if its water tile is replaced or no longer qualifies.

Output fills matching stacks up to their limits. A tile holds at most **12 output stacks**; room in existing matching stacks remains usable at that limit. Clear output when the machine cannot place another batch. Saving restores these machines stopped: reconnect and activate them to resume.

[Power & Batteries](Guide_to_Power.md) explains cable supplies. **Paved Infrastructure** provides plain white cable for the Electricity prototype; colored cable and electronics require Electricity. Electronics use copper and iron. Use [Metallurgy](Guide_to_Metallurgy.md) to establish molds, furnaces and metal production.

## Petroleum wells

Wooden oil wells remain renewable and must sit on an oil spring. Use a barrel on the well to load it; click a loaded well to remove the barrel, or an empty well to connect a nearby barrel. Extraction runs when the spring and contained barrel are valid. The well does not fill unrelated barrels on the ground. Unloading or destroying the well returns its barrel. Saving retains the barrel and petroleum; check the barrel connection after loading before collecting output.

## Hydraulic fracturing

At **Modern**, research **Hydraulic Fracturing**, which requires **Electricity** and **Modern Construction**. Craft the rig from **20 electronics and 20 steel**.

1. Anchor it beside an undepleted, mineable underground rock tile on the same level.
2. Connect a cable network with **300 available power**.
3. Load a barrel containing only freshwater, an empty or petroleum-only barrel with at least **50 units free**, and at least **5 raw sand**.
4. Activate the rig and allow the two-minute batch to complete.

Each successful batch consumes **20 water**, **5 sand** and **one rock tile**, producing **50 petroleum**. The rig stops after each batch; check supplies and the next target before restarting. Missing or contaminated inputs, removed inputs, replaced terrain, insufficient output capacity or lost power stop the batch without paying its inputs. **Unload Fracking Rig** stops it and returns contained inputs.

Depleted rock stays depleted through saves. Moving or rebuilding a rig does not renew that deposit. Saved rigs retain their contained inputs and restore stopped. **Combustion** unlocks the petroleum refinery; refine and use fuel accepted by the destination engine rather than assuming every petroleum mixture works in every engine.
