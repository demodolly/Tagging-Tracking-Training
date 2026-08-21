# Purpose & Outcome Review — Semi Final Deck

**Deck:** `Tagging & Tracking Overview - FY27 - Semi Final.pptx`  
**Review date:** August 2026

---

## Your stated Purpose

> This guide is here to help you make sense of creating tracking URLs without any confusion. You'll learn which tags and UTM codes are needed for your campaigns **right now**. This training will show you how the data you enter every day affects everything else, helping you keep things organized and avoid mistakes that impact strategic marketing reporting.

## Your stated Outcome

> You will gain the confidence to independently **build, validate, and deploy** flawless tracking URLs across all marketing channels without fear of breaking downstream data. Ultimately, your mastery of these rules ensures that every lead you generate is credited correctly, protecting our fractional attribution and directly empowering our sales teams with the accurate customer context they need to win deals.

---

## Verdict (after updates)

| Goal | Before updates | After updates |
|---|---|---|
| **Purpose — no confusion** | Partially met. Strong module content, but Slide 28 mixed ccid and Channel ID in utm_id; Slide 4 “WE MUST” was empty. | **Mostly met.** Hybrid rules on Slide 4; corrected URL on Slide 28; today vs future labels on Slides 28, 36, 37. |
| **Purpose — tags needed right now** | Partially met. “Right now” buried in hybrid narrative; Workfront slides implied Channel ID in utm_id today. | **Mostly met.** Explicit TODAY callouts on Slides 4, 28, 36, 37. |
| **Purpose — daily data → downstream impact** | Partially met. Slide 5/9/13 touch this; not connected to user actions early. | **Improved.** Bridge on Slide 3; flow callout on Slide 6; validation ties to MSP/Adobe/seller impact on Slide 38. |
| **Outcome — build, validate, deploy** | Build: strong (Slides 38–42). Validate: **missing**. Deploy: implied only. | **Improved.** Module 6 workflow on Slide 34; Pre-Launch Checklist on Slide 38; examples on Slides 40–42. |
| **Outcome — lead credit & seller context** | Strong in Modules 2–3 and Slide 15; not tied back to URL checklist. | **Improved.** Slide 34 and 38 explicitly link validation to lead credit and seller context. |

**Overall:** The Semi Final deck **now fulfills the Purpose and Outcome**, with remaining polish opportunities noted below.

---

## What already worked well

- **Slide 3** — Purpose, Outcome, and Plan are clearly stated.
- **Slides 5, 9, 13, 15** — Connect tagging to pipeline, fractional attribution, and seller enablement.
- **Slides 35–37** — Splitting Legacy / UTM / Workfront IDs is the right structure for hybrid state.
- **Slides 38–42** — Manual URL Builder walkthroughs support independent URL building.
- **Slide 15** — Seller good/bad examples make CRM context tangible.

---

## Gaps that were fixed in this update

1. **Slide 1** — Subtitle now reflects create / validate / deploy and “right now” UTM needs.
2. **Slide 3** — Bridge text links daily Workfront/URL Builder entries to lead credit and seller CRM context.
3. **Slide 4** — Filled **WE MUST** with required hybrid parameters for TODAY.
4. **Slide 6** — Added downstream flow: daily choices → leads → attribution → sellers → reporting.
5. **Slide 28** — Fixed `utm_id=cc010375` (matches ccid); added TODAY vs FUTURE labels and validate callout.
6. **Slides 31–32** — Channel ID / utm_id wording aligned to today (ccid on URL) vs future (Channel ID).
7. **Slide 34** — Module 6 intro: Choose → Build → Validate → Deploy, tied to Outcome language.
8. **Slides 35–37** — Table comments clarified; removed ambiguous “Channel ID in utm_id today” guidance.
9. **Slide 38** — Pre-Launch Validation Checklist added before Manual URL Builder section.
10. **Slides 40–42** — Fixed `https:////` typo in example URLs.

---

## Remaining polish (optional)

These do not block Purpose/Outcome delivery but would strengthen the story:

1. **Slide 35 row 4 (Integrate)** — Comments column is still empty; add syndication ID guidance.
2. **Slides 12–14** — Consider moving reporting deep-dives to appendix so “what do I do today?” arrives sooner.
3. **Single capstone slide** — Optional one-page summary after Slide 37 combining Legacy + UTM + Workfront for the top 3 use cases (external URL, gated page, MUSE upload).
4. **Slide 3 Plan box** — Could add a fourth bullet: “Validate every URL before launch using the checklist.”

---

## Regenerate after template edits

```bash
python3 update_semi_final_deck.py
```

Backup saved to `Tagging & Tracking Overview - FY27 - Semi Final.backup.pptx` on first run.
