---
date: 2026-04-14
title: "The pre-sale Strata Report"
summary: "A blunt guide to reading a pre-sale strata report with LLM help, including the prompt used to surface risks, omissions, and likely buyer exposure."
featured_image: "/blog/images/strata-report-buyers.png"
featured_image_alt: "A concerned couple looking at a pre-sale residential strata report in front of a modern apartment building."
---

Everyone says, quite rightly, before you buy into a strata you must obtain the strata report, even if you have to pay for it.  The wisdom is that, the strata report will provide all you need to make an informed decision about the maintenance of the buildings, its financial situation, and the (dis)harmony of your potential co-owners and neighbours.

Working against that are many forces which would prefer you execute the purchase without knowing any of those things.  The seller and their real estate agent would prefer you stay in the dark so you don't get cold feet and don't have any ammunition to soften your bid.  The Owners, generally, would prefer you not have a clear view for the same reason; they know that the price you pay will reflect on the valuation of their own unit.  Even the, supposedly independent, company offering the Strata Report doesn't really want you to discover any gremlins because they want more business from these Real Estate agents and don't want exposure to a lawsuit for putting people off.

Oddly enough, it's only the Strata Manager who doesn't care, or mildly inclined toward you having the full picture: merely so they don't have to listen to your outrage when the negatives become clear.  Sadly even that motive submits to the greater fear of irritating the hands that feed them, so they simply won't take your call.

So what good is the Strata Report?

Well they do have to include some hard information, or leave it out and put it on you to notice it's missing.  It's like those legal dramas where the cast spend an all-nighter going through all the boxes.  There's stuff in there, you just have to find it. But how?

Enter a modern solution: the LLM (or 'ChatGPT') has no skin in this game (yet) and no motivation to sugar coat it for you.  This is the best way I have discovered to 'read between the lines' of a 'strata report' and extract an objective view of the situation.

1. Get the strata report:
2. Feed the strata report into an LLM (ie ChatGPT, Claude, Copilot, Grok, llama, etc.) for evaluation.  

The extensive prompt below will generate a comprehensive assessment of the strata report.  You can copy/paste the prompt below into Claude (or your LLM of choice), and attach the strata report file, then type your own prompt simply stating something like `The address is "99 Baker St Cronulla NSW" and the unit number is "6"`.  

The output is insightful and comprehensive but, of course, not as authoritative as it purports... consider what it says with your own judgement and grains of salt.

I thought about setting this up as a "buy me a coffee service".  At first the LLM excitedly told me this was worth $60-$200 per report and to take it beyond coffee.  But then I asked about risks and it told me, yeah, it wasn't worth a lawsuit. 😊

{{< copy-prompt >}}
# PRE-PURCHASE STRATA ANALYSIS PROMPT — NSW AUSTRALIA

You are an expert strata lawyer and building inspector with 20 years experience reviewing pre-purchase strata reports in New South Wales, Australia. You have deep expertise in the Strata Schemes Management Act 2015 (NSW), NCAT proceedings, building remediation, capital works planning, and the financial analysis of owners corporations.

Analyze the uploaded documents for a buyer considering purchasing [UNIT/LOT NUMBER] at [ADDRESS].

Cross-reference every available document — strata reports, by-laws, AGM and committee minutes, financial statements, building inspection reports, legal correspondence, engineering reports, contractor proposals, insurance records, fire safety documents, and any other scheme records — to construct a complete picture of what a buyer is actually walking into.

## DOCUMENT HANDLING

Before beginning the analysis, read every uploaded document. As you do:

- **Exclude irrelevant pages.** Strata reports sometimes contain misfiled pages from a different strata plan, duplicate pages, or documents unrelated to the subject building or lot. Disregard these. If an entire document appears to relate to a different scheme, note it in the document inventory and exclude it from the analysis.
- **Note the date, author, and type of each document.** You will list these in the document inventory immediately after the executive summary.

## LENGTH AND DENSITY

Keep the report concise. The target is a report that can be read in 15–20 minutes. Apply these principles throughout:

- Lead with conclusions, follow with evidence. Do not narrate the process of reading documents.
- Combine related findings. If the same issue appears in multiple documents, synthesise it once and cite all sources — do not repeat the finding per document.
- Use tables for structured comparisons (financials, timelines, risk itemisation). Use prose only where narrative context is needed.
- Omit generic strata advice that applies to any building. Every sentence should be specific to this scheme, this building, or this lot.
- If a section has no material findings (e.g. no hazardous materials identified), say so in one sentence and move on.

---

## REPORT STRUCTURE

The report must contain the following sections in this order:

### EXECUTIVE SUMMARY

One page maximum. Written for a non-expert reader — no jargon, no acronyms without explanation, no legal citations. Contains:

- The overall risk score and its plain-language interpretation
- The three most critical findings, each in 2–3 sentences
- The estimated total financial exposure as a single dollar range
- A forward-looking statement: what this building will look like in 12–24 months on current trajectory
- A clear statement of whether this scheme is in good health, under stress, or in crisis

A buyer who reads only this summary and the final recommendation should have a complete decision framework.

### DOCUMENT INVENTORY

A table listing every document provided, sorted by date (oldest first), with columns:

| Date | Document | Author/Source | Relevance |
|---|---|---|---|
| e.g. 22 Jan 2020 | Building Remediation Report | Sass&Co Constructions | Core — building defects |
| e.g. 29 Jun 2023 | Pre-Purchase Strata Report | Lancelot Strata Reports | Core — scheme overview |

For any document excluded as irrelevant (wrong strata plan, duplicate, or unrelated), include it in the table with a brief note in the Relevance column explaining why it was excluded.

### 1. RISK SCORE (0–100)

Score across these weighted domains with a one-line rationale per domain:

- Structural and building condition (25%)
- Financial exposure including pending/probable special levies (25%)
- Hazardous materials (10%)
- Governance, management stability, and owner relations (15%)
- Unit-specific defects and liabilities (10%)
- Omissions and gaps in the records (15%)

### 2. PHYSICAL CONDITION

Cover building-wide and lot-specific issues:

- Structural defects (concrete, waterproofing, roofing, facades, drainage, glazing, services)
- Building age, construction type, environmental exposure, and deterioration trajectory
- Status of any remediation works — contracted, in progress, completed, or stalled
- Hazardous materials — location, risk level, whether a register/management plan exists
- Lot-specific defects from any source document

Note the age and limitations of each building report relied upon.

### 3. FINANCIAL POSITION

Quantify the buyer's exposure:

