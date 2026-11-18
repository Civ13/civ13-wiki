# Integrated Circuits

An **integrated circuit** is a small programmable board. Inside it you place components such as adders, comparisons and text tools, and wire them together in a node editor. The **compact remote** is a handheld button with its own circuit built in. Pressing it sends a signal through whatever you have wired up.

## Getting one

- Research **Digital Computing** on your faction's [tech tree](Guide_to_Research.md).
- Craft an **integrated circuit** from 4 electronics, or a **compact remote** from 5 electronics. Both are in the electronics section of the crafting menu. Electronic circuits are made from copper; see [Crafting](Guide_to_Crafting.md).

## The editor

Use an integrated circuit in your hand to open its editor. For a compact remote, Alt-click it. You must be holding it, or standing next to it while it lies on the ground.

- **Add a component:** open the component menu and drag a component onto the board. Components are made in the editor and cost nothing extra. A circuit holds up to 64 of them.
- **Wire it up:** drag from an output (on the right of a component) to an input (on the left of another). An input takes one wire, while an output can feed many inputs. Right-click a port to remove its wires.
- **Set a value:** type into an input that has no wire. Inputs with a fixed set of choices, such as an arithmetic operation, show a dropdown instead.
- **Fire by hand:** click a signal input to send it a signal straight away.
- **Variables:** the variable menu makes named values of a chosen type (up to 32 per circuit). Getter nodes read a variable and setter nodes write it.
- **Rename:** you can give the circuit a display name.

Port types are colour-coded: numbers, text, lists, signals and "any". A wire only joins ports whose types fit.

## Components

| Category | Component | What it does |
| --- | --- | --- |
| Math | Arithmetic | Add, subtract, multiply, divide, modulo, power, minimum or maximum of A and B. |
| Math | Comparison | Equal, not equal, greater or less than (or equal). Outputs true or false. |
| Math | Logic | AND, OR or XOR of two values. |
| Math | Random | A random whole number between two bounds. |
| Math | Length | The length of a piece of text or a list. |
| String | String Concat | Joins two pieces of text. |
| String | String Contains | Whether one piece of text contains another. |
| String | String Replace | Replaces every match in a piece of text. |
| String | String Split | Splits text at a separator (a comma by default) into a list. |
| String | String Case | Converts text to upper or lower case. |
| String | String to Number | Reads a number out of text. |
| List | List Add | Adds a value to the end of a list. |
| List | List Remove | Removes a value from a list. |
| List | List Concat | Joins two lists. |
| List | List Index | The value at a position in a list, counting from 1. |
| Utility | Delay | Waits 1 to 600 seconds after its trigger, then sends a signal. A new trigger restarts the wait. |

Most components work out their output as soon as an input changes.

## The compact remote

Use the remote in your hand to press it. Its built-in component has two outputs:

- **Signal**, sent each time it is pressed.
- **User**, the visible name of whoever pressed it.

For example, you can wire Signal into a Delay, then the Delay into a List Add that keeps a list of who pressed the button.

## Limits

- Text on a wire is cut off at 5,000 characters, and lists hold up to 500 entries.
- A circuit that feeds back into itself, for example two components triggering each other forever, **overloads**. It goes quiet for about five seconds and warns whoever is holding it.
- Circuits do not carry objects or people along their wires, only numbers, text and lists.
- Circuits are not kept when the world is saved. Note down any design you want to keep.
