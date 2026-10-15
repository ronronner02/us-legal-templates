# U.S. Legal Contracts and Forms Library

**Private internal research collection — 658 distinct documents as of October 15, 2026: 410 in the original organized snapshot, 83 additional originals in the October 14 supplementary collection, and 165 originals from seven subsequent research rounds.**

The combined collection contains **583 PDF and 75 DOCX originals**, deduplicated by SHA-256. [Open the complete searchable catalog](collection-overview/2026-10-15/index.html), [combined inventory](collection-overview/2026-10-15/inventory.csv), or [Chinese collection report](collection-overview/2026-10-15/REPORT.zh-CN.md). Existing organized-snapshot statistics and integrity manifests below retain their original scope.

This repository preserves the original organized collection through Pass 14, the supplementary collection, and subsequent research rounds. Original PDFs and DOCX files, source URLs, per-document metadata, extracted text, review flags, and SHA-256 checksums retain their original scope and bytes.

## Start here

- [Browse the complete organized library](organized-library/)
- [Browse all 658 originals across collections](collection-overview/2026-10-15/index.html)
- [Combined state and category statistics](collection-overview/2026-10-15/state-category-coverage.csv)
- [Detailed library guide](organized-library/README.md)
- [Document inventory](organized-library/00_Index/document-inventory.csv)
- [50-state, five-category coverage matrix](organized-library/00_Index/state-category-coverage.csv)
- [Complete metadata](organized-library/00_Index/all-records.json)
- [Document checksums](organized-library/00_Index/SHA256SUMS.txt)
- [Package integrity manifest](organized-library/00_Index/manifest.json)

## Directory structure

