# Tagging & Tracking Overview — FY27 Editorial Guide

**Purpose of this document:** Review findings and a recommended rewrite structure for `Tagging & Tracking Overview - FY27.pptx`. Use this as the narrative blueprint while you finish placeholder slides and tables.

**Audience:** Campaign marketers, channel owners, and ops teams who need to know *which IDs to use, where they go, and why* — not just what each ID is called.

---

## Executive summary: what is broken today

The deck has strong *module* content (Activity ID deep dives, reporting screenshots, Workfront value props) but the **decision story is missing**. A learner finishes Module 5 still unsure how CTT IDs, UTMs, and Workfront IDs relate — and Slide 34’s matrix mixes all three without explaining the columns.

### Top inconsistencies to fix

| Issue | Where it shows up | Why it confuses learners |
|---|---|---|
| **`utm_id` rules conflict** | Slide 28 shows `ccid=cc010375` but `utm_id=CHL000093`; Slide 31 says Channel ID *must* go in `utm_id`; `UTM Framework New Training.md` says **`utm_id` must equal `ccid` today** | Users do not know whether to copy CCID or Channel ID into `utm_id` on links they build this quarter |
| **Three ID families, no hierarchy** | Modules 2–3 (CTT), Module 4 (UTM), Module 5 (Workfront) taught separately | Users treat Project ID, CCID, and Channel ID as interchangeable “campaign IDs” |
| **Current vs future state blended** | Slide 23 (“legacy not enough”) sits *after* deep CTT training; Slide 28 URL looks future-state; hybrid rules on Slide 4 are empty | Users cannot tell what is required **now** vs what is **coming** |
| **Placeholder slides break the arc** | Slides 3, 4, 6, 7, 26, 27 are titles only | The “why hybrid” and “ID type overview” story never lands before the deep dives |
| **Decision matrix is unreadable** | Slide 34: column `ID` is undefined; `?` cells; mixes URL params with CTT IDs and Workfront IDs | This should be the capstone slide; today it creates more questions than answers |

---

## The story learners need (one sentence)

> **Every activation answers three questions — *what initiative*, *how traffic arrives*, *what asset was consumed* — and during FY27 you tag those answers in two parallel systems (CTT for lead & pipeline context, UTM for digital analytics) until Workfront Channel IDs replace CCID in `utm_id`.**

Build the entire deck around that sentence.

---

## Recommended narrative arc (6 acts, 34 slides)

Keep your existing module breaks where they work; **reorder ideas within modules** and **fill placeholders** as below.

### Act 1 — Frame the problem (Slides 1–6) ✅ mostly done, needs content

