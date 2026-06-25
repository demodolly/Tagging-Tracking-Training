# UTM Framework

**Created by:** Stephanie Boyd
**Date:** January 28, 2026
**Updated:** May 13, 2026 (added `web-referral` to WF-2 mapping table, fixed `technologyadvice` source value, synced with Standard Channel Identification)
**Source:** Standard Channel Identification
**Workfront execution (source of truth for intake mappings):** *Source and Mediums.xlsx* (channel type → `utm_medium` / platform → `utm_source`, query string examples)

# Table of Contents

1. [Overview](#section-1-overview)
    - [Purpose](#purpose)
    - [Transition Context](#transition-context)
2. [URL Tracking Parameters](#section-2-url-tracking-parameters)
    - [Global Tagging Rules](#global-tagging-rules)
3. [Workfront Requirements](#section-3-workfront-requirements)
    - [WF-1) Intake Form Automation Requirements by Project Type](#wf-1-intake-form-automation-requirements-by-project-type)
    - [WF-2) Mapping Intake Values to UTMs](#wf-2-mapping-intake-values-to-utms)
    - [WF-3) Query String Construction Rules](#wf-3-query-string-construction-rules)

---

# Section 1: Overview

## Purpose

Any channel activation driving traffic to a **Cisco central marketing-owned property** must have a properly formatted tracking URL. This document defines the current standards (as of April 2026) for URL construction and required values.

**Workfront** is the centralized intake tool. When a campaign activation is submitted through Workfront, the system uses the information entered in the intake form to automatically generate the complete tracking URL, eliminating the need for teams to manually build query strings.

UTM values can also be created via Stensul and the Manual URL Builder; the same rules apply but are managed by different teams.

**This document serves two audiences:**

- **Marketing Operations / Campaign Teams** — Approved parameter values, formatting rules, and standards for consistent channel attribution in analytics.
- **Workfront Configuration Team** — Intake form requirements: which fields to show per project type, how selections map to tracking parameters, and how the query string should be auto-constructed and appended to the destination URL.

---

## Transition Context

Cisco is in an **active transition** from the legacy CCID/DTID tracking system to a UTM-based framework managed through Workfront. This document reflects **current-state requirements** — a hybrid of both systems. Future-state notes are included throughout.

> **Current state:** All activations must include `ccid`, `dtid`, `utm_id`, `utm_medium`, and `utm_source` on every tracking URL. `utm_creative` is required **only** for **Paid Direct**, **Paid Programmatic** (DV360 or YouTube), and **Paid Social** — see [Channel Type Query String Reference](#channel-type-query-string-reference).
>
> **Future state:** When Workfront Channel IDs are available, they will replace the `ccid` value in `utm_id`. The `dtid` will be replaced by `utm_source` and `utm_medium`, and both `dtid` and `ccid` can be removed at that time.

---

# Section 2: URL Tracking Parameters

Six core parameters are used on every standard tracking URL; `utm_campaign` is optional and reserved for future use (see below).

> All parameter values must be **lowercase**. Use **hyphens** instead of spaces. Omit empty parameters entirely.

---

### 1) ccid

**Purpose:** Identifies the specific channel activation in the system of record.

**Standards:** Must start with `cc` and be 8 characters long (e.g., `cc008317`). Passed as a standalone parameter on the URL.

**How to populate:** Auto-populate from the `ccid` field captured in intake.

**Impact:** Enables tracking and attribution of channel activations in reporting systems. Required for all tracking URLs.

**Example:** `ccid=cc008317`

---

### 2) dtid

**Purpose:** Identifies the channel and platform/vendor for the activation.

**Standards:** Must use the approved DTID code for the placement type (see table below). Each code is unique to a channel/platform combination.

**How to populate:** Auto-populated based on Project Type and format selected in the intake form.

**Impact:** Ensures correct channel/platform attribution in analytics and reporting. Required for all tracking URLs.

**Example:** `dtid=pdixsp001642` (Direct Digital – Display)

| Placement Type | DTID Code |
|---|---|
| Direct Digital – Display | `pdixsp001642` |
| Direct Digital – Video | `pvixsp001643` |
| Programmatic – Display | `pddpxsp001644` |
| Programmatic – Video | `pdvpxsp001645` |
| Paid Search | `psexsp001647` |
| Audio – Direct | `ppdcxsp001648` |
| Audio – Programmatic | `paprxsp001649` |
| Paid Social – LinkedIn | `ppdllin001650` |
| Paid Social – Reddit | `ppdlsc69001651` |
| Paid Social – Twitter/X | `ppdltwt001652` |
| Offline (OOH, TV, Print) | `pptsc55001719` |
| Offline w/ QR Code | `pptsc70001792` |
| Ratings & Reviews – Other | `ooteotr001782` |
| Ratings & Reviews – TrustRadius | `ootetrs001781` |

---

### 3) utm_id

**Purpose:** Passes the CCID into the analytics platform for campaign attribution.

**Standards:** Must equal the `ccid` value exactly — they are the same identifier passed in two ways.

**How to populate:** Auto-populate from the `ccid` field.

**Impact:** Ensures campaign-level attribution in analytics platforms. Required for all tracking URLs.

**Example:** `ccid=cc008317` → `utm_id=cc008317` (values must match)

---

### 4) utm_medium

**Purpose:** Identifies the marketing channel. This is the highest-priority input for channel classification in analytics.

**Standards:** Must use one of the approved standardized values below. All values must be lowercase and use hyphens instead of spaces.

**How to populate:** Auto-populated in Workfront, Stensul, and URL Builder based on the Channel Type selected.

**Impact:** Drives channel classification in analytics and reporting. Inconsistent or missing values cause misattribution.

**Approved values:**

- `paid-direct`
- `programmatic`
- `cpc`
- `paid-social`
- `social`
- `syndication`
- `ratings-reviews`
- `email`
- `direct-mail`
- `web-referral` — URL UTM generator / manual builds only. No Workfront project type exists for web referral; use when needed outside Workfront.

---

### 5) utm_source

**Purpose:** Identifies the specific vendor or platform within the channel.

**How it works:**

1. The user selects a Channel Type (e.g., Paid Direct, Paid Programmatic, Paid Social).
2. The selected Channel Type determines which platform/vendor field is displayed (e.g., `uap Trafficking Partner`, `uap Social Platform`, `uap Search Engine`).
3. The value chosen in that field (the friendly label) is mapped to the `utm_source` value — always the lowercase version of the friendly label, with hyphens instead of spaces.

**Standards:** Only approved sources for each channel type may be used (see mapping tables below). All `utm_source` values must be lowercase with hyphens instead of spaces.

**How to populate:** The appropriate dropdown is rendered in Workfront based on the selected Channel Type. The selected value is mapped to the standard `utm_source` value for reporting and analytics.

**Impact:** Ensures accurate platform/vendor-level attribution and reporting.

**Approved `utm_source` values:** The authoritative Workfront mapping (friendly labels → `utm_source`) is ***Source and Mediums.xlsx***. This document mirrors that mapping for marketing and analytics audiences.

#### Email Sources (`utm_medium: email`)

- `eloqua`
- `gong`
- `marketo`
- `outreach`
- `outlook`
- `salesforce`

#### Paid Direct Sources (`utm_medium: paid-direct`)

- `bloomberg`
- `businessinsider`
- `extremetech`
- `fierce`
- `foundry`
- `international-security`
- `lifehacker`
- `light-reading`
- `loss-prevention-magazine`
- `mashable`
- `network-computing`
- `pcmag`
- `rcr-wireless`
- `register`
- `sdx-central`
- `security-info-watch`
- `security-magazine`
- `stack-overflow`
- `stack-overflow-network`
- `tech-brew`
- `techtarget`
- `venturebeat`
- `nfl`
- `ooh`
- `tv`
- `female-quotient`
- `hbr`
- `tbpn`

#### Paid Direct — Legacy Sources (under review)

> The following sources are currently active in Workfront but are not part of the standardized list. They are in review to be either formally added or removed next sprint. Do not add new activations using these values.

- `avid`
- `bnpmedia`
- `cnnnetwork`
- `fedscoop`
- `idgcommunications`
- `itmediajapan`
- `morning-brew`
- `nikkeixtechjp`
- `other`
- `outbrain`
- `posterscope`
- `rcrwireless2`
- `situationpublishing`
- `statescoop`
- `timesofindia`
- `washingtonpost`
- `zdnet`
- `ziffdavis`

#### Programmatic Sources (`utm_medium: programmatic`)

- `dv360` — automated when **DV360** is selected in `uap Trafficking Partner`.
- `youtube` — automated when **YouTube** is selected in `uap Trafficking Partner`.
- `tradedesk` — reserved for future use; remains in the picklist definition but is **not shown** in Workfront today. When enabled, uses the same URL pattern as DV360 with literal `utm_source=tradedesk` and `utm_creative=%ecid!`.

#### Paid Social Sources (`utm_medium: paid-social`)

- `bluesky`
- `facebook`
- `instagram`
- `linkedin`
- `meta`
- `reddit`
- `weibo`
- `x`
- `xing`
- `youtube`

#### Organic Social Sources (`utm_medium: social`)

- `bluesky`
- `facebook`
- `instagram`
- `linkedin`
- `meta`
- `reddit`
- `weibo`
- `x`
- `xing`
- `youtube`

#### Paid Search Sources (`utm_medium: cpc`)

- `baidu`
- `bing`
- `daum`
- `google`
- `naver`
- `sogou`
- `yahoo`
- `yandex`

#### Ratings and Reviews Sources (`utm_medium: ratings-reviews`)

- `capterra`
- `g2`
- `gartner`
- `getapp`
- `peerspot`
- `software-advice`
- `trustradius`

#### Content Syndication Sources (`utm_medium: syndication`)

- `activate`
- `ai-techpark`
- `anteriad`
- `b2biq`
- `bluewhale-research`
- `brighttalk`
- `bython`
- `chronicle-highered`
- `demandworks`
- `endeavor`
- `erepublic`
- `foundry` *(also Paid Direct)*
- `govexec`
- `govloop`
- `infuse`
- `interlink`
- `intentsify`
- `ismg`
- `netline`
- `peerspot` *(also Ratings and Reviews)*
- `pharosiq`
- `technologyadvice`
- `techtarget` *(also Paid Direct)*
- `trustradius` *(also Ratings and Reviews)*

---

### 6) utm_campaign

**Purpose:** Reserved for future campaign-level tagging once an organization-wide strategy is defined.

**Standards:** Not required on standard tracking URLs today. Do not treat omission as a defect for Workfront, Stensul, or URL Builder flows.

**How to populate:** When a strategy exists, this section will be updated. Until then, omit `utm_campaign` entirely.

**Impact:** No current reporting or ingestion requirement; future use only.

---

### 7) utm_creative

**Purpose:** Captures the ad-server creative ID for creative-level attribution.

**Standards:** Required **only** for **Paid Direct**, **Paid Programmatic** (DV360 or YouTube), and **Paid Social**.

**How to populate:** Use the macro `%ecid!` as the `utm_creative` value. CM360 replaces this token when the creative is served or clicked. Omit the `utm_creative` parameter entirely for all other channel types.

**Impact:** Enables creative-level attribution and optimization for paid placements that use ad-server creative IDs.

**Value:** `utm_creative=%ecid!`

---

## Global Tagging Rules

- All UTM values must be lowercase.
- Use hyphens instead of spaces.
- `utm_id` must always match the `ccid` value on the same URL.
- Omit empty parameters entirely — do not include a parameter with no value.

---

# Section 3: Workfront Requirements

> This section is for the **Workfront configuration team**. It defines business rules for UTM-related field presentation in intake forms, value validation, and query string construction.

> **Terminology — Direct Media vs. Paid Direct:** The `uap Project Type` value **Direct Media** is the Workfront intake label for what analytics and this document call **Paid Direct** (`utm_medium=paid-direct`). Use **Direct Media** only when referring to the Workfront UI field; use **Paid Direct** for standard channel naming, reporting, and `utm_medium`.

---

## WF-1) Intake Form Automation Requirements by Project Type

These are the fields that must be displayed or automated when a channel project type is chosen for activation.

> **Note:** A visual representation of these business rules can be found [here](https://cisco-my.sharepoint.com/:x:/p/jbauerle/IQA6p-V-UVhtRbqX68M3MNwSAecRMoKysaqexetBBbCRU1E?e=yhly8C&nav=MTVfe0UxREEwMzkwLUFCOEUtNDY2MS1COEZCLTVBOUQ1NDZCNDU1Qn0).

### Workfront (UAP) Field Business Rules

#### 1. Project Type → Channel Type Automation

When a channel is selected in `uap Project Type`, automatically set the same value in `uap Channel Type`.

#### 2. Channel Type-Driven Field Display

When a value is selected in `uap Channel Type`, display the following fields:

| uap Channel Type | Channel Sub-Type Field | Channel Platform Field |
|---|---|---|
| Email | uap Email Type | uap Email Platform Type |
| Content Syndication | uap Content Syndication Type | uap Content Syndication Partner |
| Paid Direct | uap Ad Type | uap Trafficking Partner |
| Paid Social | uap Social Objective | uap Social Platform |
| Paid Search | uap Search Type | uap Search Engine |
| Paid Programmatic | uap Ad Type | uap Trafficking Partner |
| Organic Social | uap Social Objective | uap Social Platform |

---

#### 3. Programmatic Channel Type (`Programmatic Media`)

When `uap Channel Type` = **Paid Programmatic** (from the **Programmatic Media** project type):

- Display `uap Trafficking Partner` with the picklist **filtered to two visible values:** **DV360** and **YouTube**.
- **TradeDesk** remains in the underlying picklist for future use but must **not** be shown to users at this time.
- **Automate `utm_source` from the selection:**
  - **DV360** selected → emit literal `utm_source=dv360`
  - **YouTube** selected → emit literal `utm_source=youtube`
- Always append `utm_creative=%ecid!` for Paid Programmatic URLs (see [WF-3](#wf-3-query-string-construction-rules)).

---

## WF-2) Mapping Intake Values to UTMs

This section defines how values captured in Workfront intake fields map to UTM parameters:

- `uap Channel Type` → `utm_medium`
- Channel Platform field (e.g., `uap Email Platform Type`, `uap Content Syndication Partner`) → `utm_source`

> **Source of truth for Workfront execution:** ***Source and Mediums.xlsx*** — contains the full uap Project Type → `utm_medium` / platform → `utm_source` mapping and standard query string patterns. A SharePoint copy may also be maintained [here](https://cisco-my.sharepoint.com/:x:/p/jbauerle/IQA6p-V-UVhtRbqX68M3MNwSARzGFoziC33k9bukg9xgfi8?e=3hrnPW&nav=MTVfezhBOENFNUJCLUM0MDctNDE4RC1CQjE4LUEzNTU0NDdCOUFBQn0); if the two differ, **Source and Mediums.xlsx** wins.

### utm_medium Values

Auto-populated based on channel type (not a user-facing dropdown):

| uap Channel Type | utm_medium Value |
|---|---|
| Paid Direct | `paid-direct` |
| Paid Programmatic | `programmatic` |
| Paid Search | `cpc` |
| Paid Social | `paid-social` |
| Organic Social | `social` |
| Content Syndication | `syndication` |
| Ratings and Reviews | `ratings-reviews` |
| Email | `email` |
| Direct Mail | `direct-mail` |
| Web Referral | `web-referral` |

> **Note:** `web-referral` does not have a Workfront project type. It is used for manual URL builds only (Stensul, URL Builder) when linking from external web properties.

### utm_source Mapping Table

| uap Channel Type | uap Platform Type Field | Platform Value (Friendly) | utm_source Value |
|---|---|---|---|
| Email | uap Email Platform Type | Eloqua | `eloqua` |
| | | Gong | `gong` |
| | | Marketo | `marketo` |
| | | Outreach | `outreach` |
| | | Outlook | `outlook` |
| | | Salesforce | `salesforce` |
| Paid Direct | uap Trafficking Partner | Bloomberg | `bloomberg` |
| | | Business Insider | `businessinsider` |
| | | ExtremeTech | `extremetech` |
| | | Fierce | `fierce` |
| | | Foundry | `foundry` |
| | | International Security | `international-security` |
| | | Lifehacker | `lifehacker` |
| | | Light Reading | `light-reading` |
| | | Loss Prevention Magazine | `loss-prevention-magazine` |
| | | Mashable | `mashable` |
| | | Network Computing | `network-computing` |
| | | PCMag | `pcmag` |
| | | RCR Wireless | `rcr-wireless` |
| | | Register | `register` |
| | | SDX Central | `sdx-central` |
| | | Security Info Watch | `security-info-watch` |
| | | Security Magazine | `security-magazine` |
| | | Stack Overflow | `stack-overflow` |
| | | Stack Overflow Network | `stack-overflow-network` |
| | | Tech Brew | `tech-brew` |
| | | TechTarget | `techtarget` |
| | | VentureBeat | `venturebeat` |
| | | NFL | `nfl` |
| | | OOH | `ooh` |
| | | TV | `tv` |
| | | Female Quotient | `female-quotient` |
| | | Harvard Business Review | `hbr` |
| | | Technology Business Programming Network (TBPN) | `tbpn` |
| | | *Legacy (under review):* | |
| | | Avid | `avid` |
| | | BNP Media | `bnpmedia` |
| | | CNN Network | `cnnnetwork` |
| | | FedScoop.com | `fedscoop` |
| | | IDG Communications | `idgcommunications` |
| | | ITmedia Japan | `itmediajapan` |
| | | Morning Brew | `morning-brew` |
| | | Nikkei xtech JP | `nikkeixtechjp` |
| | | Other | `other` |
| | | Outbrain | `outbrain` |
| | | Posterscope (Airport) | `posterscope` |
| | | RCR Wireless 2 | `rcrwireless2` |
| | | Situation Publishing | `situationpublishing` |
| | | StateScoop | `statescoop` |
| | | Times of India | `timesofindia` |
| | | Washington Post | `washingtonpost` |
| | | ZDNet | `zdnet` |
| | | Ziff Davis | `ziffdavis` |
| Paid Programmatic | uap Trafficking Partner | DV360 | `dv360` |
| | | YouTube | `youtube` |
| | | TradeDesk *(future; hidden in UI today)* | `tradedesk` |
| Paid Social | uap Social Platform | Bluesky | `bluesky` |
| | | Facebook | `facebook` |
| | | Instagram | `instagram` |
| | | LinkedIn | `linkedin` |
| | | Meta | `meta` |
| | | Reddit | `reddit` |
| | | Weibo | `weibo` |
| | | X | `x` |
| | | Xing | `xing` |
| | | YouTube | `youtube` |
| Organic Social | uap Social Platform | Bluesky | `bluesky` |
| | | Facebook | `facebook` |
| | | Instagram | `instagram` |
| | | LinkedIn | `linkedin` |
| | | Meta | `meta` |
| | | Reddit | `reddit` |
| | | Weibo | `weibo` |
| | | X | `x` |
| | | Xing | `xing` |
| | | YouTube | `youtube` |
| Paid Search | uap Search Engine | Baidu | `baidu` |
| | | Bing | `bing` |
| | | Daum | `daum` |
| | | Google | `google` |
| | | Naver | `naver` |
| | | Sogou | `sogou` |
| | | Yahoo | `yahoo` |
| | | Yandex | `yandex` |
| Ratings and Reviews | uap Ratings and Review Platform | Capterra | `capterra` |
| | | G2 | `g2` |
| | | Gartner | `gartner` |
| | | GetApp | `getapp` |
| | | PeerSpot | `peerspot` |
| | | Software Advice | `software-advice` |
| | | TrustRadius | `trustradius` |
| Content Syndication | uap Content Syndication Partner | Activate | `activate` |
| | | AI-Tech Park | `ai-techpark` |
| | | Anteriad | `anteriad` |
| | | B2BIQ | `b2biq` |
| | | BlueWhale Research | `bluewhale-research` |
| | | BrightTalk | `brighttalk` |
| | | Bython | `bython` |
| | | Chronicle of Higher Education | `chronicle-highered` |
| | | DemandWorks | `demandworks` |
| | | Endeavor | `endeavor` |
| | | eRepublic | `erepublic` |
| | | Foundry | `foundry` |
| | | GovExec | `govexec` |
| | | GovLoop | `govloop` |
| | | Infuse | `infuse` |
| | | Interlink | `interlink` |
| | | Intentsify | `intentsify` |
| | | ISMG | `ismg` |
| | | Netline | `netline` |
| | | PeerSpot | `peerspot` |
| | | Pharosiq | `pharosiq` |
| | | TechnologyAdvice | `technologyadvice` |
| | | TechTarget | `techtarget` |
| | | TrustRadius | `trustradius` |

This table maps `uap Channel Type` → platform field → friendly value → standard `utm_source` value.

**Direct Mail (`utm_medium: direct-mail`):** No approved `utm_source` list exists yet. Users may populate vendor or partner as free text in `uap Direct Mail Platform` (mapped to `utm_source` using lowercase and hyphens) until standardized values are published.

---

## WF-3) Query String Construction Rules

### Minimum Required Parameters

Every tracking URL **must** include: `ccid` · `dtid` · `utm_id` · `utm_medium` · `utm_source`

`utm_creative` is required **only** for **Paid Direct**, **Paid Programmatic**, and **Paid Social** (value: `%ecid!`). All other channel types omit `utm_creative`.

### Format

With `utm_creative`:

```
[destination URL]?ccid=[value]&dtid=[value]&utm_id=[ccid value]&utm_medium=[value]&utm_source=[value]&utm_creative=%ecid!
```

Without `utm_creative`:

```
[destination URL]?ccid=[value]&dtid=[value]&utm_id=[ccid value]&utm_medium=[value]&utm_source=[value]
```

### Parameter Order

1. `ccid`
2. `dtid`
3. `utm_id` *(must equal `ccid` value)*
4. `utm_medium`
5. `utm_source`
6. `utm_creative` *(Paid Direct, Paid Programmatic, Paid Social only — value `%ecid!`)*

### Construction Rules

- Begin with `?` after the base URL.
- Separate each parameter with `&`.
- `utm_id` must always equal the `ccid` value.
- Include `utm_creative=%ecid!` only for **Paid Direct**, **Paid Programmatic**, and **Paid Social**; omit entirely for all other channel types.
- CM360 replaces the `%ecid!` macro with the creative ID on serve/click.
- All UTM values must be **lowercase** with **hyphens** replacing spaces.
- No spaces or special characters (`&`, `%`, `?`, `=`) in values.

### Channel Type Query String Reference

Canonical formats by `uap Channel Type` (substitute real values for placeholders; `URL` = destination):

| uap Channel Type | utm_medium | Query String Format |
|---|---|---|
| Paid Direct | `paid-direct` | `URL?ccid=[ccid]&dtid=[dtid]&utm_id=[ccid]&utm_medium=paid-direct&utm_source=[uap Trafficking Partner]&utm_creative=%ecid!` |
| Paid Programmatic | `programmatic` | `URL?ccid=[ccid]&dtid=[dtid]&utm_id=[ccid]&utm_medium=programmatic&utm_source=<automated>&utm_creative=%ecid!` — `utm_source` is automated from `uap Trafficking Partner`: `dv360` (DV360) or `youtube` (YouTube). |
| Paid Search | `cpc` | `URL?ccid=[ccid]&dtid=[dtid]&utm_id=[ccid]&utm_medium=cpc&utm_source=[uap Search Engine]` |
| Paid Social | `paid-social` | `URL?ccid=[ccid]&dtid=[dtid]&utm_id=[ccid]&utm_medium=paid-social&utm_source=[uap Social Platform]&utm_creative=%ecid!` |
| Organic Social | `social` | `URL?ccid=[ccid]&dtid=[dtid]&utm_id=[ccid]&utm_medium=social&utm_source=[uap Social Platform]` |
| Content Syndication | `syndication` | `URL?ccid=[ccid]&dtid=[dtid]&utm_id=[ccid]&utm_medium=syndication&utm_source=[uap Content Syndication Partner]` |
| Ratings and Reviews | `ratings-reviews` | `URL?ccid=[ccid]&dtid=[dtid]&utm_id=[ccid]&utm_medium=ratings-reviews&utm_source=[uap Ratings and Review Platform]` |
| Email | `email` | `URL?ccid=[ccid]&dtid=[dtid]&utm_id=[ccid]&utm_medium=email&utm_source=[uap Email Platform Type]` |
| Direct Mail | `direct-mail` | `URL?ccid=[ccid]&dtid=[dtid]&utm_id=[ccid]&utm_medium=direct-mail&utm_source=[uap Direct Mail Platform]` |

*Future TradeDesk programmatic:* When the picklist option is enabled, use the same Paid Programmatic structure with literal `utm_source=tradedesk` and `utm_creative=%ecid!`.
