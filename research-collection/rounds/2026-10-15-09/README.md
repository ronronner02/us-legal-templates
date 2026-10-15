# Official-source collection round 2026-10-15-09

23 new original PDFs; 51 pages. Baseline: 683 distinct originals. Combined total after verification: 706.

Previous round 08 was pushed to `ronronner02/us-legal-templates`, branch `library/organized-snapshot`, at `5695ae08bdf97ff9fa27264993c95bc8e2a8b63b`. Remote SHA was verified before this round. This report records the verified pre-commit checkpoint for round 09. Subsequent commit and push state is recorded by Git history.

## Low-count state selection

| State | Before | Added | After |
| --- | --- | --- | --- |
| Nebraska | 2 | 21 | 23 |
| New Hampshire | 2 | 2 | 4 |

Alaska and Utah also began with two originals each. Alaska robots and Utah document-host robots requests timed out; no originals were requested from those hosts. Their counts remain two. Priority uses distinct original hashes, not directory or metadata-file counts.

## Browse and evidence

- [Searchable catalog](index.html), [CSV inventory](inventory.csv), [JSON inventory](inventory.json).
- [Final verification](reports/final-verification.json), [browser check](reports/browser-check.json), [integrity manifest](integrity-manifest.json).
- [State priorities](reports/state-prioritization.json), [acquisition summary](reports/acquisition-summary.json), [access and discovery gaps](reports/access-and-discovery-gaps.json).
- [Source ledger](evidence/source-ledger.json), [request ledger](evidence/request-ledger.json), [policy review](reports/source-policy-review.json).
- [Printed dates](reports/printed-date-review.json), [content discrepancies](reports/content-discrepancies.json), [companions](reports/companion-and-content-review.json), [follow-up queue](reports/follow-up-queue.json).

## Findings and review limits

Nebraska additions cover the initial claim and instructions, counterclaim and guide, civil-docket transfer, certified-mail return, subpoena request and guide, judgment satisfaction, default-judgment motion, publication/substitute-service companions, mailing evidence templates and fee-waiver application and guide. New Hampshire additions are two filing/attachment guides. Guidance, applications, affidavits, proposed orders and evidence templates retain separate roles. No filing packet is certified complete.

All 21 Nebraska printed date markers were checked in extracted text, retaining Eff., Rev. and NEW labels separately. The New Hampshire e-filing information sheet prints an unlabelled (07/01/2025) date and is marked For e-Filing only; the attachment guide date remains unverified. The February 2022 praecipe and May 2025 guide require edition-alignment review. HTTP Last-Modified and URL directory dates are not treated as publication or legal effective dates.

CC 6:6.5 and CC 6:6.7 headers identify CC forms while their footers identify corresponding DC codes. DC 6:6.9 includes a guardian/conservator name-field parenthetical although listed on the small-claims page. These source inconsistencies are retained without editing originals. Printed-text findings require visual/source follow-up and do not establish invalidity.

The Nebraska linked privacy-policy host already has an inherited access stop and was not requested. New Hampshire privacy policy and copyright footer evidence were captured; no blanket republication, modification or commercial reuse permission is established. Inherited permission holds and access stops remain intact.

Original bytes, HTTP bodies/headers, hashes and extracted text are retained. Parser and identity checks do not verify rendered layout, interactive fields, signatures, calculations, legal currency, complete packets, current program behavior or court acceptance. Reuse and publication approval remain pending. No personal data was entered, no external filing program was used and no case was submitted. Full-library semantic deduplication remains incomplete.

The root README and combined overview still describe the historical 658-document snapshot. This round records the current baseline and additions separately; the historical snapshot is unchanged.

## Acquired files

