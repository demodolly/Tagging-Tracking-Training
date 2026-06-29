# FY27 Tagging and Tracking Training Deck

**Source document:** `UTM Framework New Training.md`  
**Training purpose:** Explain how campaign tagging, tracking IDs, and UTM parameters work together; when users should use each; and what goes wrong when values are missing, inconsistent, or manually overridden.

> Editing note: This Markdown file is the editable source for the generated PowerPoint deck `FY27 Tagging and Tracking Training Deck.pptx`. Update this file first when FY27 precedence or persistence logic changes, then run `python3 generate_fy27_deck.py` to regenerate the PPTX.

---

## Slide 1: FY27 Campaign Tagging and Tracking Training

- Campaign Tagging IDs, Tracking IDs, and UTM parameters
- Why the framework changed
- How to build correct tracking URLs
- Impacts of incorrect tagging
- FY27 precedence and persistence discussion points

Speaker notes:
- This deck is based on repository content current as of the May 13, 2026 update.
- The repo source states that Cisco is in an active transition from the legacy CCID/DTID system to a UTM-based framework.

---

## Slide 2: What users should know by the end

- Which identifiers and UTM parameters are required today
- When Workfront should generate the tracking URL
- When Stensul or the Manual URL Builder may be used
- Which channels require `utm_creative`
- Why `utm_medium` and `utm_source` must be standardized
- How incorrect values affect attribution, reporting, and optimization

Speaker notes:
- Position this as practical enablement: users should leave knowing when to rely on automation and when to escalate instead of improvising.

---

## Slide 3: Why campaign tagging exists

- Every channel activation that drives traffic to a Cisco central marketing-owned property needs a properly formatted tracking URL.
- Campaign tagging connects the activation to the system of record.
- Tracking IDs and UTM values give analytics consistent dimensions for campaign, channel, vendor, and creative reporting.
- Standardization reduces manual query-string errors and inconsistent channel classification.

Speaker notes:
- Repository source: Workfront is the centralized intake tool for campaign activation tracking URL generation.

---

## Slide 4: Why UTMs were introduced

- Cisco is transitioning from the legacy CCID/DTID tracking system to a UTM-based framework.
- Current state is hybrid: legacy IDs and UTM values are both required.
- Future state: Workfront Channel IDs will replace `ccid` in `utm_id`.
- Future state: `dtid` will be replaced by `utm_source` and `utm_medium`.
- UTM values support standardized analytics across Workfront, Stensul, and Manual URL Builder flows.

Speaker notes:
- Keep this slide focused on the business reason: UTMs make channel and vendor attribution explicit and standardized.

---

## Slide 5: Future-state measurement model: CTT plus UTM

Future-state tracking should use both value families with clearer roles:

- CTT values identify the marketing initiative, traffic blueprint, offer, or event context.
- UTM values identify the digital traffic path: channel, platform/vendor, campaign, and creative.
- Workfront remains the preferred place to automate values and reduce manual URL building.
- Adobe and marketing effectiveness reporting use standardized UTMs to compare channel and source performance.
- Lead, nurture, VDC, and seller context continue to depend on CTT-aligned metadata.

Speaker notes:
- Source basis: the FY27 overview deck positions tagging and tracking as the connective tissue between marketing spend, customer engagement, lead routing, pipeline reporting, and seller context.

---

## Slide 6: How CTT values will be used

| CTT value | Future usage | User guidance |
|---|---|---|
| Activity ID / CCID | Campaign, program, lead scoring, nurture, pipeline, and VDC alignment | Use for marketing initiatives expected to generate pipeline or enter scoring/nurture |
| Drive To ID / DTID | Channel or vehicle that drives the customer to Cisco-owned web properties | Use for external traffic-driving links; do not treat Cisco.com as the vehicle |
| Offer ID | Gated offer or asset consumed before lead generation | Add in the gated offer page HTML, not as a normal URL parameter |
| Event ID / EID | Event or integrated activity context | Use for event integrations, static data, manual uploads, and relevant non-URL sources |

Speaker notes:
- The old CTT deck states IDs are captured for all marketing sources, not just digital. That means CTT continues to support offline, static, manual-upload, event, and integration scenarios where UTMs alone are insufficient.

---

## Slide 7: How UTM values will be used

