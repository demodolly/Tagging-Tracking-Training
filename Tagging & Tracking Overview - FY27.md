# Tagging & Tracking Overview — FY27

**Editable outline** for `Tagging & Tracking Overview - FY27.pptx`.  
The PowerPoint uses the Cisco template (layouts, graphics, module deep dives). Run `python3 update_fy27_overview_deck.py` to apply narrative fixes from this file to the deck.

**Source of truth for current-state URL rules:** `UTM Framework New Training.md`

---

## Slide 1: Tagging & Tracking Overview

- Subtitle: Which IDs to use, where they go, and why — during the FY27 hybrid transition
- GTM Readiness & Performance Teams · June 2026

---

## Slide 4: Current State — Hybrid Rules

We are in a hybrid tracking model. Legacy CTT IDs and standardized UTMs work together until Workfront Channel IDs fully replace CCID in analytics.

**On every external URL that drives traffic to Cisco.com, you MUST include today:**

| Parameter | Source today | Purpose |
|---|---|---|
| ccid | Activity ID | Campaign / initiative in system of record |
| dtid | Drive To ID | Legacy channel + vehicle classification |
| utm_id | Same value as ccid | Analytics campaign key (future: Workfront Channel ID) |
| utm_medium | Workfront / approved builder | Channel classification — highest priority in analytics |
| utm_source | Workfront / approved builder | Platform or vendor within the channel |
| utm_creative | %ecid! macro | Only Paid Direct, Paid Programmatic, Paid Social |

Do not drop ccid or dtid until governance announces retirement.

---

## Slide 28: Dissecting the Hybrid URL Requirements

### TODAY — Required hybrid URL (FY27)

```text
https://www.cisco.com/.../index.html?ccid=cc010375
&dtid=pdixsp001642
&utm_id=cc010375
&utm_medium=paid-direct
&utm_source=businessinsider
&utm_creative=%ecid!
```

✅ utm_id matches ccid · all values lowercase · & separates parameters

### FUTURE — After Workfront Channel IDs (preview only)

```text
https://www.cisco.com/.../index.html?utm_id=CHL000093
&utm_medium=paid-direct
&utm_source=businessinsider
&utm_creative=%ecid!
```

⚠️ Do not use until governance confirms Channel ID in production URLs.

---

## Slide 31: Workfront Channel ID and utm_id

- **Today:** utm_id must equal ccid on every external URL.
- **Future:** Workfront Channel ID will replace ccid in utm_id once governance confirms go-live.

---

## Slide 34: When to Use your IDs

| Scenario | Put on the URL | Put elsewhere | Do NOT |
|---|---|---|---|
| External link to Cisco.com | ccid, dtid, utm_id, utm_medium, utm_source (+ utm_creative if paid) | Workfront Channel ID auto-mapped when live | Use Offer ID as a URL param |
| Internal Cisco.com CTA or page link | Nothing | — | Any CTT or UTM params |
| Gated offer landing page (AEM) | — | Offer ID + Content ID in page HTML / AEM metadata | Tag internal navigation with DTID |
| Manual upload (MUSE template) | — | CCID + DTID in template columns | UTM params (not a live URL) |
| Integrate / PathFactory / BrightTalk | Per integration spec | CCID, DTID, Offer ID in payload | Assume UTMs replace integration metadata |

**Rule of thumb:** Outside traffic → hybrid URL (let Workfront generate). Lead needs seller context → CTT on the record. Gated asset → Offer ID on the page. Project ID → internal only.

---

## Patches applied by update script

Slides updated in place (template preserved):

1. Subtitle — clearer FY27 framing
4. WE MUST hybrid parameter list
22. Event ID callout + CTT footer
23. “Adding UTMs, not replacing CTT overnight” callout
27. Workfront automation three-step flow
28. utm_id=cc010375 (matches ccid); today vs future labels
30. Workfront vs CTT scope note
31. Channel ID / utm_id today vs future wording
32. “Structure of a Channel ID” title fix
34. Scenario-based decision table (replaces checkmark matrix)

Original deck backed up to `Tagging & Tracking Overview - FY27.backup.pptx` on first run.
