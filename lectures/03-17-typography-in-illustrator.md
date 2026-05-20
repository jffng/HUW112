---
layout: default
title: "Typography in Illustrator"
---

# Typography in Illustrator

*March 17, 2026* · [← All lectures](index.html)

- ****Demo the typography controls****
- ****Area type vs point type****
- - ****Point type**** is created by clicking once on the canvas. The text box expands infinitely as you type — there's no boundary, so it never wraps. You can't "resize" it in a meaningful way because it isn't really a box; it's just a line of text anchored to a point. Dragging a corner handle scales the text itself (changes the font size), it doesn't reflow it.
    - ****Area type**** is created by clicking and dragging to draw a box before you type. This is a true text frame with fixed boundaries — text wraps inside it and overflows (shown by a small red + symbol) if there's more text than space. This is the one you can freely resize.To resize an area type box:
        
        - - Select it with the Selection tool (V), then drag any of the 8 handles around the frame. The text reflows to fit the new dimensions — the font size doesn't change.
            - For precise dimensions, type exact values in the W and H fields in the control bar at the top.
            - You can also double-click any handle to auto-fit the box to exactly contain the text with no overflow — useful for tidying up.
        
        ****Converting between the two**** is something you'll want to know. If you accidentally created Point type but needed Area type, go to Type → Convert to Area Type (and vice versa with Type → Convert to Point Type). This is a common source of confusion when text unexpectedly scales instead of reflows on resize.One more thing worth knowing: if you hold `Cmd/Ctrl` while dragging a corner handle on an Area type box, it scales the text content proportionally rather than reflowing it — so you can use that to scale everything up or down together when needed.