| UTM value | Future usage | Cisco alignment from source decks |
|---|---|---|
| `utm_id` | Universal ID carrying reporting attributes | Activity ID today; future Workfront Channel ID when available |
| `utm_medium` | Marketing method or channel | Vehicle / channel classification |
| `utm_source` | Platform, website, vendor, or source | Sub-vehicle / vendor classification |
| `utm_campaign` | Campaign or promotion grouping | Future campaign-level strategy; not required today |
| `utm_creative` | Creative or placement-level detail | Paid creative attribution where required |

Speaker notes:
- The UTM overview deck describes the goal as automated Universal IDs and UTM codes, standard Adobe reporting, Ace reporting alignment, and one standard tool to create and manage IDs and UTM values.

---

## Slide 8: Future URL direction

Current hybrid URL:

```text
URL?ccid=[ccid]&dtid=[dtid]&utm_id=[ccid]&utm_medium=[medium]&utm_source=[source]
```

Future direction after Workfront Channel IDs are available:

```text
URL?utm_id=[workfront-channel-id]&utm_medium=[medium]&utm_source=[source]
```

Still conditional:

- Add `utm_creative=%ecid!` only for channels that require creative-level attribution.
- Add `utm_campaign` only after the organization-wide campaign strategy is defined.
- Keep CTT values in the correct system or placement when they still power lead, nurture, offer, event, or static-data use cases.

Speaker notes:
- Repository source says future Workfront Channel IDs will replace the `ccid` value in `utm_id`, `dtid` will be replaced by `utm_source` and `utm_medium`, and both `dtid` and `ccid` can be removed at that time.

---

## Slide 9: What users should do differently in the future

Do:

- Let Workfront or the approved builder generate UTM values whenever possible.
- Use CTT IDs for campaign, drive-to, offer, event, static-data, and lead-flow context.
- Use UTMs for digital traffic attribution and channel/source optimization.
- Escalate when a required source, medium, or CTT value does not exist.

Do not:

- Add CTT IDs to internal Cisco.com URLs or internal CTAs.
- Put Offer IDs into ordinary URL parameters when the offer should be tagged in page HTML.
- Create local `utm_medium` or `utm_source` variants.
- Assume UTMs replace every CTT use case; CTT still supports non-digital and lead-context scenarios.

Speaker notes:
- This combines the CTT key takeaways with the UTM transition logic: UTMs improve standardized digital attribution, while CTT values still preserve campaign, offer, event, and lead-generation context.

---

## Slide 10: Current-state URL anatomy

Every standard tracking URL must include:

1. `ccid`
2. `dtid`
3. `utm_id`
4. `utm_medium`
5. `utm_source`

Conditional:

- `utm_creative` is required only for Paid Direct, Paid Programmatic, and Paid Social.
- `utm_campaign` is optional and reserved for future use; omit it for standard tracking URLs today.

Speaker notes:
- Source deck detail: `utm_campaign` omission is not a defect today.

---

## Slide 11: What each required value does

| Value | Purpose | Training takeaway |
|---|---|---|
| `ccid` | Identifies the channel activation in the system of record | Required on every tracking URL |
| `dtid` | Identifies channel and platform/vendor in the legacy framework | Required during current hybrid state |
| `utm_id` | Passes the campaign identifier into analytics | Must equal `ccid` exactly today |
| `utm_medium` | Identifies the marketing channel | Highest-priority channel classification input |
| `utm_source` | Identifies vendor or platform within the channel | Must come from approved mappings |

Speaker notes:
- Reinforce that `ccid` and `utm_id` are the same identifier passed in two ways in the current state.

---

## Slide 12: When to use Campaign Tagging and Tracking IDs

Use `ccid` and `dtid` for:

- All activations in the current hybrid state
- Reporting that still depends on legacy campaign and channel identifiers
- Maintaining continuity while Workfront Channel IDs and UTM-based attribution mature

Do not:

- Drop `ccid` or `dtid` before future-state guidance says they are retired
- Create new ID formats outside the approved standard
- Let `utm_id` differ from `ccid`

Speaker notes:
- `ccid` must start with `cc` and be 8 characters long, for example `cc008317`.

---

## Slide 13: When to use UTM parameters

Use UTMs whenever an activation drives traffic to a Cisco central marketing-owned property.

