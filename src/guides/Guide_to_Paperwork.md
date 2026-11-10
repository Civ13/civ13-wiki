# Guide to Paperwork
Writing is an integral part to paperwork and writing books! If you want
to write an official department memo, or a good looking book, you're
gonna have to know how to write it.

To properly understand this, you need a basic grasp of BBCode or HTML.
This code is based on Bay12 code, so if you know it, it's going to be
easy. But don't worry, even if you don't know either, just try copy
pasting the examples and replacing the text with your own! Once you're
comfortable with that, try experimenting with what works together and
how.

## Writing

Writing is performed on paper using any standard writing utensil.

  - **Pens** come in a few different colours, black or blue by default,
    and some departments are provided with red pens. Pens have a variety
    of functions!
  - **Crayons** work much like pens, except that they are always bold,
    and lack the list, horizontal rule, and small tags.

### The paper editor

Writing on a paper with a pen or crayon opens the paper editor. Choose the **language** you write in at the top; only readers who know that language can understand it. Crayon writing is always bold and in a childlike hand.

The editor understands these tags:

| Tag | Effect |
| --- | --- |
| `[b]` ... `[/b]` | Bold |
| `[i]` ... `[/i]` | Italics |
| `[br]` | New line (pressing Enter also starts a new line) |
| `[sign]` | Your signature |
| `[date]` | Today's in-game date |
| `[time]` | The current in-game time |

`[sign]`, `[date]` and `[time]` are filled in once, when you write. Any other tag is shown as plain text. Papers written before the editor keep their old formatting when read, and you can keep writing on them.

The **Section** menu chooses what you write: body text, a written title, your signature, or a form blank.

### Blanks to fill in

Choose **Blank to fill in** and type a short name for it, such as `Name` or `Date of birth`. The paper then shows `Name: __________`.

Anyone with a pen can fill it in later. Choose **Fill in a blank**, pick the blank, and write the answer. It appears on the blank's line in your own ink and language. Each blank takes one answer, so it cannot be overwritten. This is handy for passes, permits and orders that someone else completes.

### Stamps and seals

Use an ink stamp or a wax seal on a paper to stamp it. The mark shows on the sheet and in the reader, and it stays when the world saves and when the paper is copied. A sheet holds up to 12 stamps, and a crumpled sheet can't be stamped. You can also stamp the top sheet of a clipboard, or the open page of a paper bundle.

### Envelopes, bundles and filing cabinets

You can write on a paper inside an open envelope you are holding, or on the open page of a paper bundle you are holding (also inside a folder you hold). Turn the page to write on another sheet. A sealed envelope keeps its wax seal through a save.

Filing cabinets and document drawers list their papers in alphabetical order. Use **Read** next to a paper to read it without taking it out.

### Classic editor

Some special papers, and characters who cannot write any language, still use the classic paper editor. It accepts the full set of tags below.

## Formatting Paper

### Signature

To sign your name, use the \[sign\] tag. Remember that **if you use the
\[sign\] tag, your signature is unique and cannot be forged in most
cases.**

    Your signature: [sign]

### Field

To insert a field from which you can start writing (instead of just
using the bottom of the paper), use the \[field\] tag.

    Reason for Request: [field]

### New Lines

New lines can be created by using the \[br\] tag. Without this, anything
you write will continue on the same line until it reaches the end of the
page.

    text above
    [br]
    text below

### Bold

To make text bold, enclose it within the \[b\] and \[/b\] tags.

    [b]This text is going to be bold.[/b] This text is not.

### Italics

To italicize text, enclose it within the \[i\] and \[/i\] tags.

    [i]This text is italicized.[/i] This text is not.

### Underlining

To underline text, enclose it within the \[u\] and \[/u\] tags.

    [u]This text is underlined.[/u] This text is not.

### Centering

To center text, enclose it with the \[center\] and \[/center\] tags.

`[center]Type the center tags onto the paper like this![/center]`

### Lists

Create a list by using the \[list\] and \[/list\] tags. For every entry
in your list, add a \[*\] in front of your entry. For example;

`[list][*]Bullet one.[*]Bullet two.[/list]`

### Large Text

Make text larger, enclose it within the \[large\] and \[/large\] tags.
Large text like this can be used for emphasis or for titles.

    [large]This text is much larger[/large] than this text.

### Small Text

To shrink text, enclose it with the \[small\] and \[/small\] tags.
Shrunken text can be used to fit more information onto your paper.

    [small]This text is very small![/small] This text is normal-sized.

### Horizontal rules

To add a horizontal rule, use the \[hr\] tag.

    text above
    [hr]
    text below

### First Heading

To make a first level heading, use the \[h1\] and \[/h1\] tags.

    [h1]insert desired text
    [br]
    closing text for heading[/h1]

### Second Heading

To make a second level heading, use the \[h2\] and \[/h2\] tags.

    [h2] insert desired text
    [br]
    closing text here[/h2]

### Third Heading

To make a third level heading, use the \[h3\] and \[/h3\] tags.

    [h3]insert desired text[/h3]

### Date

To insert the current date of the station, use the \[date\] tag.

    Date:[date]

### Time

To insert the current station time, use the \[time\] tag.

    Time Of Request: [field][time]
    [br]
    Reason for request: [field]