- Fund balances (flag deficits)
- Current levy amounts for the specific lot
- Special levy history — amounts, dates, purposes, any that were voted down
- Loan proposals — approved or rejected
- Capital works fund plan — date, adequacy, s80 SSMA compliance
- Upcoming special levy exposure (estimated total and per-unit share, in low/mid/high scenarios)
- Insurance status and any restrictions
- Expenditure patterns (3–5 years) with unusual or escalating items
- Contractor quotes or tender amounts sighted

### 4. GOVERNANCE AND RELATIONSHIPS

- Strata manager turnover (how many, how often, why)
- Committee composition and representation gaps
- Owner–committee–manager conflict indicators
- Evidence of resistance to spending or blocking necessary works
- Active or threatened disputes
- Overall governance health assessment

### 5. OMISSIONS AND GAPS

List what is missing and why each gap matters. Prioritise by materiality — lead with the gaps that most affect the buyer's risk assessment.

### 6. QUESTIONS FOR THE VENDOR

Up to 8 specific questions targeting critical gaps, risks, or ambiguities. Each should require a factual, verifiable answer and specify documentary evidence where relevant.

### 7. PURCHASE RECOMMENDATION AND PRICE GUIDANCE

**Market Price Estimate (Before Strata Analysis):**
Estimate what this unit would sell for if the building were well-maintained with no material strata issues, based on comparable sales, local market data, and stated assumptions about the unit (size, bedrooms, parking, views — state what is assumed vs what is known from the documents).

**Strata-Adjusted Valuation:**
Itemise every material risk as a dollar adjustment in a table:

| Risk Item | Adjustment | Certainty |
|---|---|---|
| e.g. Concrete remediation levy share | -$80K to -$170K | Probable |

Sum into a total discount range. Subtract from market price to produce a strata-adjusted valuation range.

**Recommendation:**
State one of:

- **BUY** at the strata-adjusted price or below, with reasoning.
- **BUY WITH CAUTION** only if specific listed conditions are met.
- **DO NOT BUY** with reasoning.

Be direct. Do not substitute "seek professional advice" for a position.

### SOURCES

List every online reference (URL, title, date accessed) used to support the analysis — for example, comparable sales data, legislative references, or market information. If no online sources were used, state that the analysis was based entirely on the uploaded documents.

---

## OUTPUT REQUIREMENTS

- Every claim must trace to a specific uploaded document (cited by name and date) or to a listed online source.
- Where documents conflict or contain inconsistencies, flag them.
- The executive summary appears first. The purchase recommendation appears last. A reader should be able to read only those two sections and have a complete decision framework.
{{< /copy-prompt >}}

The output will depend entirely on your LLM model, but might look something like this.

{{% sample-output %}}
# PRE-PURCHASE STRATA ANALYSIS REPORT
## Lot 6 – Strata Plan 10881

---

## EXECUTIVE SUMMARY

**Overall Risk Score: 62/100 — Under Stress**

This six-unit brick residential building presents a **moderately elevated risk profile** driven by identified asbestos hazards, aging infrastructure requiring remediation, and structural settlement patterns. The scheme finances are stable but tight, with limited reserves relative to anticipated capital expenditure. The building is functionally sound but shows its age (circa 1940s construction) and requires attention to remedial works over the next 12–24 months.

**Three Critical Findings:**

1. **Asbestos in Entry Doors.** Quotations from Aquafire Protection (December 2009) confirm asbestos-laden doors in Units 3, 4, and 6. Replacement costs total $2,805 (inc. GST). This is a material but contained liability—identified, quantified, and addressable through standard remedial protocols.

2. **Deferred Structural and Safety Works.** The 2008 Building Inspection Report identified multiple items including pathways with uneven surfaces presenting tripping hazards, loose railings, electrical safety switch upgrades, and fire stair deficiencies. As of April 2010, no evidence indicates completion. These works are necessary for building compliance and tenant safety.

3. **Sinking Fund Underfunding Risk.** The 2006 10-year sinking fund projection (Solutions IE) shows an accumulated deficit trajectory. Contributions have been inadequate historically to fund anticipated major replacements. The current balance ($21,434.71 as of April 2010) covers imminent needs but leaves minimal buffer for unbudgeted expenditure.

**Estimated Financial Exposure:** $35,000–$75,000 (aggregated strata-wide) over the next 24 months. Lot 6's proportional share (1/6 of entitlement) approximately $5,800–$12,500.

**Forward Trajectory (12–24 months):** Without immediate action, the building will face escalating maintenance costs, potential safety compliance issues, and a special levy to fund outstanding deferred works. Active governance and spending discipline are required to stabilise finances and address remedial backlog.

**Scheme Health Assessment:** Under stress—financially stable in the immediate term but structurally dependent on committed capital works and owner compliance with levy obligations.

---

## DOCUMENT INVENTORY

| Date | Document | Author/Source | Relevance |
|---|---|---|---|
| 28 Apr 2010 | Strata Records Inspection Report (Summary Page) | CP Reports Pty Ltd | Core — scheme overview, financial position, compliance status |
| 27 Apr 2010 | Strata Records Inspection — Full Report | CP Reports Pty Ltd | Core — comprehensive record examination, insurance, governance, maintenance |
| 29 Jun 2009 | AGM Minutes (Strata Plan 5714) | Robinson Strata Management / Mason & Brophy | Governance — note: this plan number differs from subject (10881); **excluded as irrelevant** |
| 7 Sep 2009 | AGM Minutes (Strata Plan 5714) | Mason & Brophy Strata Management | Governance — note: plan 5714, not 10881; **excluded as irrelevant** |
| 10 Sep 2009 | EGM Minutes (Strata Plan 10881) | Robinson Strata Management | Core — governance, resolutions on security intercom, painting, carpeting |
| 29 Jun 2009 | EC Meeting Minutes (Strata Plan 10881) | Robinson Strata Management | Core — governance, maintenance decisions |
| 20 Apr 2010 | Balance Sheet (Strata Plan 5714) | Solutions IE/Robinson Strata Management | **Excluded — plan 5714, not 10881** |
| 1 Aug 2009–20 Apr 2010 | Statement of Income & Expenditure (Strata Plan 5714) | Solutions IE/Robinson Strata Management | **Excluded — plan 5714, not 10881** |
| 1 Aug 2008–31 Jul 2009 | Statement of Financial Performance (Strata Plan 5714) | Solutions IE/Robinson Strata Management | **Excluded — plan 5714, not 10881** |
| 23 Apr 2010 | Balance Sheet (Strata Plan 10881) | Robinson Strata Management | Core — financial position, fund balances |
| 1 Jun 2009–23 Apr 2010 | Income & Expenditure Statement — Admin Fund (SP 10881) | Robinson Strata Management | Core — expenditure patterns, levy adequacy |
| 1 Jun 2005–23 Apr 2010 | Income & Expenditure Statement — Sinking Fund (SP 10881) | Robinson Strata Management | Core — sinking fund trend, major expenditures |
| 01/08/2008–31/07/2009 | Financial Performance Statement (SP 10881) | Robinson Strata Management | Core — year-on-year comparison, admin & sinking fund |
| 1 May 2006 | 10-Year Sinking Fund Management Outline (SP 10881) | Solutions IE Pty Ltd | Core — capital works forecast, fund adequacy analysis |
| 01/09/2009 | Proposed Budget (SP 10881) | Robinson Strata Management | Core — forward levy estimates, revenue projections |
| 16 Dec 2009 | Asbestos Testing & Quotation (Units 3, 4, 6) | Aquafire Protection | Core — hazardous materials identification, remediation cost |
| 9 Aug 2008 | Building Inspection Report (SP 10881) | Brainwaves Building Services (Richard Meth) | Core — structural condition, safety issues, maintenance recommendations |
| July 2008 | OH&S Report (Section 1 — Safety Summary) | Solutions IE Pty Ltd | Core — electrical and safety compliance findings |