Required today:

- `utm_id`: campaign/activation identifier; equals `ccid` today
- `utm_medium`: channel classification
- `utm_source`: platform/vendor classification

Conditional:

- `utm_creative=%ecid!`: only for Paid Direct, Paid Programmatic, and Paid Social

Reserved:

- `utm_campaign`: future use; omit today unless the standard changes

Speaker notes:
- UTMs can be created via Workfront, Stensul, and Manual URL Builder, but the same value rules apply.

---

## Slide 14: Use the right build path

| Situation | Recommended path | Why |
|---|---|---|
| Workfront channel activation | Workfront-generated URL | Centralized intake and mapping source of truth |
| Email or other supported non-Workfront flow | Stensul when applicable | Same UTM rules, managed by the owning team |
| External web referral or exception | Manual URL Builder | `web-referral` is manual-build only today |
| Missing source/medium option | Escalate for mapping update | Avoid creating unapproved values |

Speaker notes:
- Source says Workfront execution source of truth is `Source and Mediums.xlsx`.
- If source documents differ, `Source and Mediums.xlsx` wins.

---

## Slide 15: Global tagging rules

- All UTM values must be lowercase.
- Use hyphens instead of spaces.
- Omit empty parameters entirely.
- `utm_id` must always match `ccid`.
- No spaces or special characters (`&`, `%`, `?`, `=`) in values.
- Use approved values; do not create local variants.

Examples:

- Correct: `paid-social`, `technologyadvice`, `security-info-watch`
- Incorrect: `Paid Social`, `Technology Advice`, `security_info_watch`

Speaker notes:
- The query string itself uses `&`, `%`, `?`, and `=`, but parameter values should not include those characters except the required `%ecid!` macro for `utm_creative`.

---

## Slide 16: Approved `utm_medium` values

- `paid-direct`
- `programmatic`
- `cpc`
- `paid-social`
- `social`
- `syndication`
- `ratings-reviews`
- `email`
- `direct-mail`
- `web-referral`

Important:

- `web-referral` is for URL generator or manual builds only.
- No Workfront project type exists for web referral today.

Speaker notes:
- `utm_medium` is auto-populated based on channel type, not a user-facing dropdown.

---

## Slide 17: `utm_source` depends on channel

`utm_source` identifies the vendor or platform within the channel.

Examples:

- Email: `eloqua`, `marketo`, `salesforce`
- Paid Direct: `bloomberg`, `foundry`, `techtarget`
- Programmatic: `dv360`, `youtube`
- Paid Social / Organic Social: `linkedin`, `reddit`, `x`, `youtube`
- Paid Search: `google`, `bing`, `baidu`
- Ratings and Reviews: `g2`, `gartner`, `trustradius`
- Syndication: `activate`, `technologyadvice`, `netline`

Speaker notes:
- A value can appear in more than one channel, such as `foundry` or `trustradius`; the combination of source and medium gives the reporting context.

---

## Slide 18: Channel-specific rules users often miss

- Paid Programmatic:
  - Show only DV360 and YouTube in Workfront today.
  - TradeDesk is reserved for future use and hidden in the UI.
  - Always append `utm_creative=%ecid!`.
- Paid Direct, Paid Programmatic, Paid Social:
  - Require `utm_creative=%ecid!`.
- Direct Mail:
  - No approved `utm_source` list exists yet.
  - Use lowercase and hyphens until standardized values are published.
- Paid Direct legacy sources:
  - Under review; do not add new activations using those values.

Speaker notes:
- Users should not use legacy sources for new activations unless governance explicitly approves.

---

## Slide 19: Precedence and persistence logic - FY27 edit slide

Repository-backed rule:

- `utm_medium` is the highest-priority input for channel classification in analytics.

Training implication:

- If `utm_medium` is missing, inconsistent, or manually changed, channel reporting can be misclassified.
- If `utm_source` does not match the selected channel context, vendor/platform reporting can be split or incorrectly grouped.
- If persisted values are retained downstream, early mistakes may continue to affect reporting until corrected.

FY27 owner edits:

- Add the current FY27 precedence order here.
- Add the current FY27 persistence rules here.
- Add any exceptions by channel, tool, or reporting surface here.

Speaker notes:
- The repository does not include the full FY27 persistence specification. Keep this slide as the update point when that logic is finalized.

