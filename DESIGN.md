<!-- SEED: established with the user before implementation; re-run /impeccable document once there's code to capture the actual tokens and components. -->

# Design System: Cortinas Sergio

## Overview

**Creative North Star: "The Textile Atelier"**

Cortinas Sergio's visual language is rooted in the warmth of Colombian craftsmanship and the precision of architectural design. The system pairs the richness of deep emerald and gold with the airy lightness of ivory, creating spaces that feel both luxurious and approachable. Full-bleed photography carries the proof — real installations, real textures, real results. Typography is generous and editorial, built for an older audience that values clarity and elegance.

**Key Characteristics:**
- Minimalist but warm — never cold or sterile
- Photography-led; imagery carries the narrative, chrome does not
- Generous scale and whitespace for legibility
- Gold accents as deliberate punctuation, never as surface decoration
- Architectural structure with soft, natural materiality

## Colors

The palette draws from Colombia's natural and architectural heritage: emerald from the coffee region, gold from colonial altarpieces, ivory from traditional hacienda walls.

### Primary
- **Deep Emerald** (#1F6A3A): The structural brand color. Used for the header background, dark section backgrounds, and as the dominant field color. It conveys quality, trust, and natural richness.
- **Forest Green** (#184C32): A deeper, more introspective variant for footer backgrounds and the hero overlay gradient. Adds depth without competing with the primary.

### Accent
- **Satin Gold** (#B8923E): The accent voice. Used for phone CTAs, the hero tag label, section label text, hover states, and the scroll indicator. Applied sparingly — its rarity is the point. Never used as a background fill for large areas.

### Neutral
- **Ivory** (#F7F5F0): The page background and canvas. Warm, timeless, never clinical white. Used as the default section background.
- **Linen Beige** (#E8E0D2): Secondary neutral for alternation (the gallery section background). One step warmer than Ivory.
- **Graphite** (#2F3133): Primary text color. High-contrast against Ivory, slightly softened from pure black for readability.
- **Stone Gray** (#B8B8B4): Subtle borders, dividers, and secondary text elements.

### Supporting
- **Sage Green** (#A8B69C): Reserved for potential future supporting roles (badges, tags, decorative elements). Not yet deployed in the initial build.

**The Gold Touch Rule.** Satin Gold covers less than 5% of any viewport. It exists to draw the eye to the action — the phone call — and to signal quality without shouting.

## Typography

**Display Font:** Playfair Display (serif), with Georgia and Times New Roman as fallback.
**Body Font:** DM Sans (sans-serif), with system-ui and Arial as fallback.

**Character:** Playfair Display brings editorial gravitas — the voice of a design magazine, not a shopping catalog. DM Sans provides exceptional legibility for older readers, with open counters and generous x-height. The pairing bridges timeless elegance with modern clarity.

### Hierarchy
- **Display** (Playfair Display 600, clamp 2.5rem–4.5rem, line-height 1.1, letter-spacing -0.02em): Hero headline only. One use per page.
- **Headline** (Playfair Display 600, clamp 2rem–3rem, line-height 1.15, letter-spacing -0.02em): Section titles.
- **Title** (Playfair Display 600, 1.35rem, line-height 1.3): Service card headings and other sub-section titles.
- **Body** (DM Sans 400, 1.125rem, line-height 1.6–1.7, max-width 640px/65–75ch): All running text. Minimum 18px in-body ensures readability for the primary audience.
- **Label** (DM Sans 500, 0.8rem, letter-spacing 0.1em, uppercase): Section labels, tag badges, small metadata.

**The One Headline Rule.** Every viewport has exactly one headline in Display size. A second headline in the same viewport must be one step down in the hierarchy.

## Layout

A single-column spine on mobile, expanding to a multi-column editorial grid on tablet and desktop. The container maxes at 1200px with 1.5rem gutters. Sections alternate between full-width (hero, dark CTA) and contained (about, services, gallery, showroom) to create rhythm.

On desktop, alternating sections use a 2-column split (about, showroom) at a 4rem gap. The gallery uses a 3-column grid that collapses to 2 on tablet and 2 on mobile. Services stack in 3 columns on desktop, 2 on tablet, 1 on mobile.

**The Section Rhythm Rule.** A contained section after a full-bleed section, and vice versa. No two full-bleed sections in a row.

## Elevation & Depth

The system is fundamentally flat. Depth is created through:
- **Tonal layering**: dark backgrounds (Forest Green, Deep Emerald) against light ones (Ivory, Linen Beige).
- **Photographic depth**: full-bleed imagery with gradient overlays creates atmosphere without artificial shadows.
- **The scrolled header** receives a subtle neutral shadow (0 2px 16px rgba(0,0,0,0.08)) — the only shadow in the system. It signals that the header is above the page content.

## Shapes

- **Buttons and CTAs**: Fully rounded (100px / pill shape). The pill communicates approachability and a human touch.
- **Cards**: 16px border-radius for service cards (backdrop-filter cards on dark backgrounds). 12px for informational cards.
- **Gallery images**: 8px radius — enough to soften without competing with the photography.
- **Header logo**: 2px radius — subtle, minimal.

**The Soft Edge Rule.** Every corner has a radius, but the radius shrinks as the element's information density increases. Pill buttons (most important action) > section cards > gallery thumbnails (least radius).

## Components

### Buttons
- **Shape:** Pill (100px border-radius).
- **Primary (Gold CTA):** Satin Gold (#B8923E) background, white text, font-weight 600, 1rem-1.125rem, padding 1rem 2rem, min-height 3.5rem. Hover: darken to #a07e2e with -1px translateY. Transition: 0.25s background, 0.15s transform.
- **Outline (Ghost):** Transparent background, white text, 2px solid border at 30% white opacity. Hover: gold border (#B8923E) with 10% gold background.
- **Phone (White CTA in dark sections):** White background, Deep Emerald (#1F6A3A) text, 1.5rem font-size, pill shape. Hover: translateY(-2px) with elevated shadow.

### Navigation (Header)
- **Style:** Fixed top, transparent at rest. Transitions to solid Deep Emerald (#1F6A3A) with neutral shadow on scroll past 80px.
- **Logo:** Left-aligned, 2.5rem height, with brand name in Playfair Display 600 (hidden on mobile <640px).
- **Phone CTA:** Right-aligned, gold-outlined pill button. Always visible, always tappable.

### Service Cards
- **Background:** `rgba(255,255,255,0.06)` with `backdrop-filter: blur(4px)` on the dark Emerald section.
- **Shape:** 16px border-radius.
- **Icon:** Gold-icon in a 3.5rem circle with 20% gold background.
- **Hover:** Background lightens to 10% white, card lifts 4px.

### Gallery Grid
- **3 columns** on desktop, 2 on tablet/mobile.
- Images at 4:3 ratio with one 4:5 tall image per row for rhythm.
- 8px border-radius. Hover: subtle 1.03x scale with 0.4s ease.

## Do's and Don'ts

### Do:
- **Do** let photography carry the proof. A room photograph is worth more than any headline.
- **Do** use Satin Gold sparingly — on CTAs, section labels, and the scroll indicator. Its rarity is its power.
- **Do** use generous whitespace, especially above headings. The audience needs visual breathing room.
- **Do** make the phone number the most prominent interactive element on every viewport.
- **Do** use the editorial typography scale: one bold headline per section, then step down.

### Don't:
- **Don't** use gradients on text. Emphasis comes from weight or size.
- **Don't** use glass or blur effects as decoration. The service cards' backdrop-filter is functional — it creates depth on a dark field.
- **Don't** use colored border-left/right lines on cards or callouts.
- **Don't** use cards as the default page structure. Cards are for the service section only; the rest of the page uses editorial layout.
- **Don't** use section numbers (01, 02, 03) or tracked uppercase eyebrows over every section.
- **Don't** use monospace fonts — the audience and context have no need for code or technical typography.
