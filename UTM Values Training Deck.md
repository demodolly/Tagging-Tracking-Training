# UTM Values Training Deck

**Source document:** `UTM Framework New Training.md`  
**Training purpose:** Provide a focused, editable slide deck showing how UTM values are used, why they matter, how users should select them, and what happens when they are used incorrectly.

> Editing note: This Markdown file is the editable source for the generated PowerPoint deck `UTM Values Training Deck.pptx`. Update this file first, then run `python3 generate_utm_values_deck.py` to regenerate the PPTX.

---

## Slide 1: How to Use UTM Values

- What UTM values do
- Which UTM values are required today
- How Workfront maps intake selections to UTM values
- When to include optional or conditional values
- What goes wrong when UTM values are incorrect

Speaker notes:
- This is a focused deck for users who need to understand UTM values specifically, separate from the broader CTT and precedence/persistence training.

---

## Slide 2: Why UTM values matter

- UTMs standardize how digital marketing traffic is classified in analytics.
- They identify the channel, platform or vendor, campaign identifier, and creative context.
- They help compare which sources are driving traffic and which channels are performing.
- They reduce manual naming variations that split reporting across duplicate buckets.
- They support the transition from legacy CCID/DTID tracking to a UTM-based framework.

Speaker notes:
- Source basis: the framework states Cisco is actively transitioning from legacy CCID/DTID tracking to a UTM-based framework managed through Workfront.

---

## Slide 3: Current-state UTM usage

Every standard tracking URL must include:

1. `utm_id`
2. `utm_medium`
3. `utm_source`

Also required during the current hybrid state:

- `ccid`
- `dtid`

Conditional:

- `utm_creative` is required only for Paid Direct, Paid Programmatic, and Paid Social.

Speaker notes:
- The source document requires `ccid`, `dtid`, `utm_id`, `utm_medium`, and `utm_source` on every tracking URL today.

---

## Slide 4: Future-state UTM usage

Future-state direction from the UTM framework:

- Workfront Channel IDs will replace the current `ccid` value in `utm_id`.
- `dtid` will be replaced by `utm_source` and `utm_medium`.
- When that future state is available, `ccid` and `dtid` can be removed from standard URLs.
- `utm_campaign` remains reserved until an organization-wide strategy is defined.

Speaker notes:
- Keep this slide as the transition anchor: users should not remove `ccid` or `dtid` until the future-state criteria are confirmed.

---

## Slide 5: UTM value roles at a glance

| UTM value | What it identifies | Required today? |
|---|---|---|
| `utm_id` | Campaign or activation identifier | Yes |
| `utm_medium` | Marketing channel | Yes |
| `utm_source` | Platform or vendor | Yes |
| `utm_campaign` | Future campaign grouping | No; reserved |
| `utm_creative` | Ad-server creative ID | Only for selected paid channels |

Speaker notes:
- The current framework uses six core parameters on standard tracking URLs, but `utm_campaign` is optional and reserved for future use.

---

## Slide 6: `utm_id`

Purpose:

- Passes the campaign or activation identifier into analytics.
- Today, it must equal the `ccid` value exactly.
- Future state will use Workfront Channel IDs when available.

Correct current-state example:

```text
ccid=cc008317&utm_id=cc008317
```

Impact of misuse:

- If `utm_id` does not match `ccid`, campaign-level attribution can break or split.

Speaker notes:
- This is one of the easiest validation checks for users: `utm_id` and `ccid` should be identical in current-state URLs.

---

## Slide 7: `utm_medium`

Purpose:

- Identifies the marketing channel.
- It is the highest-priority input for channel classification in analytics.

Approved values:

- `paid-direct`, `programmatic`, `cpc`, `paid-social`, `social`
- `syndication`, `ratings-reviews`, `email`, `direct-mail`, `web-referral`

Impact of misuse:

- Missing or inconsistent `utm_medium` values cause channel misattribution.

Speaker notes:
- `web-referral` is for URL generator or manual builds only; there is no Workfront project type for web referral today.

---

## Slide 8: `utm_source`

Purpose:

- Identifies the specific vendor or platform within the channel.
- Workfront renders the appropriate platform field based on Channel Type.
- The selected friendly value maps to a standardized lowercase, hyphenated source value.

Examples:

- Email: `eloqua`, `marketo`, `salesforce`
- Paid Search: `google`, `bing`, `baidu`
- Paid Social: `linkedin`, `reddit`, `x`
- Programmatic: `dv360`, `youtube`

Speaker notes:
- The authoritative Workfront mapping is `Source and Mediums.xlsx`; this repo mirrors that mapping for training and analytics audiences.

---

## Slide 9: `utm_campaign`

Purpose:

- Reserved for future campaign-level tagging once an organization-wide strategy is defined.

Current rule:

