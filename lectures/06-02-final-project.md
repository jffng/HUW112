---
layout: default
title: "Final Project"
---

# Final Project

*June 2, 2026* · [← All lectures](index.html)

_Due June 16_

---

## Assignment #4

The site built during Unit 4 — about something you love — completed to its full requirements.

**Requirements:**

- Text written by you about the subject
- At least one image
- A video, embedded or linked
- A working navigation — more than one page, or clear linked sections
- CSS styling that makes it distinct — fonts, colors, and a flex or grid layout

---

## Semester Recap

- Typography/poster → __how do text and images create meaning?__
- Reading → __what does it mean for an image to feel "real" or "true"?__
- Icons → __how do you compress an idea into its simplest visual form?__
- GIFS + Animation → __what does time add to an image that a still can't do? how do you sequence meaning across time?__
- Web → __what happens when you connect everyone simultaneously?__

## Final Project — Portfolio Project

A webpage housing all four assignments from this semester, plus **one new work** about a topic of your choosing:

- static poster
- SVG graphic
- gif
- animation

**Portfolio Requirements:**
- Your name
- A short statement — who you are, what you're interested in, what kind of work you want to make. 100 words minimum.
- All **five** works present: poster, icons + gif, animation, link to fan page, and  
- Some basic styling: fonts, colors, and layout applied throughout
- BONUS: create a moodboard that visualizes your process, inspiration, and artistic references.

**Where it lives:** A root (`/`) of your Neocities site or a dedicated page (`/portfolio.html`) on your existing one. It must be live and shareable by June 16.

## Schedule

- **June 4** — Work time, individual check-ins.
- **June 9** — Studio, bring both deliverables for feedback.
- **June 11** — Final polish.
- **June 16** — Presentations. Everyone presents (~3 minutes each).

---

## Grading Policy Reminder


Letter grades are determined by a combination of your work and participation in class:

40% assignments
30% final project and portfolio
30% participation (includes attendance)

Assignments are evaluated according to effort, completeness, and creativity you put in.
  
****Final grade examples:****

A — Completes every assignment and final project with great effort and creative enthusiasm. Active and consistent participant during class time.

B — Assignments completed with few late submissions, and the required effort. You are attendant and participate in class discussions and work.

C — Frequent late work. Assignments are submitted but show inconsistent effort. Participation is limited.

D — Significant missing or late work. Incomplete participation, or inconsistent and / or disruptive effort.

F — Failure to submit required work, attendance and participation are non-existent or extremely disruptive.

Late work is always accepted.

- 1 class late — one grade down A→B
- 2 classes late — two grades down A→C
- 3 classes late - D

Participation grade is separate.

---

## DEMO

Adding a background image: 

```css
/* 1. basic background image */
.add-some-waves {
  background-image: url("https://images.unsplash.com/photo-1505118380757-91f5f5632de0");
  height: 300px;
}

/* 2. sized and positioned properly */
.add-some-waves-properly {
  background-image: url("https://images.unsplash.com/photo-1505118380757-91f5f5632de0");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  height: 300px;
}

/* 3. shorthand */
.add-some-waves-same-but-short {
  background: url("https://images.unsplash.com/photo-1505118380757-91f5f5632de0") center / cover no-repeat;
  height: 300px;
}
```


MDN Reference: 
https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image
