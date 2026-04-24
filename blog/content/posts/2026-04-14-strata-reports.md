---
date: 2026-04-14
title: "The pre-sale Strata Report"
summary: "A blunt guide to reading a pre-sale strata report with LLM help, including the prompt used to surface risks, omissions, and likely buyer exposure."
featured_image: "/blog/images/strata-report-buyers.png"
featured_image_alt: "A concerned couple looking at a pre-sale residential strata report in front of a modern apartment building."
---

Everyone says, quite rightly, before you buy into a strata you must obtain (even if you have to pay for it) the strata report.  The wisdom is that, the strata report will provide all you need to make an informed decision about the maintenance of the buildings, its financial situation, and the (dis)harmony of your potential co-owners and neighbours.

Working against that are many forces which would prefer you execute the purchase without knowing any of those things.  The seller and their real estate agent would prefer you stay in the dark so you don't get cold feet and don't have any ammunition to soften your bid.  The Owners, generally, would prefer you not have a clear view for the same reason; they are conscious that the price you pay will reflect on the valuation of their unit.  And the, supposedly independent, company offering the Strata Report doesn't really want you to discover any gremlins because they want more business from these Real Estate agents and don't want exposure to a lawsuit for putting people off.

Oddly enough, it's really only the Strata Manager who doesn't really care, or even inclined that you do know the whole story; so they don't have to endure the outrage of the new owners when negatives become more clear.  But, that motive is not strong enough to overcome the fear of irritating the hands that feed them, so they simply won't talk to you at all.

But we have a modern solution: the LLM (or 'ChatGPT') has no skin in the game (yet) and no motivation to sugar coat it for you.  This is the best way I have discovered to 'read between the lines' of a 'strata report' and get some negative, or objective, feedback.

1. Get the strata report:
2. Feed the strata report into an LLM (ie ChatGPT, Claude, Copilot, Grok, llama, etc.) for evaluation.  

The extensive prompt below will generate a comprehensive assessment of the strata report.  You can paste it into Claude (or your LLM of choice), attach the strata report file and add your own prompt simply stating something like "The address is "99 Baker St Cronulla NSW" and the unit number is "6".  The output is insightful and comprehensive but, of course, not as authoritative as it purports... consider what it says with your own judgement and grains of salt.

I thought about setting this up as a "buy me a coffee service", but the LLM told me it wasn't worth my time. 😊

```
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

8-12 specific questions targeting identified gaps, risks, or ambiguities. Each should require a factual, verifiable answer and specify documentary evidence where relevant.

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
```
