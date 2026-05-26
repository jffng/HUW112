---
layout: default
title: "Interactivity"
---

# Interactivity

*May 28, 2026* · [← All lectures](index.html)

# Making It Move & Making It Respond: SVG, Animation, and a Little JavaScript

_HUW 112 · Unit 4: Web_

Last class your pages learned to lay things out. Today they learn to **move** and **react**. Three new ingredients you can drop into your own site: drawing with SVG, animating with CSS, and a first taste of JavaScript so a page can _do_ something when you click.

A useful way to hold the three languages of the web apart:

- **HTML** is the structure — _what's on the page._
- **CSS** is the look — _how it appears._
- **JavaScript** is the behavior — _what happens when someone clicks, types, or waits._

## SVG — drawing with shapes you can type

An **SVG** is an image made of shapes written as markup, right inside your HTML. Instead of a photo made of pixels, it's instructions: _draw a circle here, a line there._ Because it's just shapes-as-text, you can edit it, style it with CSS, and scale it to any size without it getting blurry.

```html
<svg viewBox="0 0 100 100" width="80" height="80">
  <circle cx="50" cy="50" r="40" fill="#ff5a36" />
  <rect x="10" y="10" width="30" height="30" fill="black" />
  <line x1="0" y1="0" x2="100" y2="100" stroke="white" />
</svg>
```

A few shapes to know: `<circle>`, `<rect>` (rectangle), `<line>`, `<polygon>`, and `<text>`. Each takes attributes for position and size, plus `fill` (inside color) and `stroke` (outline color).

This connects back to **Unit 2**: the icons you made could _be_ SVGs — and because each shape is its own element, you can later make individual shapes clickable. That's the seed of a hand-built, link-driven navigation.

→ MDN: [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG) · [Basic shapes](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Basic_shapes)

## CSS animation — two ways to make things move

### 1. Transitions — ease a change instead of snapping

A **transition** says: "when this property changes, don't jump — glide." Pair it with `:hover` for the easiest win on the web.

```css
.cover {
  transition: background-color 0.3s;   /* glide color changes over 0.3 seconds */
}

.cover:hover {
  background-color: #ff5a36;            /* on hover, this change eases in */
}
```

→ MDN: [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/transition)

### 2. Keyframes — define a movement and run it

A **`@keyframes`** rule defines an animation as a start state and an end state. Then you _run_ it on an element with the `animation` property.

```css
@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

.logo:hover {
  animation: spin 2s linear infinite;   /* spin while hovered: 2s per turn, forever */
}
```

**Heads up — a common SVG gotcha:** by default an SVG rotates around the page's corner, not its own center, which looks broken. Fix it by telling the shape to spin around itself:

```css
.logo {
  transform-box: fill-box;
  transform-origin: center;
}
```

→ MDN: [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations) · [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/@keyframes) · [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/transform)

## JavaScript — making the page respond

CSS reacts to hovering. **JavaScript** reacts to anything: clicks, typing, time passing. Here's the smallest useful pattern, and it's only three steps.

```html
<button id="lights-button">Lights on</button>
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

The clever part: **JavaScript only flips a switch.** All it does is add or remove one class. The _actual_ visual change lives in CSS:

```css
body.lights-on {
  background-color: #f4f1ea;
  color: #1a1a1a;
}
```

So JS decides _when_, CSS decides _what it looks like._ Keeping that division clean is how you make interactive things without writing much JavaScript. Your `<script>` goes near the bottom of the page, just before `</body>`, so the elements exist before the code goes looking for them.

→ MDN: [`getElementById`](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById) · [`addEventListener`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) · [`classList`](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList) · [Intro to events](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events)

## The bigger idea

A web page is not a frozen document. It's a **running program** in your browser. It can change depending on _when_ you visit, _what_ you click, _where_ you are. The page you load at midnight can look different from the page at noon. That's what people mean when they say the web is _dynamic_ — and it's what separates a website from a printed poster.

## Try this

Drop **one** of these into your own site:

- A shape (SVG) in your header that spins or grows on hover.
- A button that toggles your page between a dark and a light theme.
- Any element that changes color or appears/disappears on a click.

One small interactive moment makes a site feel alive. You don't need many.

---

**Assignment #4** is due **June 2.** Layout from last class is the requirement; today's SVG, animation, and interaction are how you make it _yours_ — and a head start on the kind of thinking your final project will ask for.
