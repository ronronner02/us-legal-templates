# Official-source collection round 2026-10-15-05

25 new Wisconsin original PDF files. Baseline: 583 distinct originals. Combined expected total: 608; executed verification is recorded separately.

Previous delivery: commit `dde2fcba5b5b2e07b176ab65fee54bf482e8a9b6` was pushed to `ronronner02/us-legal-templates`, branch `library/organized-snapshot`, and the remote SHA was verified. This round was verified locally before submission. Delivery status is tracked by Git; the verification record describes the pre-commit checkpoint.

## Browse and evidence

- [Searchable catalog](index.html), [CSV inventory](inventory.csv), and [JSON inventory](inventory.json).
- [Final verification](reports/final-verification.json), [browser check](reports/browser-check.json), and [integrity manifest](integrity-manifest.json).
- [Source ledger](evidence/source-ledger.json), [request ledger](evidence/request-ledger.json), and [source policy review](reports/source-policy-review.json).
- [Acquisition summary](reports/acquisition-summary.json), [edition discrepancies](reports/edition-discrepancies.json), [cross-reference review](reports/cross-reference-review.json), and [follow-up queue](reports/follow-up-queue.json).

## Scope and review limits

This round contains 12 party filing forms, eight proposed orders, one blank eviction writ, and four procedural guides. Housing/eviction and non-eviction small-claims uses remain distinct. Twenty-two source rows expressly identify voluntary forms or guides; the remaining three are retained without inferring a mandatory status. Related declarations, stipulations, petitions, statements, and court orders are linked separately. Blank orders and writs are not issued court instruments.

SC-5130V is listed as revised September 12, 2024, while the supplied original prints 05/24. Both observations are preserved. SC-6030V, a replevin guide, references SC-512 Writ of Restitution; the catalog identifies SC-512 as an eviction writ and separately lists SC-514 Writ of Replevin. This cross-reference requires source and procedural review. Originals were not corrected or rewritten.

The initial Python transport failed DNS resolution. Ordinary browser requests reached the official Wisconsin source and PDF endpoints, with original bytes, response metadata, and SHA-256 receipts retained. SC-500 and SC-500I exhausted their bounded DNS retries and were not acquired. Two guide timeouts succeeded on one bounded retry. This is not a complete filing packet. Hawaii stopped at robots HTTP 403; Ohio stopped at robots TLS verification timeout. Maryland family forms were discovery-only. All inherited permission holds and access stops, including hostname aliases, remain in effect.

The standard-forms FAQ and acquired filing forms restrict modification. Original bytes, fields, and security settings are preserved. Legal applicability, visual layout, interactive fields, signatures, filing acceptance, reuse rights, and publication approval remain pending. Printed revisions were checked in extracted PDF text only. HTTP Last-Modified and site footer update dates are not treated as publication dates.

File SHA-256 checks screen duplicates across all baseline originals and this round. Related guidance and financial-disclosure content may overlap. Full-library semantic deduplication remains incomplete. Baseline tracked files are preserved byte for byte.

## Acquired files

