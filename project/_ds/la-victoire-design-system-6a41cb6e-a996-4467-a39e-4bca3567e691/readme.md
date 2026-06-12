# La Victoire — Design System

## Overview

**La Victoire** is a premium French-language brand operating across recruitment, education, and commercial communications. The name — "The Victory" — signals aspiration, excellence, and achievement. The brand identity centers on a regal gold crest featuring a crowned "V" monogram with shield and wing motifs, rendered in a textured gold-foil finish.

### Products & Surfaces
Based on provided materials, La Victoire applies across:
- **Recruitment posters** — talent acquisition campaigns
- **Educational certificates** — completion and achievement awards
- **Commercial presentations** — pitch decks, investor materials
- **Document systems** — letterheads, email signatures, headers
- **Social media** — avatars, cover images, story templates
- **Marketing website** — brand landing page, about, contact
- **Printed collateral** — brochures, event programs

### Source Materials
- `uploads/LOGO LA VICTOIRE .png` — Primary logo, 1080×1080 transparent PNG, gold crest on transparent background
- `uploads/Logo_La_Victoire_Asset.md` — Brand asset documentation with color codes and usage guidelines

---

## Content Fundamentals

### Tone & Voice
La Victoire communicates with **confident authority** and **refined elegance**. The brand voice is:
- **Aspirational** — language lifts the reader, implying excellence and achievement
- **Formal but warm** — professional without being cold; uses "vous" (formal French) register
- **Direct** — short, declarative statements; avoids filler and hedging
- **Bilingual-ready** — French is the primary language; English is used for international contexts

### Copywriting Rules
- **Casing**: Title Case for headings and labels; sentence case for body copy
- **Pronouns**: Address the audience as "you" (or "vous"); the brand speaks as "we" or in third person ("La Victoire")
- **No emoji** in formal communications — the brand relies on typography and gold accents for visual punctuation
- **Numbers**: Spell out one through nine; use numerals for 10+
- **Punctuation**: Em dashes (—) for emphasis; no exclamation marks in headers

### Example Copy
- Heading: "Excellence Is Not an Aspiration — It Is a Standard"
- Subheading: "Join a legacy of distinction"
- CTA: "Begin Your Journey"
- Certificate: "Awarded to [Name] in Recognition of Outstanding Achievement"

---

## Visual Foundations

### Color System
The palette is built on two pillars: **gold** (warmth, prestige, value) and **dark navy** (depth, trust, authority), supported by warm neutrals.

| Role | Token | Value |
|------|-------|-------|
| Primary Gold | `--gold-400` | `#d4af37` |
| Dark Navy | `--navy-600` | `#1a1a2e` |
| White | `--neutral-0` | `#ffffff` |
| Near-Black | `--neutral-950` | `#0d0c0b` |

- **Backgrounds**: Predominantly white (`--surface-primary`) or dark navy (`--surface-dark`). Never a mid-tone background — always high contrast.
- **Gold usage**: Accents, borders, key headings, CTAs, and decorative elements. Never as a large surface fill (except on certificates or awards).
- **Navy usage**: Hero sections, headers, footers, and dark-mode contexts.

### Typography
- **Display / Headings**: Playfair Display (serif) — elegant, high-contrast letterforms with sharp wedge serifs. Used for all headings, hero text, and ceremonial copy. ⚠️ *Substituted from Google Fonts; original brand may specify a different serif.*
- **Body / UI**: Montserrat (sans-serif) — clean, geometric, highly legible at small sizes. Used for paragraphs, labels, navigation, and form elements. ⚠️ *Substituted from Google Fonts.*
- **Heading tracking**: Wide (`0.05em` to `0.2em`) letter-spacing on uppercase display text creates a luxury feel.
- **Body tracking**: Normal to slightly tight.

### Spacing & Layout
- **Generous whitespace** — luxury brands breathe. Minimum `--space-8` (32px) between major sections; `--space-16` (64px) or more between hero areas.
- **Fixed layout zones**: Headers and footers are fixed/sticky on marketing pages.
- **Grid**: 12-column grid with 24px gutters on desktop; single-column on mobile with 20px side padding.
- **Alignment**: Left-aligned body text; centered headings in hero contexts.

### Backgrounds & Imagery
- **No gradients** as primary backgrounds — solid colors (navy, white, cream) maintain the refined look.
- **Gold-foil textures**: Used sparingly for decorative borders and the logo itself — not for backgrounds.
- **Photography style**: If imagery is used, it should be warm-toned, high-contrast, desaturated slightly. Portrait photography with shallow depth of field. Never cool or clinical.
- **No hand-drawn illustrations** — the brand is formal. Decorative elements are geometric or crest-derived.
- **No repeating patterns/textures** except subtle paper or linen textures on certificate backgrounds.

