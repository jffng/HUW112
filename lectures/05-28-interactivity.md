---
layout: default
title: "Interactivity"
---

# Interactivity

*May 28, 2026* · [← All lectures](index.html)

# SVG, Animation, and a Little JavaScript

_HUW 112 · Unit 4: Web_

You already wrote your first interaction last class:
`.learn-more:hover`? 

Move the mouse over it, the background and padding change. 

1. drawing with SVG
2. CSS animating
3. javascript

A useful way to hold the three languages of the web apart:

- **HTML** is the structure — _what's on the page._
- **CSS** is the look — _how it appears._
- **JavaScript** is the behavior — _what happens when someone clicks, types, or waits._

## A small change to what you already have

Add one line to `.learn-more`:

```css
.learn-more {
  /* ...everything you had before... */
  transition: all 0.3s;
}
```

Reload. Hover. The change now _eases_ instead of snapping. That's a **transition** — it tells CSS to animate any property change over a duration. Same hover code as before; it just feels deliberate now.

→ MDN: [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/transition)

## SVG — drawing with shapes you can type

The logo in the Spectral Sound demo is an **SVG** — an image made of shapes written as markup, right inside your HTML:

```html
    <svg class="logo" viewBox="0 0 100 100" width="80" height="80" aria-label="Spinning record">
      <circle cx="50" cy="50" r="48" fill="#1d1d1d" stroke="#333333" stroke-width="1"/>
      <circle cx="50" cy="50" r="46" fill="none" stroke="#2a2a2a" stroke-width="1"/>
      <circle cx="50" cy="50" r="40" fill="none" stroke="#2a2a2a" stroke-width="1"/>
      <!-- a light reflection across the disc — breaks the symmetry so the spin is visible -->
      <rect x="20" y="48" width="60" height="4" fill="#3a3a3a"/>
      <circle cx="50" cy="50" r="18" fill="#ff5a36"/>
      <!-- a small mark on the label, off to one side, so you can see it go around -->
      <circle cx="50" cy="38" r="2.5" fill="#111111"/>
      <circle cx="50" cy="50" r="3"  fill="#111111"/>
    </svg>
```

You made SVGs in your assignment #2. Now you can see that it's just instructions: _draw a circle here, a circle there._ 

Because it's just shapes-as-text, you can edit and style it with CSS, and scale it to any size without it getting blurry.

A few shapes to know: `<circle>`, `<rect>` (rectangle), `<line>`, `<polygon>`, and `<text>`, `path` . Each takes attributes for position and size, plus `fill` (inside color) and `stroke` (outline color).

This connects back to **Unit 2**: the icons you made could _be_ SVGs — and because each shape is its own element, you can later make individual shapes clickable. That's the seed of a hand-built, link-driven navigation.

→ MDN: [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG) · [Basic shapes](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Basic_shapes)

However often times SVGs are messy when you export them from vector programs like Illustrator and Figma. You can clean them up / optimize them with tools like this: https://svgomg.net/

## CSS animation — beyond hover

A **transition** animates a single change. **`@keyframes`** lets you define a sequence of states and run them in a loop.

```css
@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

.logo:hover {
  animation: spin 2s linear infinite;
}
```

Same `:hover` you already know — only now we _run_ an animation instead of changing one property. The record spins continuously while hovered, rests otherwise.

**Heads up — an SVG gotcha:** by default an SVG rotates around the page's corner, not its own center. Fix it by telling the shape to spin around itself:

```css
.logo {
  transform-box: fill-box;
  transform-origin: center;
}
```

→ MDN: [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations) · [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/@keyframes) · [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/transform)

## JavaScript — making the page respond

CSS reacts to hovering. **JavaScript** reacts to anything: clicks, typing, time passing. Here's the smallest useful pattern, three steps.

```html
<button id="lights-button">Dark mode</button>
```

```html
<script>
  // 1. FIND an element on the page (by its id)
  const button = document.getElementById("lights-button");

  // 2. LISTEN for an event on it (here: a click)
  button.addEventListener("click", function () {
    // 3. CHANGE something when it happens
    document.body.classList.toggle("lights-on");
  });
</script>
```

1. **Find** the element — `getElementById` grabs the thing with `id="lights-button"`.
2. **Listen** — `addEventListener("click", ...)` runs your code every time it's clicked.
3. **Change** — here we add or remove the class `lights-on` on the page.

The key realization — **JavaScript just flips switch** — adding / removing one CSS classs. The _actual_ visual change lives in CSS:

```css
body.lights-on {
  background-color: #111111;
  color: #eeeeee;
}
```

So JS decides _when_, CSS decides _what it looks like._ Keeping that division clean is how you make interactive things without writing much JavaScript. Your `<script>` goes near the bottom of the page, just before `</body>`, so the elements exist before the code goes looking for them.

→ MDN: [`getElementById`](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById) · [`addEventListener`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) · [`classList`](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList) · [Intro to events](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events)

## A bigger idea worth sitting with

A web page is not a frozen document. It's a **running program** in your browser. It can change depending on _when_ you visit, _what_ you click, _where_ you are. The page you load at midnight can look different from the page at noon. That's what people mean when they say the web is _dynamic_ — and it's what separates a website from a printed poster.

## Try this

Drop **one** of these into your own site:

- A shape (SVG) in your header that spins or grows on hover.
- A button that toggles your page between a dark and a light theme.
- Any element that changes color or appears/disappears on a click.

One small interactive moment makes a site feel alive. You don't need many.

## A note on AI tools

Yon can ask ChatGPT or Claude to "make me a site dedicated to X." 

Don't, for this assignment. The point of typing it yourself isn't to be old-fashioned — it's that what you can _type_, you can _change_. What an AI writes for you, you can't change with any confidence, because you don't know what it did. 

After this class? Use whatever you want. For now: your hands, your code, your site.

---

**Assignment #4** is due **June 2.** Layout from last class is the requirement; today's SVG, animation, and interaction are how you make it _yours_ — and a head start on the kind of thinking your final project will ask for.
