# Official-source collection round 2026-10-15-10

20 new Oklahoma original PDFs; 43 pages. Baseline: 706 distinct originals. Combined expected total: 726; final verification records the executed result.

Previous round 09 was pushed to `ronronner02/us-legal-templates`, branch `library/organized-snapshot`, at `b13682c8849f36440d81d64f54356ac4cc9b94b2`. Remote SHA was verified before this round. This report records the verified pre-commit checkpoint for round 10. Subsequent commit and push state is recorded by Git history.

## Low-count state priority

| State | Before | Added | After |
| --- | --- | --- | --- |
| Oklahoma | 5 | 20 | 25 |

Lower-count sources were evaluated first. Mississippi returned robots HTTP 500; Indiana timed out; Wyoming returned a WAF challenge; Arizona returned HTTP 403; Connecticut robots disallows named assisted-retrieval clients; the tested Florida judiciary hostname failed DNS lookup. No source or original requests followed those failures/stops. Georgia permits the catalog but disallows the PDF upload directory: 42 links are retained without downloads. These observations do not establish that any state lacks forms. All inherited holds remain in force.

## Browse and evidence

- [Searchable catalog](index.html), [CSV inventory](inventory.csv), [JSON inventory](inventory.json).
- [Final verification](reports/final-verification.json), [browser check](reports/browser-check.json), [integrity manifest](integrity-manifest.json).
- [State priorities](reports/state-prioritization.json), [acquisition summary](reports/acquisition-summary.json), [access and discovery gaps](reports/access-and-discovery-gaps.json), [Georgia link-only candidates](reports/link-only-candidates.json).
- [Source ledger](evidence/source-ledger.json), [request ledger](evidence/request-ledger.json), [policy review](reports/source-policy-review.json).
- [Printed dates](reports/printed-date-review.json), [content findings](reports/content-discrepancies.json), [extraction review](reports/extraction-review.json), [source-label findings](reports/source-content-review.json), [companions](reports/companion-and-content-review.json), [follow-up queue](reports/follow-up-queue.json).

## Findings and limits

This round supplements three earlier Oklahoma real-estate originals, keeping disclaimer and exemption forms distinct from condition disclosure, landlord and seller lead-paint disclosure separate, and land-ownership affidavits distinct from the federal tax-status affidavit. Lease application, addenda, supplement, tenant rules, brokerage disclosure, guidance and consumer notices retain separate roles. No complete transaction packet is verified.

Sixteen originals print the parenthetical date (01-01-2026), verified in extracted text. Three ownership affidavits print OAG 2023-1, OAG 2023-2 and OAG 2023-3 identifiers; these are not interpreted as revision dates. The resource-guide edition date remains unverified. URL years and HTTP Last-Modified are not publication or legal effective dates.

The pet addendum has two PDF pages but prints Page 1 of 1 and Page 2 of 1, and a Section Marker header. Property-data page 3 contains 202 replacement characters in extracted field-line regions. Resource-guide pages 1 and 11 have little extractable text. OAG 2023-1 produced five object-pointer parser warnings while parsing successfully. Original bytes remain unchanged; these findings require compatible-viewer and visual inspection, not silent correction.

The source label Lead-Based Paint - Residential Disclosure (EPA Link) points to a local 2025 seller-disclosure PDF. That link is not fetched or conflated with the acquired 2026 seller disclosure. Source section context and observed destinations are preserved.

Copyright/protection and policy pages are captured; a download link does not establish broad commercial reuse, modification or republication permission. Legal and tax currency, fields, calculations, signatures, notarizations, visual layout, packet completeness and transaction acceptance remain pending. No personal data was entered, no application screening, tax filing, transaction, financial transfer or legal submission occurred. Full-library semantic deduplication remains incomplete.

The root README and combined overview remain historical 658-document snapshots. This round records the 706-original baseline and 20 additions separately.

## Acquired files

| Document | Role | Printed date or identifier | Pages |
| --- | --- | --- | --- |
| [Residential Property Condition Disclosure Act Resource Guide](originals/OK/property-condition-act-guide-21021ad162da.pdf) | agency_guide | Unverified | 11 |
| [Residential Property Condition Disclaimer Statement (Appendix B)](originals/OK/property-condition-disclaimer-f32281d53644.pdf) | statutory_disclosure | 01-01-2026 | 1 |
| [Residential Property Condition Disclosure Exemption Form](originals/OK/property-condition-exemption-b9f0c7471ab7.pdf) | statutory_disclosure | 01-01-2026 | 1 |
| [Lead-Based Paint Landlord Disclosure](originals/OK/lead-paint-landlord-disclosure-382848cf976e.pdf) | statutory_disclosure | 01-01-2026 | 1 |
| [Lead-Based Paint Seller Disclosure](originals/OK/lead-paint-seller-disclosure-391bc00f8246.pdf) | statutory_disclosure | 01-01-2026 | 1 |
| [Residential Lease Application](originals/OK/lease-application-4f04da76baa7.pdf) | application_form | 01-01-2026 | 6 |
| [Disclosure of Brokerage Services to Landlord or Tenant](originals/OK/broker-disclosure-landlord-tenant-a68028b98cc7.pdf) | brokerage_disclosure | 01-01-2026 | 1 |
| [Key and Re-Keying Addendum](originals/OK/key-rekeying-addendum-7f91e4c18538.pdf) | contract_addendum | 01-01-2026 | 1 |
| [Pet Addendum](originals/OK/pet-addendum-ab36f3eadd90.pdf) | contract_addendum | 01-01-2026 | 2 |
| [Residential Lease Supplement](originals/OK/lease-supplement-6ebfd3ea8e94.pdf) | contract_supplement | 01-01-2026 | 1 |
| [Tenancy Guidelines](originals/OK/tenancy-guidelines-3558bf9927f0.pdf) | lease_rules | 01-01-2026 | 2 |
| [Affidavit for Title or Ownership of Land - Individual](originals/OK/ownership-affidavit-individual-ed41af0e05f2.pdf) | ownership_affidavit | OAG 2023-1 | 2 |
| [Affidavit for Title or Ownership of Land - Non-Exempt Business or Trust](originals/OK/ownership-affidavit-nonexempt-business-dac778521d9d.pdf) | ownership_affidavit | OAG 2023-2 | 2 |
| [Affidavit for Title or Ownership of Land - Exempt Business or Trust](originals/OK/ownership-affidavit-exempt-business-7435d6bdb620.pdf) | ownership_affidavit | OAG 2023-3 | 2 |
| [Non-Foreign Seller Affidavit](originals/OK/nonforeign-seller-affidavit-8461d6ca8db2.pdf) | tax_affidavit | 01-01-2026 | 1 |
| [Non-Foreign Seller Information Sheet](originals/OK/nonforeign-seller-information-1dd125b6e85a.pdf) | tax_information_guide | 01-01-2026 | 2 |
| [Notice to Buyer - Signs and Risk of Deed Theft](originals/OK/deed-fraud-notice-679f99d9d49f.pdf) | consumer_notice | 01-01-2026 | 1 |
| [Notice of Homeowner Cancellation of Wholesale Real Estate Purchase Contract](originals/OK/wholesale-contract-cancellation-98c0e3aeb13d.pdf) | cancellation_notice | 01-01-2026 | 1 |
| [Wire Fraud Advisory](originals/OK/wire-fraud-advisory-abd039aa941c.pdf) | consumer_notice | 01-01-2026 | 1 |
| [Property Data Form](originals/OK/property-data-6291a563285b.pdf) | property_information_form | 01-01-2026 | 3 |