---

## Slide 20: What happens when tagging is wrong

Incorrect or inconsistent tagging can cause:

- Campaign activity to be disconnected from the system of record
- `utm_id` and `ccid` mismatch, breaking campaign-level attribution
- Channel misclassification when `utm_medium` is wrong
- Vendor/platform reporting errors when `utm_source` is wrong
- Creative reporting gaps when required `utm_creative` is missing
- Duplicate reporting buckets caused by capitalization, spaces, or local naming variants
- Cleanup work for Marketing Operations, Analytics, and Workfront teams

Speaker notes:
- Anchor this in business impact: bad tags create bad data, and bad data drives the wrong optimization decisions.

---

## Slide 21: Example - correct paid social URL

Scenario:

- Channel: Paid Social
- Platform: LinkedIn
- CCID: `cc008317`
- DTID: `ppdllin001650`

Correct format:

```text
URL?ccid=cc008317&dtid=ppdllin001650&utm_id=cc008317&utm_medium=paid-social&utm_source=linkedin&utm_creative=%ecid!
```

Why it works:

- `utm_id` equals `ccid`
- `utm_medium` uses approved channel value
- `utm_source` uses approved social platform value
- `utm_creative` is included because Paid Social requires it

Speaker notes:
- Use this as the walkthrough example for query-string order and conditional creative tagging.

---

## Slide 22: Example - correct email URL

Scenario:

- Channel: Email
- Platform: Eloqua
- CCID: `cc008317`
- DTID: approved email DTID from intake

Correct format:

```text
URL?ccid=cc008317&dtid=[dtid]&utm_id=cc008317&utm_medium=email&utm_source=eloqua
```

Why it works:

- Email does not require `utm_creative`
- `utm_source` is an approved email platform
- Empty or future-only parameters are omitted

Speaker notes:
- The source document lists email source values but does not list email DTID values in the provided DTID table; keep DTID populated from approved intake/mapping data.

---

## Slide 23: Incorrect examples and impacts

| Incorrect pattern | Impact |
|---|---|
| `utm_medium=Paid Social` | Creates inconsistent channel classification |
| `utm_medium=social` for paid social | Paid activity may report as organic social |
| `utm_source=LinkedIn Ads` | Splits platform reporting from approved `linkedin` |
| `utm_id=cc008318` while `ccid=cc008317` | Campaign attribution mismatch |
| Missing `utm_creative` on Paid Direct | Creative-level attribution gap |
| Empty parameter like `utm_campaign=` | Adds noise; omit future-only or empty parameters |

Speaker notes:
- These are training examples based on the rules in the repository source.

---

## Slide 24: User checklist before launch

Before a URL is used, confirm:

- The build path is correct: Workfront, Stensul, or Manual URL Builder.
- `ccid`, `dtid`, `utm_id`, `utm_medium`, and `utm_source` are present.
- `utm_id` exactly matches `ccid`.
- `utm_medium` is one of the approved values.
- `utm_source` is approved for the channel.
- `utm_creative=%ecid!` is included only when required.
- Values are lowercase and hyphenated.
- Empty parameters are omitted.

Speaker notes:
- This can become a one-page job aid for launch readiness.

---

## Slide 25: Where to go for updates

- Workfront intake mappings: `Source and Mediums.xlsx`
- Repository source document: `UTM Framework New Training.md`
- CTT source context: `Tagging & Tracking Overview - FY27 New Training.pptx`
- Historical CTT usage context: `Creating your Activity ID - Old Training Presentation.pptx`
- Historical UTM strategy context: `UTM Overview - Old Training.pptx`
- Generated training deck: `FY27 Tagging and Tracking Training Deck.pptx`
- Editable deck source: `FY27 Tagging and Tracking Training Deck.md`

Open items for FY27:

- Confirm final precedence order.
- Confirm final persistence behavior by reporting surface.
- Confirm when CCID/DTID retirement criteria are met.
- Confirm the final future-state Workfront Channel ID naming and handoff process.
- Confirm whether `utm_campaign` becomes active and what naming convention it should follow.
- Confirm any new approved `utm_source` values.

Speaker notes:
- If governance changes, update the source Markdown and regenerate the PPTX so the repository remains the training source of truth.