**Note:** Documents referencing Strata Plan 5714 (various balance sheets and financial statements dated prior to June 2009) have been excluded from analysis as they relate to a different strata scheme and are not relevant to the subject property (Strata Plan 10881).

---

## 1. RISK SCORE (0–100)

**Overall Score: 62/100**

| Domain | Weight | Score | Rationale |
|---|---|---|---|
| Structural & Building Condition | 25% | 65 | Building circa 1940s, sound basic structure but multiple deferred safety & remedial items identified in 2008 report. Minor settlement cracks typical for age. Asbestos identified in doors (contained, addressable). No major structural defects but maintenance backlog evident. |
| Financial Exposure & Special Levies | 25% | 55 | Sinking fund inadequately funded relative to 10-year projection. Current administration fund healthy ($3,656.68) but tight. Sinking fund ($21,434.71) insufficient for imminent major works. No current special levy, but risk of one is moderate-to-high within 24 months. |
| Hazardous Materials | 10% | 70 | Asbestos in three door frames identified and quantified ($2,805 total replacement). No other hazardous materials flagged. Scope is limited and manageable; however, no evidence of management plan or completion timeline. |
| Governance & Management | 15% | 60 | Strata manager (Robinson Strata Management) in place since 2002; professionally licensed. Executive committee active and meeting regularly. Some resistance noted to spending (security intercom, stairwell works) but ultimately resolutions passed. No litigation evident. Records maintained. Minor communication gaps (no evidence of sinking fund forecast disseminated to owners). |
| Unit-Specific Defects | 10% | 58 | Unit 6 shows typical minor cracking, patched plasterwork, worn wall finishes. Cracked shower screen noted. No structural issues specific to Unit 6; condition consistent with building age. Asbestos door replacement required ($935 estimated cost for Unit 6). |
| Omissions & Gaps in Records | 15% | 50 | Title deed not made available; drainage diagram not on file; no pest inspection records; no annual fire safety statement filed; occupational health & safety inspection dated July 2008 (now 2 years old); no recent valuation; capital works plan not updated since 2006. Key missing: evidence of completion of 2008 remedial works and current compliance status. |

---

## 2. PHYSICAL CONDITION

**Building Overview:**  
Three-storey brick and tile block residential building constructed circa 1940s, known as "Radford House." Original timber windows partially replaced with Colorbond. Six units arranged vertically. Brick and mortar construction with concrete floor paths. Laundry facilities in common area (rear, locked).

**Age & Deterioration Trajectory:**  
At approximately 70 years old, the building displays typical age-related wear: worn brick mortar joints, minor settlement cracking, evidence of past patching and repainting, and gradually failing original services. The 2008 Brainwaves Building Inspection Report (dated 9 August 2008) notes the structure remains in "good order" with "various minor settlement cracks and worn mortar joints" typical for a building of this type and age. No major structural defects identified. However, deferred maintenance is evident, particularly in common areas and fire safety infrastructure.

### Structural Defects

**Cracking & Settlement:**  
- Multiple fine subsidence cracks identified in front brick fence and concrete paths
- Cracked terrazzo entry doorsill (north side)
- Worn brick joints on street-facing and rear elevations, especially around entry gates, windows, and plumbing penetrations
- Minor crack under front window of Unit 1 (approx. 300mm × 0.05mm)
- Pathways show minor settlement cracks; crack under fire stairs noted at approximately 4mm width in concrete path
- **Assessment:** Consistent with normal settlement and age. No evidence of active structural movement or foundation failure. Cracks are cosmetic or routine maintenance-level.

**Waterproofing & Moisture:**  
- Worn mortar joints in exterior brick especially near water sources (laundry door, gates, plumbing)
- Some patched mortar work noted (Unit 2 north wall shows grey mortar patches over white original)
- Cracked laundry door sill (photo 13)
- Colorbond gutters noted as "fair" condition with some corrosion
- Minor gaps around plumbing pipes to brickwork
- **Assessment:** Weathering is present but managed. No evidence of widespread water ingress or dampness documented. Routine gutter and joint maintenance required.

**Roofing:**  
- Report states "Does the building have a flat roof?" — response: "Unable to determine"
- Building visually appears to have pitched tile roof (1940s original or replacement)
- **Assessment:** Roof type uncertain from documents; no defects reported in inspection.

### Hazardous Materials

**Asbestos:**  
Quotation from Aquafire Protection dated 16 December 2009 (Reference 19516) confirms asbestos testing of entry doors in Units 3, 4, and 6. Report states: "Asbestos is exposed through a hole where the dead latch was replaced which requires the door to be replaced."

| Unit | Scope | Cost (inc. GST) |
|---|---|---|
| Unit 3 | 2hr Mini Fire Door with Hardware | $935.00 |
| Unit 4 | 2hr Mini Fire Door with Hardware | $935.00 |
| Unit 6 | 2hr Mini Fire Door with Hardware | $935.00 |
| **Total** | | **$2,805.00** |

Quote valid 30 days from issue (expired by April 2010 inspection). No evidence of completion in available documents. This is the sole hazardous material identified. Scope is limited and cost is quantified. No other asbestos, lead paint, or other regulated materials flagged in any inspection.

**Assessment:** Asbestos is confined to three door frames. Health risk during occupancy is minimal (asbestos is encapsulated in door material). Replacement is standard building remediation, not a structural emergency. However, delay increases liability risk and may violate occupational health and safety obligations if the holes remain unrepaired.

### Lot-Specific Defects (Unit 6)

From Brainwaves Building Services report (Sections Unit 6):

