---
layout: default
title: "Poetic Web"
---

# Poetic Web

*May 21, 2026* · [← All lectures](index.html)

**Animation review + crit** Assignment #3 due. 

**Neal.fun**

- ARPANET map: https://neal.fun/internet-artifacts/arpanet-map/
- Internet Roadtrip: https://neal.fun/internet-roadtrip/

**What is the web, recap**

**Poetic Web** 
- are.na/chia/poetic-web 
- sadgrl.online


**Assignment #4**
	**Make a website about something you love.** A band, a video game, a movie, an animal, a person, a place, a food — anything you actually care about. It can also be a home for your work / posters.
	
	**It must contain:**
	- **Text** — write something real about it. 
	- **An image** — at least one.
	- **A video** — embedded or linked.
	- **A navigation** — more than one page, or clear sections you can jump to, with links that work.
	- **Some CSS styling** — make it yours. At minimum: change the fonts, the colors, and the layout (flexbox or grid). It should not look like a default HTML page.
	
	**It must be live** on your Neocities site by 6/2.

**CSS layout demo + studio

- Everything on a page is a box. Some boxes stack vertically by default (block — headings, paragraphs, divs). Some sit inline (text, links, images). CSS layout is mostly about taking control of how boxes sit next to each other. Draw this on the board with rectangles. Don't touch the keyboard yet.
- 
```css
* {
  box-sizing: border-box;
}
```
This makes padding and borders count _inside_ an element's width instead of adding to it, so things stop unexpectedly getting bigger than you told them to.

- **Three ways to target things in CSS**: 
	- by tag (`h1`)
	- by class (`.cover`)
	- by id (`#button` use sparingly). 
	- bread-and-butter properties on one box: `background-color`, `color`, `padding`, `margin`, `border`. Add the `box-sizing` line here and explain it once. Let them see padding push content inward and margin push boxes apart — the inside/outside distinction is the thing they need to feel.
- **Flexbox**
	- Use flexbox when you 
	- container div + child divs
	- `display: flex;`
	- `gap` for spacing between them
	-  `justify-content` (spacing along the row) and `align-items` (alignment across the row) — demo by changing values live and narrating what moves.
	- `flex-wrap: wrap;` so covers drop to the next line on small screens. This single example — a wrapping row of evenly spaced album covers — teaches 80% of what they'll use flex for.
- **Grid**
	- Use when you want rows AND columns
	- Example:
		- `display: grid;`
		- `grid-template-columns: repeat(3, 1fr);` — explain `fr` as "fraction of available space," and `repeat(3, ...)` as "three equal columns."
		- `gap` again


**Exercise**