### Borders & Dividers
- **Borders**: 1px solid, `--border-default` (warm neutral) for containers. `--border-gold` for accent borders.
- **Dividers**: Thin gold lines (`1px solid var(--gold-300)`) for horizontal rules and section breaks.
- **Corner radii**: Minimal — `--radius-sm` (2px) to `--radius-md` (4px) for cards and inputs. Buttons use `--radius-md`. Never fully rounded except for avatars and badges.

### Shadows
- **Subtle and warm** — shadows use low opacity and slight warm tint, never harsh drop shadows.
- **Cards**: `--shadow-md` for resting state, `--shadow-lg` on hover.
- **Gold glow**: `--shadow-gold` for premium CTAs and highlighted elements.

### Animation & Transitions
- **Restrained** — transitions are smooth and brief. No bounces, no playful springs.
- **Easing**: `--ease-default` (ease-out) for most interactions.
- **Duration**: `--duration-normal` (200ms) for hover/focus states; `--duration-slow` (350ms) for reveals and page transitions.
- **Entrance animations**: Subtle fade-up (opacity 0→1, translateY 12px→0) for content blocks. No scale or rotate.
- **No infinite loops** or decorative animations.

### Hover & Press States
- **Hover**: Darken by one step in the color scale (e.g., `--gold-400` → `--gold-500`). No opacity change on hover.
- **Press/Active**: Darken by two steps (e.g., `--gold-400` → `--gold-600`).
- **Focus**: 2px gold outline with 2px offset (`outline: 2px solid var(--gold-400); outline-offset: 2px`).
- **Links**: Underline on hover; gold color for links on light backgrounds, light gold on dark backgrounds.

### Cards
- **Background**: `--surface-primary` (white)
- **Border**: `1px solid var(--border-default)` — no colored left-border accents
- **Radius**: `--radius-lg` (6px)
- **Shadow**: `--shadow-md` resting; `--shadow-lg` on hover
- **Padding**: `--space-6` (24px)

### Transparency & Blur
- Used minimally — only for overlay modals (`background: oklch(0% 0 0 / 0.6); backdrop-filter: blur(8px)`).
- No frosted-glass effects in normal UI.

---

## Iconography

### Approach
La Victoire uses a **minimal, refined** approach to iconography:
- **No emoji** — ever. The brand relies on typographic weight and gold accents.
- **No unicode symbols** as icons.
- **Icon style**: Thin stroke (1.5px), consistent with the elegant line-work of the crest. Lucide Icons (available via CDN) is the recommended set — it matches the brand's refined stroke weight.

### CDN Reference
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lucide-static@latest/font/lucide.min.css">
```
Or use individual SVGs from `https://unpkg.com/lucide-static@latest/icons/`.

### Usage Rules
- Icons are **always paired with labels** in navigation and forms — never icon-only (except close/dismiss actions).
- Icon size: 20px for inline/body, 24px for navigation, 32px for feature highlights.
- Icon color: Inherits text color; gold (`--text-gold`) for decorative feature icons.
- **No filled icons** — always outline/stroke style.

---

## Assets

| File | Description |
|------|-------------|
| `assets/logo-full.png` | Primary gold crest logo, 1080×1080 transparent PNG |

### Logo Usage
- **Minimum clear space**: 20px on all sides
- **On white backgrounds**: Use the gold logo as-is
- **On dark backgrounds**: Use the gold logo as-is (the gold reads well on navy/black)
- **Minimum display size**: 48px height for digital; 15mm for print
- **Never**: Stretch, rotate, recolor, or add effects to the logo

---

## File Index

### Tokens
| File | Contents |
|------|----------|
| `tokens/colors.css` | Gold, navy, neutral color scales + semantic aliases |
| `tokens/typography.css` | Font faces, families, sizes, weights, tracking, leading |
| `tokens/spacing.css` | Spacing scale, radii, shadows, transitions, z-index |

### Global Entry Point
| File | Contents |
|------|----------|
| `styles.css` | Root import file — link this to consume all tokens |

### Components
| Directory | Contents |
|-----------|----------|
| `components/core/` | Button, Badge, Card, Input, Select, Avatar, Divider |

### Guidelines (Foundation Cards)
| Directory | Contents |
|-----------|----------|
| `guidelines/` | Visual specimen cards for the Design System tab |

### Assets
| Directory | Contents |
|-----------|----------|
| `assets/` | Logo files, brand imagery |

### UI Kits
| Directory | Contents |
|-----------|----------|
| `ui_kits/website/` | Marketing website recreation |

---

## Quick Start

```html
<link rel="stylesheet" href="styles.css">
```

All tokens are available as CSS custom properties on `:root`. Use `var(--token-name)` in your styles.

```css
h1 {
  font-family: var(--font-display);
  color: var(--text-gold);
  letter-spacing: var(--tracking-wide);
}

body {
  font-family: var(--font-body);
  color: var(--text-primary);
  background: var(--surface-primary);
}

.btn-primary {
  background: var(--interactive-primary);
  color: var(--text-on-gold);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-gold);
}
```