| State | Form or key | Document | Use | Printed date |
| --- | --- | --- | --- | --- |
| Nebraska | CC 4:1 | [Plaintiff's Claim and Notice to Defendant](originals/NE/ch6art14app1-8837f9f40933.pdf) | court_procedural_form | 07/2025 |
| Nebraska | CC 4:1 instructions | [Instructions for Plaintiff's Claim and Notice to Defendant](originals/NE/ch6art14app1-instructions-6a0440bea7dc.pdf) | procedural_guide | 07/2025 |
| Nebraska | CC 4:2 | [Counterclaim or Setoff of Defendant](originals/NE/cc-4-2-a293ceb149cb.pdf) | court_procedural_form | 05/2025 |
| Nebraska | CC 4:2a | [Instructions for Counterclaim or Setoff of Defendant](originals/NE/cc-4-2a-537a61e7d4f5.pdf) | procedural_guide | 05/2025 |
| Nebraska | CC 4:3 | [Notice to Transfer to Civil Docket](originals/NE/cc-4-3-5e8c1f08eedc.pdf) | court_procedural_form | 05/2016 |
| Nebraska | CC 4:5 | [Small Claims Certified Mail Return](originals/NE/cc-4-5-12450cdfeace.pdf) | service_return | 07/2026 |
| Nebraska | CC 4:6 | [Praecipe for Subpoena](originals/NE/cc-4-6-be181c32fa32.pdf) | court_procedural_form | 02/2022 |
| Nebraska | CC 4:6a | [Instructions for Praecipe for Subpoena](originals/NE/cc-4-6a-e400996a421e.pdf) | procedural_guide | 05/2025 |
| Nebraska | CC 4:8 | [Satisfaction of Judgment](originals/NE/cc-4-8-c5b5275ebbe1.pdf) | court_procedural_form | 02/2015 |
| Nebraska | CC 4:9 | [Motion to Set Aside Default Judgment and Application for New Trial](originals/NE/cc-4-9-e56cc2f9393c.pdf) | court_procedural_form | 02/2015 |
| Nebraska | CC 6:6.1 | [Motion for Service by Publication](originals/NE/cc-6-6-1-5798978882f8.pdf) | court_procedural_form | 05/2019 |
| Nebraska | CC 6:6.2 | [Affidavit in Support of Motion for Service by Publication](originals/NE/cc-6-6-2-4d1515c2288b.pdf) | court_procedural_form | 05/2019 |
| Nebraska | CC 6:6.3 | [Order for Service by Publication](originals/NE/cc-6-6-3-9ebf3b4703be.pdf) | proposed_court_order | 05/2019 |
| Nebraska | CC 6:6.4 | [Notice of Small Claims Proceeding (Service by Publication)](originals/NE/cc-6-6-4-17d7be22cf97.pdf) | court_procedural_form | 05/2019 |
| Nebraska | CC 6:6.5 | [Motion for Substitute Service](originals/NE/cc-6-6-5-3483baddf090.pdf) | court_procedural_form | 12/2025 |
| Nebraska | CC 6:6.6 | [Affidavit in Support of Motion for Substitute Service](originals/NE/cc-6-6-6-898ae1da556f.pdf) | court_procedural_form | 12/2025 |
| Nebraska | CC 6:6.7 | [Order for Substitute Service](originals/NE/cc-6-6-7-c44210ac034f.pdf) | proposed_court_order | 12/2025 |
| Nebraska | DC 6:6.8 | [Affidavit of Mailing Published Notice](originals/NE/dc-6-6-8-aba363b48aba.pdf) | court_procedural_form | 05/2025 |
| Nebraska | DC 6:6.9 | [Certificate of Mailing](originals/NE/dc-6-6-9-819affb5ba3e.pdf) | service_certificate | 02/2026 |
| Nebraska | DC 6:7.1 | [Affidavit and Application to Proceed Without Payment of Fees](originals/NE/dc-6-7-1-5dfdab62d10d.pdf) | court_procedural_form | 03/2025 |
| Nebraska | DC 6:7.1a | [Instructions for Affidavit and Application to Proceed Without Payment of Fees](originals/NE/dc-6-7-1a-e97e032a721f.pdf) | procedural_guide | 03/2025 |
| New Hampshire | scefilinginfo | [Small Claims e-Filing Information Sheet](originals/NH/scefilinginfo-aa709fe31c01.pdf) | procedural_guide | 07/01/2025 |
| New Hampshire | turbocourt-instructions-attach-doc-all | [Instructions for Attaching Documents in TurboCourt](originals/NH/turbocourt-instructions-attach-doc-all-98ccc5c3975a.pdf) | procedural_guide | Unverified |