| Form | Document | Use | Printed revision |
| --- | --- | --- | --- |
| SC-506A | [Order for Financial Disclosure (Small Claims)](originals/WI/sc-506a-1504f0cbea40.pdf) | proposed_order | 11/17 |
| SC-506B | [Financial Disclosure Statement (Small Claims)](originals/WI/sc-506b-4ec80eb43268.pdf) | court_procedural_form | 05/23 |
| SC-5100V | [Declaration of Service of SC-500, Summons and Complaint Eviction (Small Claims)](originals/WI/sc-5100v-772beb238dea.pdf) | court_procedural_form | 09/24 |
| SC-512 | [Writ of Restitution/Disposal of Personal Property (Eviction)](originals/WI/sc-512-f2054b52f467.pdf) | blank_writ_form | 03/22 |
| SC-5130V | [Declaration of Mailing (Small Claims)](originals/WI/sc-5130v-0921b25eed05.pdf) | court_procedural_form | 05/24 |
| SC-5200V | [Answer and Counterclaim (Small Claims)](originals/WI/sc-5200v-b0df3bff4d53.pdf) | court_procedural_form | 11/19 |
| SC-5250V | [Notice of Counterclaim - Claim against Plaintiff(s) (Small Claims)](originals/WI/sc-5250v-6e6c11e2d870.pdf) | court_procedural_form | 10/21 |
| SC-5300VA | [Stipulation for Dismissal Eviction (Small Claims)](originals/WI/sc-5300va-5e870b7d7e13.pdf) | court_procedural_form | 09/24 |
| SC-5300VB | [Order for Dismissal - Eviction (Small Claims)](originals/WI/sc-5300vb-032b04fb708d.pdf) | proposed_order | 10/07 |
| SC-5310VA | [Stipulation for Dismissal Non-Eviction (Small Claims)](originals/WI/sc-5310va-b492a97832ac.pdf) | court_procedural_form | 09/24 |
| SC-5310VB | [Order for Dismissal Non-Eviction (Small Claims)](originals/WI/sc-5310vb-7226ded21387.pdf) | proposed_order | 03/26 |
| SC-5400VA | [Declaration Based on Noncompliance Eviction (Small Claims)](originals/WI/sc-5400va-9efb087edd6a.pdf) | court_procedural_form | 09/24 |
| SC-5400VB | [Order for Judgment Based on Noncompliance Eviction (Small Claims)](originals/WI/sc-5400vb-b8e6d695ff31.pdf) | proposed_order | 09/24 |
| SC-5410VA | [Declaration Based on Noncompliance Non-Eviction (Small Claims)](originals/WI/sc-5410va-ca319ec78f82.pdf) | court_procedural_form | 09/24 |
| SC-5410VB | [Order for Hearing Non-Eviction (Small Claims)](originals/WI/sc-5410vb-57183aeb3e67.pdf) | proposed_order | 09/24 |
| SC-5420VA | [Declaration Based on Noncompliance for Money Judgment Non-Eviction (Small Claims)](originals/WI/sc-5420va-601ef048fb29.pdf) | court_procedural_form | 03/26 |
| SC-5420VB | [Order For Money Judgment Non-Eviction (Small Claims)](originals/WI/sc-5420vb-fb418e0ed403.pdf) | proposed_order | 09/24 |
| SC-5500VA | [Petition for Stay of Eviction Based on Defendant's Application for Emergency Assistance (Small Claims)](originals/WI/sc-5500va-01d8cd7c71ae.pdf) | court_procedural_form | 05/24 |
| SC-5500VB | [Order on Petition for Stay of Eviction Based on Defendant's Application for Emergency Assistance (Small Claims)](originals/WI/sc-5500vb-64ff2e7d3f0e.pdf) | proposed_order | 05/18 |
| SC-5510VA | [Statement on Eligibility to Receive or Receipt of Emergency Assistance (Small Claims)](originals/WI/sc-5510va-771010ddf8a1.pdf) | court_procedural_form | 11/19 |
| SC-5510VB | [Order on Eligibility to Receive or Receipt of Emergency Assistance (Small Claims)](originals/WI/sc-5510vb-1c392a900949.pdf) | proposed_order | 11/17 |
| SC-6000V | [Basic Guide to Wisconsin Small Claims Actions](originals/WI/sc-6000v-2211504c3839.pdf) | procedural_guidance | 09/24 |
| SC-6010V | [Pre-Judgment: Basic Steps for Handling a Small Claims Case for Eviction](originals/WI/sc-6010v-e1b04b75ded6.pdf) | procedural_guidance | 09/24 |
| SC-6020V | [Pre-Judgment: Basic Steps for Handling a Small Claims Case for Recovery of Money](originals/WI/sc-6020v-9d489c90e9ee.pdf) | procedural_guidance | 11/19 |
| SC-6030V | [Pre-Judgment: Basic Steps for Handling a Small Claims Case for Replevin (Recovery of Property)](originals/WI/sc-6030v-11dc8f39b163.pdf) | procedural_guidance | 11/19 |