- **Lounge:** Patched hairline crack under window, very fine
- **Kitchen:** Patched hairline crack over window to cornice, very fine; wall cornice to wall cracks (multiple fine); patched crack on north wall between doorways, very fine
- **Bedroom:** Patched fine north wall crack below window to floor; dummy plaster noted
- **Sunroom:** In good order
- **Bathroom:** Fine wall crack in south wall over wall cabinet door (approx. 400mm × 1mm); some dummy areas; paint cracks over wall tiles

**Unit-Specific Assessment:**  
Unit 6 shows cosmetic wear typical of a 70-year-old building. No structural issues unique to this lot. Cracking is minor, patched, and hairline—consistent with building settlement and age. The asbestos door requires replacement (quantified at $935 inc. GST).

### Building Maintenance Status

**Deferred Works Identified in 2008 Inspection (Brainwaves Building Services, 9 Aug 2008):**

The Initial Safety Report / Inspection Summary (Section 1 of OH&S report, Solutions IE, July 2008) lists 8 specific action items:

1. **Pathway Trip Hazard:** "Please grind back at approximately 45 degrees the lip along the cracks on the pathway to the laundry as soon as possible as the variation in height currently represents a moderate tripping hazard." — *Status: No evidence of completion.*

2. **Electrical Main Switch:** "Please ensure the main switch is clearly marked with appropriate signage stating 'MAIN SWITCH' as soon as possible as this represents a minor electrical hazard." — *Status: Unknown.*

3. **Power Circuit RCD Protection:** "Please ensure all community power circuits with socket outlets are protected by a Safety Switch (RCD) including outlets identified elsewhere in this report, as soon as possible." — *Status: No evidence of completion.*

4. **Community Light Circuit RCD:** "Please ensure all community light circuits are protected by a Safety Switch (RCD) including outlets identified elsewhere in this report, as soon as possible." — *Status: No evidence of completion.*

5. **Power Safety Switch Testing:** "Please ensure after installation of power Safety Switches that two-yearly tests of the Safety Switches (RCDs) are carried out by a competent electrician and records of these checks are kept onsite." — *Status: Dependent on item 3.*

6. **Lighting Safety Switch Testing:** "Please ensure after installation of lighting Safety Switches that two-yearly tests of the Safety Switches (RCDs) are carried out by a competent electrician and records of these checks are kept onsite." — *Status: Dependent on item 4.*

7. **Switchboard Inspection:** "Please ensure the switchboards are inspected and tested at least every 2 years by qualified electrician and suitable records of the test date are kept on site (Sec 8: AS/NZ 3000:2007)." — *Status: Unknown.*

8. **Loose Railings/Palings:** "Please ensure loose palings / rails / posts are secured as soon as possible as this represents a moderate security / personal injury hazard." — *Status: No evidence of completion.*

**Executive Committee Resolutions (June 2009 AGM, Extraordinary General Meeting 10 September 2009, EC Meeting 29 June 2009):**

Resolution from EGM 10 September 2009 indicates:
- **Security Intercom:** "The Owners Corporation specially resolved not to accept one of the quotations submitted" for security intercom access system. *Status: Not proceeding.*
- **Painting Stairwell:** "The matter was not resolved as there was no clear majority vote for or against the quotations submitted." *Status: Unresolved.*
- **Recarpeting Stairwell:** "The matter was not resolved as there was no clear majority vote for or against the quotations submitted." *Status: Unresolved.*

A resolution (EC Meeting 4 January 2010, extracted from minutes page 21) authorised:
- **Stairwell Repainting:** Accept quotation from Argyle Painters for $3,410
- **Stairwell Carpet Replacement:** Accept quotation from Baigowlah Carpet Choice for carpet and labour

**Assessment of Deferred Works:**  
As of April 2010 (inspection date), critical electrical and safety remediation identified in the 2008 OH&S report remain incomplete. Stairwell works (repainting and carpeting) were approved in January 2010 but no evidence confirms execution. The pathway trip hazard, loose railings, and RCD installations are outstanding. These items are compliance-level, not cosmetic, and their non-completion represents potential liability exposure for the owners corporation and occupational health and safety risk.

**Major Maintenance Expenditure (Recent Years):**

From income & expenditure statements (Robinson Strata Management, to 23 Apr 2010, SP 10881):

- **Painting (Interior Stairwell):** $3,410.00 (Sinking Fund, year to 31 May 2009)
- **Concrete Spalling:** $1,782.00 (Sinking Fund, year to 31 May 2009)
- **General Replacement (Sinking):** $4,526.90 (budgeted, year to 31 May 2009)
- **Painting, Exterior:** $9,300.00 (Sinking Fund, actual expenditure Aug 2009–Apr 2010)
- **Balcony/Balustraders:** $1,980.00 (Sinking Fund, year to 31 May 2009)

**Assessment:** The scheme has undertaken exterior painting (recent, $9,300) and is funding stairwell works. However, electrical compliance and pathway safety remediation remain deferred.

---

## 3. FINANCIAL POSITION

### Fund Balances (as at 23 April 2010, Robinson Strata Management)

| Fund | Balance |
|---|---|
| **Administration Fund** | $3,656.68 |
| **Sinking Fund** | $21,434.71 |
| **Total Owners Corporation Funds** | **$25,091.39** |

**Composition of Assets:**

| Asset | Amount |
|---|---|
| Cash at Bank — Admin | $3,007.81 |
| Cash at Bank — Sinking | $235.19 |
| Levies in Arrears — Admin | $40.70 |
| Levies in Arrears — Sinking | $10.19 |
| Sinking Investment Account | $4,844.19 |
| Sinking Fund Investment Interest | $16,355.33 |
| Owner Invoices Receivable — Admin | $608.17 |
| **Total Assets** | **$25,101.58** |

**Liabilities:**

| Item | Amount |
|---|---|
| PAYG Clearing Account | $0.00 |
| Creditors | $59.80 |
| Levies in Advance | $0.00 |
| **Total Liabilities** | **$59.80** |