```text
organized-library/
|-- README.md
|-- 00_Index/
|   |-- document-inventory.csv
|   |-- state-category-coverage.csv
|   |-- all-records.json
|   |-- SHA256SUMS.txt
|   |-- manifest.json
|   |-- metadata/
|   `-- extracted-text/
|-- 01_Review_Required/
|   |-- 01_State_Documents/STATE_State_Name/Category/
|   |-- 02_Federal_Documents/Category/
|   |-- 03_Multistate_Templates/Category/
|   `-- 04_Research_References/Jurisdiction/Category/
|-- 02_Permission_Hold/STATE_State_Name/Category/
|-- 03_Historical_Review/Jurisdiction/Category/
`-- 04_File_Quality_Review/STATE_State_Name/Category/
```

### Categories

| Folder | Area |
| --- | --- |
| `A_Real_Estate` | Real estate |
| `B_Business_Contracts` | Business contracts |
| `C_Insurance` | Insurance |
| `D_Court_and_General_Legal` | Courts and general legal forms |
| `E_Employment` | Employment and labor |
| `Z_Category_Unconfirmed` | Classification pending review |

### Original organized snapshot counts

| Section | Unique files |
| --- | ---: |
| State documents | 363 |
| Federal documents | 15 |
| Multistate templates | 10 |
| Research references | 3 |
| Permission hold | 3 |
| Historical review | 5 |
| File quality review | 11 |
| **Total** | **410** |

Formats: **341 PDF and 69 DOCX**. The inventory also retains one link-only record, which does not count as a downloaded document. Incremental convenience copies and the older ZIP are deliberately excluded to avoid duplicating the corpus.

## Original snapshot coverage

- **50 states are physically represented**, including permission-held files.
- **48 states have active research files**; Michigan and North Carolina remain permission-held.
- **85 of 250 state/category cells** contain eligible research documents; **165 remain empty**.
- **Zero cells meet the full completion standard.** A single form does not establish complete state coverage.

These coverage figures describe the original 410-document snapshot. The combined overview records 113 occupied research cells out of 250 after later additions; presence does not establish completeness. Federal and multistate materials do not fill state-specific gaps. Quality-held files remain available for investigation but do not count toward eligible coverage.

## Rights, legal review, and privacy

**No document is approved for product publication. Keep this repository private.** Private storage is not a determination that copying, modification, or redistribution is legally permitted.

- **648 files lack confirmed commercial redistribution permission.** The remaining 10 retain conditional license records and are still unapproved for product publication. These combined figures include all collections through October 15.
- No repository-wide license is granted for the collected materials. Review each document's `copyright_status`, `license_url`, permission fields, and `legal_review_status`.
- Official publication, free access, successful downloading, and a valid file hash do not establish public-domain status, legal currency, or commercial reuse rights.
- Permission-held, historical, and file-quality materials are deliberately separated. Their presence here does not clear earlier restrictions.
- Preserve printed notices, attribution requirements, modification restrictions, and original bytes. Extracted text is a search aid, not a substitute for the original or professional legal review.
- Original documents and source text have not been translated. Collection guides and classification labels are in English.
- Three original Word files retain publisher-side local-path metadata; one also contains a public video-link redirect parameter. These source bytes are preserved for private review. Inspect embedded metadata before wider sharing; automated screening is not an exhaustive privacy review.

Do not enable public access, public download services, or product distribution without a separate item-level rights and legal review.

## Verify a downloaded copy

Run this PowerShell check from the repository root. It checks every asset listed in the package manifest and rejects unexpected files in the organized folder:

```powershell
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path '.\organized-library').Path
$manifest = Get-Content -LiteralPath (Join-Path $root '00_Index\manifest.json') -Raw | ConvertFrom-Json
$entries = @($manifest.files.PSObject.Properties)
foreach ($entry in $entries) {
    $path = Join-Path $root $entry.Name
    $actual = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actual -ne $entry.Value) { throw "Hash mismatch: $($entry.Name)" }
}
$actualCount = @(Get-ChildItem -LiteralPath $root -Recurse -File).Count
if ($actualCount -ne ($entries.Count + 1)) { throw 'Unexpected package file count' }
Write-Output "Verified $($entries.Count) indexed assets; $($manifest.document_count) distinct documents."
```

The manifest is an integrity index, not a cryptographic signature or proof of legal validity. `.gitattributes` prevents automatic line-ending conversion so text/metadata checksums remain consistent across platforms.

## Snapshot scope and future updates

This is an organized snapshot, **not a complete backup of the research project**. Raw HTTP captures, the local research database, manual-intake originals, collection scripts, historical increment folders, and operational logs remain in the local research workspace. Metadata retains their relative evidence references for traceability; those references are not promised to resolve inside this repository.

The parent-project commands in the detailed library guide apply to that research workspace, not to this snapshot checkout. For this repository, use the verification command above.

For later updates, finish collection, deduplication, classification, and rights review in the research workspace first. Refresh only the organized snapshot, verify every hash, inspect the exact changed paths, and then commit and push the intended update. Preserve prior versions and stricter review states; do not replace originals merely because filenames match.

**Collection snapshot timestamp (UTC): 2026-10-14T07:26:58.249990+00:00.**

## Additional collection - October 14, 2026

[Browse the additional research collection](research-collection/README.md) or [open its searchable catalog](research-collection/organized/2026-10-14-03/index.html). This historical 240-document catalog references 157 existing originals and adds 83 distinct originals, bringing the repository to **493 unique documents at that October 14 checkpoint**. Its final October 14 round adds 22 collected files. The existing organized snapshot, review states and integrity manifest remain preserved.

The combined count is deduplicated by SHA-256. The two inventories retain their own scope, provenance and review queues; shared records do not override existing permission, historical or quality holds.

## Combined collection - October 15, 2026

Seven later rounds add **165 distinct originals**, bringing the combined collection to **658**. The [overview](collection-overview/2026-10-15/REPORT.zh-CN.md) includes batch, state, category, format, review-section, source and integrity statistics. It records one unique link-only item separately from downloaded originals. The overview checks original hashes and preserves historical classifications; it does not establish legal currency, complete filing packets or publication approval.