- Not required on standard tracking URLs today.
- Do not treat omission as a defect for Workfront, Stensul, or URL Builder flows.
- Omit it entirely until the strategy is defined.

Impact of misuse:

- Early local naming conventions could create inconsistent campaign reporting that must later be cleaned up.

Speaker notes:
- This slide prevents users from adding empty or locally invented `utm_campaign` values.

---

## Slide 10: `utm_creative`

Purpose:

- Captures the ad-server creative ID for creative-level attribution.

Required only for:

- Paid Direct
- Paid Programmatic using DV360 or YouTube
- Paid Social

Value:

```text
utm_creative=%ecid!
```

Speaker notes:
- CM360 replaces the `%ecid!` macro when the creative is served or clicked. Omit `utm_creative` entirely for all other channel types.

---

## Slide 11: Workfront mapping logic

Workfront uses intake selections to automate UTM values:

- `uap Channel Type` maps to `utm_medium`.
- The channel-specific platform field maps to `utm_source`.
- Example fields include `uap Email Platform Type`, `uap Social Platform`, and `uap Search Engine`.
- Paid Programmatic uses the trafficking partner selection to emit `dv360` or `youtube`.
- TradeDesk is reserved for future use and hidden in Workfront today.

Speaker notes:
- Workfront should generate the URL for Workfront channel activations so users do not manually build query strings.

---

## Slide 12: Global UTM formatting rules

- Use lowercase values.
- Use hyphens instead of spaces.
- Omit empty parameters entirely.
- Keep `utm_id` equal to `ccid` in current-state URLs.
- Do not create local source or medium variants.
- Do not include spaces or special characters in values.

Correct examples:

- `paid-social`
- `technologyadvice`
- `security-info-watch`

Speaker notes:
- The query string uses separators like `?`, `&`, and `=`, but those should not appear inside parameter values.

---

## Slide 13: Correct URL patterns

With creative:

```text
URL?ccid=[ccid]&dtid=[dtid]&utm_id=[ccid]&utm_medium=[medium]&utm_source=[source]&utm_creative=%ecid!
```

Without creative:

```text
URL?ccid=[ccid]&dtid=[dtid]&utm_id=[ccid]&utm_medium=[medium]&utm_source=[source]
```

Parameter order:

- `ccid`, `dtid`, `utm_id`, `utm_medium`, `utm_source`, `utm_creative`

Speaker notes:
- The order shown mirrors the framework construction rules and makes URLs easier to validate.

---

## Slide 14: Channel examples

| Channel | `utm_medium` | `utm_source` example | `utm_creative`? |
|---|---|---|---|
| Paid Direct | `paid-direct` | `techtarget` | Yes |
| Paid Programmatic | `programmatic` | `dv360` | Yes |
| Paid Search | `cpc` | `google` | No |
| Paid Social | `paid-social` | `linkedin` | Yes |
| Organic Social | `social` | `linkedin` | No |
| Email | `email` | `eloqua` | No |

Speaker notes:
- Use this as a quick comparison slide to show how channel context changes the required URL pattern.

---

## Slide 15: Common mistakes and impacts

| Mistake | Impact |
|---|---|
| `utm_medium=Paid Social` | Capitalization creates inconsistent channel reporting |
| `utm_medium=social` for paid social | Paid activity may report as organic social |
| `utm_source=LinkedIn Ads` | Splits reporting from approved `linkedin` |
| `utm_id` differs from `ccid` | Campaign attribution mismatch |
| Missing `utm_creative` on Paid Direct | Creative-level attribution gap |
| `utm_campaign=` with no value | Adds noise; empty parameters should be omitted |

Speaker notes:
- These examples are intentionally practical so users can spot errors before launch.

---

## Slide 16: User checklist

Before using a URL, confirm:

- The URL was generated through Workfront, Stensul, or the approved URL Builder.
- `utm_id`, `utm_medium`, and `utm_source` are present.
- `ccid` and `dtid` are present during the current hybrid state.
- `utm_id` matches `ccid` during the current hybrid state.
- `utm_medium` is an approved value.
- `utm_source` is approved for the selected channel.
- `utm_creative=%ecid!` appears only when required.
- Empty or future-only parameters are omitted.

Speaker notes:
- This slide can be used as a final launch-readiness check.

---

## Slide 17: Where to go for updates

- Workfront source of truth: `Source and Mediums.xlsx`
- Repository framework: `UTM Framework New Training.md`
- Editable source for this deck: `UTM Values Training Deck.md`
- Generated PowerPoint: `UTM Values Training Deck.pptx`

Open items to confirm:

- Future Workfront Channel ID timing and naming
- Final `utm_campaign` strategy
- Any new approved `utm_source` values
- Any changes to `utm_creative` channel requirements

Speaker notes:
- If the Workfront mapping and this deck differ, the source-of-truth mapping should win and this deck should be updated.