| Slide | Keep / change | Recommended content |
|---|---|---|
| 1 Title | Keep | Subtitle: *“Which IDs to use, where they go, and why — during the FY27 hybrid transition”* |
| 2 Module 1 divider | Keep | |
| **3 Document Objectives** | **Fill** | See [Slide 3 copy](#slide-3-document-objectives) |
| **4 Current State** | **Fill** | See [Slide 4 copy](#slide-4-current-state-hybrid-rules) |
| 5 Strategic value | Keep (trim bullets if needed) | Already strong — ties tagging to pipeline, nurture, sellers |
| **6 Hybrid landscape** | **Fill** | See [Slide 6 diagram](#slide-6-navigating-the-hybrid-landscape) |

### Act 2 — Teach the three business questions (Slides 7–22) ✅ strong content, small tweaks

| Slide | Keep / change | Recommended content |
|---|---|---|
| **7 CTT ID types table** | **Fill table** | See [CTT ID table](#slide-7-campaign-tagging--tracking-id-types) |
| 8–15 Activity ID module | Keep | Consider renaming “Activity ID” to **“Activity ID (CCID)”** on first mention in Slide 9 |
| 16–21 Drive To & Offer | Keep | |
| **22 ID Relationships** | **Enhance** | Add fourth row: **Event ID (EID)** — *when / where the interaction happened*; add footer: *“These four IDs power lead records, nurture, and pipeline — not Adobe channel reports.”* |

### Act 3 — Explain why UTMs exist (Slides 23–27)

| Slide | Keep / change | Recommended content |
|---|---|---|
| 23 Why legacy not enough | **Move earlier** *or* add callout: *“This is why we are adding UTMs — not replacing CTT overnight.”* |
| 24 Module 4 divider | Keep | |
| 25 UTM strategic value | Keep | |
| **26 UTM parameter table** | **Fill table** | See [UTM table](#slide-26-utm-tracking-id-types) |
| **27 Workfront automation** | **Fill** | See [Slide 27 copy](#slide-27-empowering-the-automation-engine-via-workfront) |

### Act 4 — Show the URL (Slides 28) ⚠️ critical fix

| Slide | Keep / change | Recommended content |
|---|---|---|
| **28 Hybrid URL** | **Split into two examples** | See [Slide 28 fix](#slide-28-dissecting-the-hybrid-url-requirements) |

### Act 5 — Introduce Workfront ID taxonomy (Slides 29–32) ✅ good, clarify scope

| Slide | Keep / change | Recommended content |
|---|---|---|
| 29–30 Workfront value | Keep | Add one line: *“Workfront IDs govern intake and automation; CTT IDs still populate lead context until retirement.”* |
| 31 Workfront ID types | Keep | Fix typo: “Structure of **a** Channel ID”; fix truncated bracket on Channel ID bullet |
| 32 Channel ID structure | Keep | |

### Act 6 — Decision guide (Slides 33–34) ⚠️ rewrite

| Slide | Keep / change | Recommended content |
|---|---|---|
| 33 Module 6 divider | Keep | |
| **34 When to use your IDs** | **Replace matrix** | See [Slide 34 decision guide](#slide-34-when-to-use-your-ids-replacement) |

---

## Slide copy to paste

### Slide 3: Document Objectives

**By the end of this training, you will be able to:**

1. **Name the three business questions** every activation must answer (initiative, traffic path, consumed asset).
2. **Choose the correct ID family** — CTT, UTM, or Workfront — for a given touchpoint.
3. **Build or validate a hybrid tracking URL** with the parameters required in FY27.
4. **Know what not to tag** (internal Cisco.com CTAs, wrong placements for Offer ID).
5. **Escalate** when a required source, medium, or mapping does not exist — instead of inventing values.

---

### Slide 4: Current State — Hybrid Rules

**We are in a hybrid tracking model.** Legacy CTT IDs and standardized UTMs work together until Workfront Channel IDs fully replace CCID in analytics.

**On every external URL that drives traffic to Cisco.com, you MUST include today:**

| Parameter | Source today | Purpose |
|---|---|---|
| `ccid` | Activity ID | Campaign / initiative in system of record |
| `dtid` | Drive To ID | Legacy channel + vehicle classification |
| `utm_id` | **Same value as `ccid`** | Analytics campaign key *(future: Workfront Channel ID)* |
| `utm_medium` | Workfront / approved builder | Channel classification — **highest priority in analytics** |
| `utm_source` | Workfront / approved builder | Platform or vendor within the channel |
| `utm_creative` | `%ecid!` macro | **Only** Paid Direct, Paid Programmatic, Paid Social |

**Do not drop `ccid` or `dtid` until governance announces retirement.**

---

### Slide 6: Navigating the Hybrid Landscape

Use a simple two-lane diagram:

```
┌─────────────────────────────┐     ┌─────────────────────────────┐
│  CTT IDs (lead & pipeline)  │     │  UTM params (web analytics) │
├─────────────────────────────┤     ├─────────────────────────────┤
│ Activity ID (CCID)          │     │ utm_id  (= ccid today)      │
│ Drive To ID (DTID)          │     │ utm_medium                  │
│ Offer ID → gated page HTML  │     │ utm_source                  │
│ Event ID → integrations     │     │ utm_creative (paid only)    │
└─────────────────────────────┘     └─────────────────────────────┘
              │                                    │
              └────────── on same URL ───────────┘
                    (external traffic only)
```

**Workfront sits above both:** Project ID (internal) → Channel ID (future `utm_id`) → Content ID (AEM gated pages).

---

### Slide 7: Campaign Tagging & Tracking ID Types

| ID | What it answers | Where it lives | Key rules | Example |
|---|---|---|---|---|
| **Activity ID (CCID)** | *What marketing initiative?* | URL param `ccid`; lead record | Starts with `cc`, 8 chars; one per initiative | `cc010375` |
| **Drive To ID (DTID)** | *How am I driving traffic?* | URL param `dtid` | External vehicle only — not Cisco.com as the vehicle | `pdixsp001642` |
| **Offer ID** | *What gated asset did they consume?* | **Gated offer page HTML** — not a normal URL param | One ID per gated asset | `dmomrk033343` |
| **Event ID (EID)** | *What event context?* | Integrations, static data, manual uploads | Use when event metadata is required | *(varies)* |

**Memory aid:** CCID = *what* · DTID = *how* · Offer = *what they got* · Event = *when/where*

---

### Slide 26: UTM Tracking ID Types

| Parameter | What it answers | Key rules | Example |
|---|---|---|---|
| **`utm_id`** | Campaign / activation in analytics | **Must equal `ccid` today**; future = Workfront Channel ID (`CHL######`) | `utm_id=cc010375` |
| **`utm_medium`** | Marketing channel | Approved lowercase values; **drives channel reporting** | `paid-direct` |
| **`utm_source`** | Platform or vendor | Must match channel context; from *Source and Mediums.xlsx* | `businessinsider` |
| **`utm_creative`** | Ad creative | `%ecid!` only for Paid Direct, Programmatic, Paid Social | `utm_creative=%ecid!` |
| **`utm_campaign`** | Campaign grouping | **Not used today** — omit | — |

**Roadmap note (keep your existing NB):** When Workfront Channel IDs are live, `utm_id` will adopt Channel ID and `ccid`/`dtid` can be retired from URLs.

---

### Slide 27: Empowering the Automation Engine Via Workfront

**Let Workfront build the URL whenever the activation goes through intake.**

1. Marketer selects **channel type** and **platform** in Workfront.
2. Workfront assigns **CCID**, **DTID**, and maps **`utm_medium` / `utm_source`** from *Source and Mediums.xlsx*.
3. Generated query string is appended to the destination URL — **no manual UTM editing**.

**Use Stensul** for supported email flows; **Manual URL Builder** for web-referral and exceptions.

**If a source or medium is missing → escalate.** Do not create local variants.

---

### Slide 28: Dissecting the Hybrid URL Requirements

Show **two side-by-side examples** labeled clearly:

#### TODAY — Required hybrid URL (FY27)

```text
https://www.cisco.com/.../index.html
  ?ccid=cc010375
  &dtid=pdixsp001642
  &utm_id=cc010375
  &utm_medium=paid-direct
  &utm_source=businessinsider
  &utm_creative=%ecid!
```

✅ `utm_id` **matches** `ccid` · all values lowercase · `&` separates params

#### FUTURE — After Workfront Channel IDs (preview only)

```text
https://www.cisco.com/.../index.html
  ?utm_id=CHL000093
  &utm_medium=paid-direct
  &utm_source=businessinsider
  &utm_creative=%ecid!
```

⚠️ Do **not** use this pattern until governance confirms Channel ID in production URLs.

**Remove the current Slide 28 example** that mixes `ccid=cc010375` with `utm_id=CHL000093` without labeling — that is the single biggest source of confusion in the deck.

---

### Slide 34: When to use your IDs (replacement)

Replace the wide matrix with **scenario-based cards**. Each scenario: *situation → URL params → CTT / Workfront → do not*.

| Scenario | Put on the URL | Put elsewhere | Do NOT |
|---|---|---|---|
| **External link to Cisco.com** (email, paid, social, syndication, referral) | `ccid`, `dtid`, `utm_id`, `utm_medium`, `utm_source` (+ `utm_creative` if paid) | Workfront Channel ID auto-mapped when live | Use Offer ID as a URL param |
| **Internal Cisco.com CTA or page link** | Nothing | — | Any CTT or UTM params |
| **Gated offer landing page (AEM)** | — | **Offer ID** (+ **Content ID**) in page HTML / AEM metadata | Tag internal navigation with DTID |
| **Manual upload (MUSE template)** | — | **CCID** + **DTID** in template columns; Offer/Event as applicable | UTM params (not a live URL) |
| **Integrate / PathFactory / BrightTalk** | Per integration spec | **CCID**, **DTID**, **Offer ID** in payload | Assume UTMs replace integration metadata |

**Quick rule of thumb (make this a callout box):**

- **URL driving traffic from outside Cisco.com?** → Hybrid URL params (let Workfront generate).
- **Lead needs sales context?** → CTT IDs on the lead record (CCID minimum; add DTID, Offer, Event as scenario requires).
- **Gated asset on Cisco.com?** → Offer ID (+ Content ID) on the **page**, not the ad link.
- **Workfront Project ID?** → Internal only — never on an external URL.

---

## Terminology cheat sheet (add as appendix or speaker notes)

| User-facing name | Code / param | Retiring? |
|---|---|---|
| Activity ID | CCID → `ccid` | `ccid` retires when Channel ID replaces `utm_id` |
| Drive To ID | DTID → `dtid` | Replaced by `utm_medium` + `utm_source` |
| Offer ID | Offer ID in HTML | Stays — not a UTM |
| Event ID | EID | Stays for event contexts |
| Workfront Project ID | `PA######` | Internal only |
| Workfront Channel ID | `CHL######` | Future `utm_id` |
| Workfront Content ID | `CON######` | AEM gated pages |

Always pair **CCID** with the words *Activity ID* at first use in each module.

---

## What to deprioritize or move to appendix

These slides are valuable but **slow the “which ID do I use?” story** if placed before the decision guide:

- Slides 12–14 (reporting screenshots) → appendix or “see also”
- Slides 19–21 (Anatomy of a Deal, VDP, Content Impact) → appendix unless audience is analytics-heavy

Keep Slide 15 (Seller Enablement) — it makes the *why* tangible.

---

## Alignment with repo source of truth

When Slide 28 or 26 conflict with other materials, **`UTM Framework New Training.md` wins for current-state URL rules** until governance publishes Channel ID go-live criteria.

Open items to confirm before final publish (from training deck):

- Final FY27 precedence order (`utm_medium` confirmed as highest priority)
- Persistence behavior by reporting surface
- CCID/DTID retirement criteria and date
- Channel ID naming and handoff process
- Whether `utm_campaign` activates in FY27

---

## Suggested next step

1. Fix Slide 28 (today vs future URL) first — highest-impact change.
2. Fill Slides 3, 4, 6, 7, 26, 27 from this guide.
3. Replace Slide 34 matrix with scenario cards.
4. Add terminology footers to Modules 2 and 5 linking CCID ↔ Activity ID and Channel ID ↔ future `utm_id`.

Once content is stable, consider adding a Markdown source + generator (same pattern as `FY27 Tagging and Tracking Training Deck.md`) so hybrid rules stay in sync with `UTM Framework New Training.md`.