**Net Assets (Owners' Funds):** $25,041.78

### Current Levy Amounts (as at April 2010)

| Fund | Per Quarter | Annual |
|---|---|---|
| **Administration Fund** | $522.00 | $2,088 (estimated) |
| **Sinking Fund** | $201.86 | $807.44 (estimated) |
| **Total Quarterly Levy for Unit 6** | **$723.86** | **~$2,895** |

Unit 6 entitlement: 150 units of 1,000 aggregate entitlement (15% share).

**Arrears Status:** The CP Reports inspection (27 Apr 2010) confirms: "Arrears for the subject lot ... **Nil**" and "Arrears for the complex ... **$884**" (other units only).

### Special Levy History

**CP Reports Summary (27 Apr 2010):**
- Current Special Levies: **Nil Noted**
- Proposed Special Levies: **Nil Noted**

No evidence in 3-year period prior to April 2010 of struck or proposed special levies.

### Capital Works Fund Plan

**10-Year Sinking Fund Management Outline (Solutions IE, 1 May 2006):**

Projected fund balances and expenditures:

| Year End | Opening Balance | Total Contributions | Anticipated Expenses | Closing Balance |
|---|---|---|---|---|
| 31/05/2007 | $10,000.00 | $4,650.00 | $0.00 | $14,995.10 |
| 31/05/2008 | $14,995.10 | $4,882.50 | $14,969.30 | $5,396.51 |
| 31/05/2009 | $5,396.51 | $5,126.63 | $3,210.48 | $7,535.53 |
| 31/05/2010 | $7,535.53 | $5,382.96 | $7,496.58 | $5,708.25 |
| 31/05/2011 | $5,708.25 | $5,652.10 | $1,865.07 | $9,734.24 |
| 31/05/2012 | $9,734.24 | $5,934.71 | $1,500.91 | $14,523.69 |
| 31/05/2013 | $14,523.69 | $6,231.44 | $0.00 | $21,249.04 |
| 31/05/2014 | $21,249.04 | $6,543.02 | $1,812.35 | $26,666.29 |
| 31/05/2015 | $26,666.29 | $6,870.17 | $0.00 | $34,379.29 |
| 31/05/2016 | $34,379.29 | $7,213.68 | $28,235.91 | $14,420.67 |

**Note:** Projection includes interest earned and GST provision. Anticipated expenses include general replacement, fire safety fittings, fence maintenance, and landscaping. Key assumption: annual contributions indexed at 7.5%.

**Status of Plan:** The 2006 projection provides a framework but was not formally updated or revalidated as of April 2010. Given that actual expenditure (exterior painting $9,300 in 2009–2010) materially exceeded budget, the projection's accuracy is questionable. The plan is outdated and does not reflect recent spending patterns.

**Assessment of Fund Adequacy:**

The sinking fund as at April 2010 ($21,434.71) sits within the 10-year projection but is below optimal levels for a six-unit scheme with identified deferred maintenance. The projection assumed steady contribution indexation, but actual sinking fund levies have remained static or modest. The $2,805 asbestos door replacement, the $3,410 stairwell painting, and outstanding electrical/safety remediation (estimated $3,000–$5,000 to complete) create immediate pressure. Without a special levy, the scheme relies on sinking fund accumulation, which is slow relative to identified needs.

**Section 80 Compliance (Strata Schemes Management Act 1996):**  
The CP Reports inspection states: "Has a Sinking Fund analysis been carried out? **Yes, extract attached**" — referring to the 2006 Solutions IE plan. However, the plan is now 4 years old (as of inspection), and no evidence of an updated s80 assessment is provided. Under current NSW legislation (Strata Schemes Management Act 2015 or its 1996 predecessor as applicable), a sinking fund plan or capital works plan must be kept current. This is a governance gap.

### Insurance

**Building Insurance (QBE, Policy 798572):**
- **Premium:** $3,628.26 (date due: 01/09/2010)
- **Sum Insured:** $2,835,000
- **Excess:** $100 all claims
- **Valuation Basis:** $2,250,000 (James Spinks valuation, 28 June 2006) — **now 4 years old**
- **Common Contents Covered:** $28,000

**Additional Covers:**
- Public Liability: $20,000,000
- Personal Accident: $100,000/$1,000 per week
- Office Bearers: $500,000
- Other Policies: Loss of Rent, Fidelity Guarantee, Government Audit/Legal, Appeals/Fixtures

**Claims History:** CP Reports confirms "Have there been any insurance claims exceeding $2,000.00 in the past two years? **No**"

**Notes:** Valuation is dated 2006; a current valuation may be warranted given building age and market movements. The sum insured ($2,835,000) exceeds the valuation basis, which is conservative and appropriate. No issues flagged regarding insurance adequacy or restrictions.

### Expenditure Patterns (Three Years)

**Administrative Fund Expenditure (Year to 31 May 2009, Robinson Strata Management):**

| Item | Amount | Comment |
|---|---|---|
| Accounting | $95.00 | |
| Electricity | $234.45 | |
| Grounds Maintenance — Contracts | $3,967.00 | Major item |
| Insurance Claims/Misc | $826.10 | |
| Insurance Premiums | $139.70 | |
| Legal Fees | $427.98 | |
| Pest Control | $165.00 | |
| Postage, Stationery, Printing | $438.50 | |
| Repairs & Maintenance — General | $2,151.95 | |
| Standard Management Fees | $1,639.20 | |
| Water | $248.50 | |
| **Total Admin Expenditure** | **$13,354.00** | Annual run rate ~$13,000–$14,000 |
| **Total Admin Revenue** | $14,521.41 | Levies $13,546.20 + interest/arrears |
| **Surplus** | $1,167.41 | Modest positive balance |

**Sinking Fund Expenditure (Year to 31 May 2009, Robinson Strata Management):**

| Item | Amount |
|---|---|
| Company Income Tax — Sinking | $98.70 |
| General Replacement | $4,526.90 |
| Painting | $3,410.00 |
| **Total Sinking Expenditure** | **$8,036.20** |
| **Sinking Fund Revenue** | $5,723.12 (levies + interest) |
| **Deficit for Period** | $(2,313.08) |

**Year to 31 May 2009 (Previous Year):**  
- Sinking expenditure was materially higher: $15,654.90 (notably balcony/balustraders $1,980, concrete spalling $1,782, doors $0, garage doors $11,490)
- The $11,490 garage door expenditure in 2008–09 is a one-off major item not repeated in subsequent year

**Year to 31 Aug 2009 (Statement of Financial Performance, period 01/08/08–31/07/09):**  
- Sinking fund opening balance: $33,863.77
- Income: $10,095.52
- Expenditure: $15,654.90 (including concrete spalling $1,782, balcony balustraders $1,980, garage doors $11,490, TV antenna $2,650)
- Closing balance: $28,304.39

**Assessment:** Expenditure is episodic rather than smooth. Major items (garage doors $11,490 in 2008–09, exterior painting $9,300 in 2009–10) drive volatility. Administrative fund is stable and in surplus most years. Sinking fund has been in deficit in some periods due to lumpy capital expenditure. Ongoing contributions are insufficient to fund major works without accumulating reserves over several years or striking a special levy.

---

## 4. GOVERNANCE AND RELATIONSHIPS

### Strata Manager

**Robinson Strata Management**  
- **License Number:** 307576
- **Manager on Record:** Mr. John Jocumsen
- **Address:** Level 1, 48 Lawrence Street, Harford NSW 2096
- **Phone:** (02) 9907 5050
- **Date Appointed:** 15/08/2002 (approximately 8 years as of April 2010)
- **Appointment by Instrument:** Yes
- **Specialised Strata Manager:** Yes

**Assessment:** Manager is professionally licensed, has been in role for 8 years (establishing continuity), and is noted as specialised. No turnover issues or complaints evident in available documents.

### Committee Composition (as at April 2010)

**Executive Committee Members (4):**
1. **Ms. Janaya Killworth** — Chairman (Unit lot unknown, exact unit not specified in available documents)
2. **Mr. Dane Swaney** — Secretary/Building Representative (Unit lot unknown)
3. **Miss Amanda Belcastro** — Treasurer (noted as co-owner of Unit 6 with Mr. Robert Alexander Walton; current lessees per strata roll are Calum Wilson & Vanja Tcherneva)
4. **Mr. D Robinson** (Unit lot: presumed U9 based on AGM minutes)

**Note:** The 2009 AGM minutes (29 Jul 2009, different strata plan 5714) show different composition; the April 2010 report references EC members for Plan 10881 (our subject). Cross-referencing is complicated by the inclusion of minutes from the wrong strata plan in the uploaded documents. Based on the EC Meeting of 29 June 2009 (for Plan 10881), the EC comprised Ms. J. Killworth, Mr. D. Swaney, and Miss A. Belcastro, with roles assigned at that meeting.

**Attendance & Quorum:** Minutes from 10 September 2009 EGM note "Owners Present: Nil / Present by Proxy: [multiple]" but attendance is sparse. Quorum is marginal, suggesting limited owner engagement.

### Owner–Committee–Manager Relationships

**Indicators of Conflict or Resistance:**

1. **Security Intercom System (Sep 2009 EGM):** Quotation for intercom system was submitted and discussed. Resolution: "The Owners Corporation specially resolved not to accept one of the quotations submitted." Indicates cost sensitivity or disagreement on priority.

2. **Stairwell Painting & Recarpeting (Sep 2009 EGM):** Two separate resolutions: "The matter was not resolved as there was no clear majority vote for or against the quotations submitted." Both items deferred pending further decision.

3. **January 2010 EC Resolution:** Subsequent to the unresolved items, the EC authorised stairwell painting ($3,410, Argyle Painters) and carpet replacement (Baigowlah Carpet Choice). This suggests the committee eventually moved forward but took several months to resolve.

**Assessment:** There is evidence of cost/priority friction among owners, but no litigation, legal disputes, or manager complaints are flagged. Decisions are ultimately reached, albeit sometimes slowly. This is a governance culture of caution rather than crisis.

### Notices and Orders

**CP Reports Inspection Summary (27 Apr 2010):**
- "There is no evidence of any current Applications, Notices or Orders lodged by or against the Owners Corporation." — Confirmed for both NCAT and Supreme Court.

**Assessment:** No active disputes or tribunal proceedings.

### Records Maintenance

**CP Reports Inspection (27 Apr 2010):**
- "Are Owners Corporation Books and Records maintained correctly? **Yes**"
- "Are they retained for the prescribed period? **Yes**"
- Current Tax statement lodged: **Not sighted**
- Current BAS statement lodged: **Not sighted**
- Tax File Number: **085 912 846**
- ABN: **98 630 683 734**
- Strata Roll: Maintained correctly in database format
- Minutes: Kept and maintained for the prescribed period. First AGM: "Not on file"

**Assessment:** Records are maintained but tax compliance documentation (current tax statement and BAS) are not sighted during inspection. Minor gap but not critical.

### Overall Governance Health

**Summary:** The scheme has a professionally managed strata manager with continuity, a functioning executive committee, and engaged (if cautious) owners. There is no evidence of serious conflict, litigation, or administrative failure. However, decision-making is deliberate and cost-conscious, sometimes to the point of deferring necessary works. Owners prioritise cost control over accelerated capital spending, which constrains fund accumulation and defers remedial works. This is a stable but conservative governance environment.

---

## 5. OMISSIONS AND GAPS

| Gap | Materiality | Why It Matters |
|---|---|---|
| **Title Deed / Certificate of Title** | High | CP Reports notes: "The Title Deed for the common property was not made available for inspection and the whereabouts of same is not known. Under computerisation the reference to title is now CP/SP10881." This is concerning. A buyer should independently verify the title via NSW Land Registry. The missing physical deed is not necessarily problematic if digital records are sound, but the phrasing suggests uncertainty. |
| **Updated Capital Works Plan (Section 80 Compliance)** | High | The 10-year sinking fund plan (Solutions IE, May 2006) is 4 years old and has not been formally revalidated as of April 2010. The 1996 Strata Schemes Management Act (and subsequent 2015 Act) require a current capital works plan. This is a compliance gap. Updated plan is needed to justify current levy adequacy and forecast special levy risk. |
| **Completion of 2008 Building Safety Items** | High | Eight critical items identified in the July 2008 OH&S report (electrical RCD installation, pathway trip hazard, loose railings, switchboard testing) remain unresolved as of April 2010. No evidence of completion or timeline. This creates potential occupational health and safety liability and non-compliance with standards. |
| **Asbestos Door Replacement Status** | Medium | Aquafire quotation (Dec 2009, $2,805 total) expired 30 days from issue. No evidence the work has been ordered or completed. Holes in doors (where asbestos is exposed) remain a minor hazard. Timeline for remediation is unclear. |
| **Drainage Diagram** | Medium | "A drainage diagram for the subject property was not on file." Relevant for understanding common property responsibilities and identifying potential blockage or repair liability. Not critical but useful for future maintenance. |
| **Pest Inspection Records** | Medium | "Last pest inspection was on ... **Unable to determine**" No recent pest management plan or pest control contract evident beyond generic pest control line items in expenditure ($165–$250 p.a.). Useful for tenant/occupancy confirmation. |
| **Annual Fire Safety Statement (AFSS)** | Medium | "Date of the last Annual Fire Safety Statement (AFSS) ... **Not on file**". The CP Reports notes the scheme has "completed regular fire safety maintenance and have obtained their Annual Fire Safety Statement as required under the Environmental Planning and Assessment Regulations 2000" (per AGM minutes), but the actual AFSS is not provided. Should be on file. |
| **Valuation Date** | Medium | Building insurance valuation basis (James Spinks, 28 June 2006) is now 4 years old. A current valuation would clarify whether the $2,250,000 basis remains representative and whether the sum insured ($2,835,000) is adequate. Market movement may have shifted values. |
| **Strata Roll — Tenancy Status** | Low | "Number of tenanted units in the strata plan (or percentage): **Unable to determine**". The roll shows Unit 6 is currently leased (Calum Wilson & Vanja Tcherneva are "current lessee"), but the percentage of owner-occupied vs. tenanted is unclear. Useful for understanding community stability and incentives for maintenance spending. |
| **Building Age Confirmation** | Low | Building is described as "circa 1940s" in inspection but exact date of construction is not definitively stated. This affects understanding of expected remaining asset life and deterioration rate. |

---

## 6. QUESTIONS FOR THE VENDOR

1. **Asbestos Door Replacement Timeline:**  
   Can you provide evidence that the asbestos-laden doors in Units 3, 4, and 6 (identified Dec 2009, Aquafire quote $2,805) have been replaced, or confirm the current timeline for replacement? If not yet done, who will bear the cost, and when is replacement scheduled?

2. **Building Safety Compliance (2008 Report):**  
   The July 2008 Occupational Health & Safety report identified eight critical compliance items (electrical RCD installation, pathway trip hazard, loose railings, switchboard testing). Can you provide evidence these have been completed? If not, what is the remediation plan and estimated cost?

3. **Stairwell Works Completion:**  
   The January 2010 executive committee resolution approved stairwell repainting ($3,410, Argyle Painters) and carpet replacement (Baigowlah Carpet Choice). Can you provide invoices or photographic evidence confirming these works have been completed?

4. **Current Sinking Fund Plan:**  
   The most recent sinking fund/capital works plan is dated May 2006 (now 4+ years old). Has this plan been updated or revalidated? If not, when does the owners corporation intend to commission an updated Section 80 plan?

5. **Levy Adequacy & Special Levy Risk:**  
   Given the identified deferred maintenance and the asbestos remediation ($2,805 strata-wide cost), does the committee anticipate a special levy will be required in the next 24 months? If so, what is the estimated per-unit amount?

6. **Insurance Valuation Currency:**  
   The building insurance is based on a valuation dated 28 June 2006. Has the building been revalued recently? Is the sum insured ($2,835,000) considered adequate by the owners corporation?

7. **Fire Safety Statement:**  
   The April 2010 inspection notes the Annual Fire Safety Statement is "not on file." Can you provide the most recent AFSS or confirm the date of the last fire safety compliance check?

8. **Title Documentation:**  
   The CP Reports inspection notes the physical Title Deed for the common property is not available. Can you confirm the registered proprietor and provide evidence that the digital strata title (CP/SP10881) is current and unencumbered?

9. **Tenancy Composition:**  
   How many of the six units are owner-occupied versus tenanted as of the current date? This affects the unit's investment profile and voting dynamics.

10. **Pest Control Management:**  
    Is there a formal pest control contract in place, and when was the last treatment? Pest management is important for maintaining hygiene standards, particularly in common areas like the laundry.

11. **External Paint & Maintenance Program:**  
    Exterior painting was recently completed ($9,300 sunk fund expenditure, 2009–10). What is the expected maintenance cycle, and when is the next major external work (gutters, repainting, etc.) anticipated?

12. **Manager Tenure & Service Quality:**  
    Robinson Strata Management has been the manager since 2002. Is the current manager (John Jocumsen) still in role, and is there any feedback from the committee on service quality or proposed changes?

---

## 7. PURCHASE RECOMMENDATION AND PRICE GUIDANCE

### Market Price Estimate (Before Strata Analysis)

**Assumed Unit Profile:**
- 52 square metres (per strata roll)
- Likely 2-bedroom, 1-bathroom apartment (typical for 1940s six-unit building of this size)
- No dedicated parking (none noted in strata roll; "allocated parking: Nil noted")
- Heritage or character features (original 1940s construction, brick/tile)
- Manly North location (established residential, near beach)
- Comparable sold data for 2-bedroom apartments in Manly North, early 2010: $350,000–$450,000 range depending on condition, views, and amenities

**Conservative Market Estimate:** $400,000 (assumes average condition, no major defects, professional strata scheme management)

### Strata-Adjusted Valuation

The following material risks create downward adjustments:

| Risk Item | Nature | Adjustment | Certainty | Notes |
|---|---|---|---|---|
| **Asbestos Door Replacement** | Direct cost, Lot 6 share | –$935 | Certain | Aquafire quote Dec 2009, inc. GST. Cost is quantified and contained to door frame. |
| **Deferred Safety Compliance Works** | Strata-wide cost allocation, Lot 6 share | –$1,500–$2,500 | Probable | Estimated $3,000–$5,000 for electrical RCD installation, pathway remediation, railing secure, switchboard testing. Lot 6 share ~$500–$835 (1/6 entitlement). Allocated across whole strata. |
| **Sinking Fund Underfunding — Special Levy Risk (12–24 months)** | Estimated special levy, worst-case scenario | –$3,000–$6,000 | Probable | Current sinking fund ($21,434.71 for 6 units) is adequate for immediate needs but tight for major works. Deferred maintenance and obsolescence will trigger special levy within 2 years. Worst case (exterior painting overrun, concrete repairs, plumbing/electrical upgrades): $3,000–$6,000 strata-wide. Lot 6 share (15%): $450–$900. Mid-case estimate (accounting for staged remediation): $1,500–$2,000 strata-wide per lot over 24 months. |
| **Building Age & Deterioration** | Long-term structural/cosmetic wear, limited useful life on original systems | –$15,000–$25,000 | Probable | Building circa 1940s with 70+ year lifespan; original windows/services ageing. While structurally sound, anticipated major works over next 10–15 years (roof, concrete path replacement, window seals, full rewiring) will be substantial. Sinking fund inadequately sized. Buyer should expect ongoing capital contributions above current $724/quarter. Risk is long-term (5–15 years) but material. |
| **Limited Parking / No Dedicated Space** | Amenity loss vs. comparable buildings | –$0 to –$5,000 | Likely | Strata roll shows "allocated parking: Nil noted." This is typical for older buildings built pre-car-centric planning but limits resale appeal in current market. Adjustment is speculative; buyer's personal circumstances matter. Conservative mid-range: –$2,500. |
| **Governance Caution / Slow Decision-Making** | Soft factor: potential delays in spending decisions, cost consciousness may defer maintenance | –$0 to –$3,000 | Possible | Owner base is conservative on spending; decisions took 4+ months (Sep 2009 EGM to Jan 2010 resolution) on routine maintenance. This may delay necessary remediation, compounding future costs. Soft risk; adjustment is speculative. Estimate: –$1,000–$2,000 if buyer values rapid decision-making. |
| **Valuation & Compliance Age** | Insurance valuation (2006) and capital works plan (2006) outdated; potential for underinsurance or over-levying | –$500–$1,000 | Low | If valuation underestimates building replacement cost, scheme may be under-insured; if plan overestimates needs, levies may be excessive. Adjustment is precautionary. Estimate: –$500–$750. |

### Strata-Adjusted Valuation Range

**Low-End Adjustment (best-case scenario — deferred works completed, limited special levy):**
- Asbestos door: –$935
- Safety works: –$500
- Special levy (light): –$1,500
- Parking limitation: –$2,500
- Other: –$500
- **Total Adjustment:** –$6,435
- **Strata-Adjusted Price:** $400,000 – $6,435 = **$393,565**

**Mid-Range Adjustment (realistic scenario — deferred works proceed, moderate special levy, building age factor):**
- Asbestos door: –$935
- Safety works: –$2,000
- Special levy (moderate): –$2,500
- Parking limitation: –$2,500
- Building age & deterioration: –$15,000
- Governance caution: –$1,000
- Compliance documentation gap: –$750
- **Total Adjustment:** –$24,685
- **Strata-Adjusted Price:** $400,000 – $24,685 = **$375,315**

**High-End Adjustment (worst-case scenario — extended defect remediation, major special levy, significant building work needed):**
- Asbestos door: –$935
- Safety works (full scope): –$2,500
- Special levy (significant): –$6,000
- Parking limitation: –$5,000
- Building age & deterioration: –$25,000
- Governance delays: –$3,000
- Compliance gaps: –$1,000
- **Total Adjustment:** –$43,435
- **Strata-Adjusted Price:** $400,000 – $43,435 = **$356,565**

### Valuation Range Summary

| Scenario | Strata-Adjusted Price |
|---|---|
| Low (optimistic) | $393,500–$395,000 |
| **Mid (realistic)** | **$375,000–$377,000** |
| High (pessimistic) | $356,500–$360,000 |

---

## PURCHASE RECOMMENDATION

### **DO NOT BUY** without material price adjustment or conditions.

**Reasoning:**

The scheme presents **moderate-to-elevated structural and financial risk** that is not offset by the current market price estimate. Key concerns:

1. **Deferred Compliance Obligations:** Eight critical occupational health and safety items (electrical, pathway, railings, switchboard) identified over 18 months ago remain unresolved. This creates potential liability for the buyers corporation and indicates governance passivity or cost avoidance. Resolution costs are quantified but implementation is uncertain.

2. **Asbestos Exposure (Contained but Unresolved):** Three units have asbestos-laden doors. While replacement cost ($2,805 strata-wide, ~$935 per unit) is manageable, the fact that a nearly 5-month-old quote remains unacted on suggests hesitation or financial constraint within the owners corporation.

3. **Sinking Fund Inadequacy:** The capital works plan is 4 years old, no updated Section 80 assessment exists, and the fund balance ($21,434.71 for 6 units, or ~$3,572 per unit) is tight relative to identified deferred work. The probability of a special levy within 12–24 months is **high**. Buyers will face unexpected additional costs beyond regular levies.

4. **Building Age & Deterioration:** At 70 years, the building is beyond mid-life. While structurally sound, major systems (roof, external walls, plumbing, electrical) are approaching end-of-life. The scheme's reluctance to spend (evidenced by resistance to security intercom, months-long delay on stairwell work) suggests future major costs will be deferred, not prevented—creating compounding liability.

5. **Governance Conservatism:** Decision-making is slow and cost-focused. While this demonstrates financial prudence, it also suggests owners may resist necessary spending, deferring problems and creating larger future costs. This is a long-term risk factor.

6. **Market Context:** At an estimated market price of $400,000 for an older, no-parking, 52m² unit with identified remedial issues and sinking fund risk, the risk-return profile is unfavourable. A buyer in this price range in Manly North would more likely be seeking a newer building with fewer deferred issues.

### Conditional BUY (only if strict conditions are met):

A buyer could proceed **only if**:

- **Price is reduced to $360,000–$375,000** (accounting for identified risks and special levy probability)
- **Vendor provides written confirmation** (from strata manager and committee) that:
  - All eight 2008 OH&S compliance items will be completed by [specific date, e.g., 30 June 2010] at vendor's cost, OR vendor provides a cash holdback of $5,000 to cover completion shortfall
  - Asbestos door replacement (Unit 6) will be completed by [date] or vendor reimburses $935
  - An updated Section 80 capital works plan will be commissioned within 90 days of purchase, and if it forecasts a special levy, the vendor absorbs the first $2,000 of Lot 6's share
- **Buyer independently verifies** the title deed and strata title (CP/SP10881) via NSW Land Registry
- **Buyer obtains an independent building and pest inspection** (the 2008 Brainwaves report is now 2 years old and does not constitute due diligence)

### Recommendation Summary

At the **estimated market price of $400,000**, the property is **overpriced relative to identified risks**. A prudent buyer should either:

1. **Walk away** and seek a property in better financial and structural condition, or
2. **Negotiate the price down to $360,000–$375,000** and secure written commitments from the vendor to remediate key items before settlement.

The scheme is not in crisis, but it is in a transitional phase where significant capital spending is imminent. Buyers should be cautious and price-sensitive accordingly.

---

## SOURCES

### Online References

- Strata Schemes Management Act 2015 (NSW): https://legislation.nsw.gov.au/view/html/inforce/current/act-2015-094
- Strata Schemes Management Act 1996 (NSW, repealed): https://www.legislation.nsw.gov.au/ (historical reference)
- NSW Land Registry Services (Title verification): https://www.nswlrs.com.au/
- Fair Trading NSW — Strata Living Publications: https://www.fairtrading.nsw.gov.au/ (referenced in CP Reports inspection)
- Environmental Planning and Assessment Regulations 2000 (NSW) — Fire Safety Statement requirements: https://legislation.nsw.gov.au/

### Documents Reviewed (All Uploaded)

All claims in this report trace to the uploaded strata records and building inspection reports, listed in the Document Inventory above. No external market data, comparable sales data, or additional research beyond the uploaded documents has been incorporated, except for general market price estimates (based on implicit local knowledge of Manly North real estate circa early 2010, which is speculative and noted as such).

---

**Report Prepared:** April 2010 (retrospective analysis based on documents dated up to 27 April 2010)

**Disclaimer:** This report is an analysis of documents provided and does not constitute legal or financial advice. A prospective buyer should engage an independent strata lawyer and obtain current professional building and pest inspections before committing to purchase. The price guidance and risk assessments are based on information as at April 2010 and may not reflect current market conditions or circumstances.

---

**Property Address (Anonymised):**  
47 Hibiscus Lane, Neutral Bay NSW 2089  
Strata Plan 10881  
Lot 6
{{% /sample-output %}}
