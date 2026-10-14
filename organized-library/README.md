# U.S. Legal Contracts and Forms Library

## Start here

This folder contains **410 distinct documents**, deduplicated by SHA-256: **341 PDFs and 69 DOCX files**. Every document is a byte-identical copy of its archived source file.

Files associated with **50 states** are present, including documents on permission hold. The active research catalog represents **48/50 states**. Neither figure means that every legal category is complete or that the documents are cleared for commercial use.

**No document in this folder is approved for publication to product users.** Free access, official publication, or inclusion in this collection does not establish permission to redistribute or modify a document commercially.

## Find a document

- **Browse by state:** open `01_Review_Required/01_State_Documents/STATE_State_Name/`, then choose a legal category.
- **Check permission-held files:** open `02_Permission_Hold/`. Previously received Michigan and North Carolina documents remain separate from the active research catalog.
- **Check file-quality exceptions:** open `04_File_Quality_Review/`. These originals are preserved and counted as physical files, but excluded from eligible state/category coverage. A source-byte match does not clear a structural anomaly.
- **Search or filter the inventory:** open [document-inventory.csv](00_Index/document-inventory.csv). It includes the title, state, category, printed edition, file location, source URLs, SHA-256, and review status. CSV files use UTF-8 with a BOM for spreadsheet compatibility.
- **Review detailed metadata:** use the `metadata_path` column or open [all-records.json](00_Index/all-records.json).
- **Search extracted text:** use `00_Index/extracted-text/`. This text is a search aid, not a replacement for the original document. No OCR was performed.

## Folder structure

```text
organized-library/
├── README.md
├── 00_Index/
│   ├── document-inventory.csv
│   ├── latest-manual-intake.csv
│   ├── state-category-coverage.csv
│   ├── all-records.json
│   ├── original-paths.json
│   ├── link-only-records.csv
│   ├── excluded-non-documents.json
│   ├── SHA256SUMS.txt
│   ├── manifest.json
│   ├── metadata/
│   └── extracted-text/
├── 01_Review_Required/
│   ├── 01_State_Documents/STATE_State_Name/Category/
│   ├── 02_Federal_Documents/Category/
│   ├── 03_Multistate_Templates/Category/
│   └── 04_Research_References/Jurisdiction/Category/
├── 02_Permission_Hold/STATE_State_Name/Category/
├── 03_Historical_Review/Jurisdiction/Category/
└── 04_File_Quality_Review/STATE_State_Name/Category/
```

### Legal categories

| Folder | Category |
| --- | --- |
| `A_Real_Estate` | Real estate |
| `B_Business_Contracts` | Business contracts |
| `C_Insurance` | Insurance |
| `D_Court_and_General_Legal` | Court and general legal forms |
| `E_Employment` | Employment and labor |
| `Z_Category_Unconfirmed` | Classification pending review |

State folders use standard two-letter codes and English state names, such as `NM_New Mexico`. Federal documents, multistate templates, research references, and historical materials are kept separate and do not fill gaps in state-specific coverage.

## Document counts

| Section | Distinct documents |
| --- | ---: |
| State documents | 363 |
| Federal documents | 15 |
| Multistate templates | 10 |
| Research references | 3 |
| Permission hold | 3 |
| Historical review | 5 |
| File quality review | 11 |
| **Total** | **410** |

There are also **1 link-only records** without a local document. These are listed separately and do not increase the document count. Historical files are retained; a historical classification alone does not establish that a form has been legally withdrawn.

## Latest manual intake

The latest batch contains **3 files totaling 9 PDF pages**.

| State | Document | Printed edition evidence | Placement |
| --- | --- | --- | --- |
| NV | Nevada Contract for Services of Independent Contractor | Printed effective month 02/2017; reformatted 03/2020 | Active research catalog; review required |
| NV | Nevada Terms and Conditions for Goods | Revised 2024-10 | File quality review; excluded from eligible coverage |
| NV | Nevada Terms and Conditions for Services | Revised 2024-10 | File quality review; excluded from eligible coverage |

Review the `scope_review` and warning fields in [latest-manual-intake.csv](00_Index/latest-manual-intake.csv) and each document's metadata. A request, complaint, proposal, or reporting list is not necessarily the underlying contract or a complete filing packet.

Previously identified items still requiring review:

- **NM NOA-1:** the supplied PDF has one page but refers to the back of the form. Check the layout and related instructions. This is not a confirmed finding of corruption or missing pages.
- **NM complaint and lump-sum petition:** their instructions refer to additional procedural forms in applicable circumstances. An individual file is not necessarily a complete filing packet.
- **MI and NC:** the existing permission holds remain in place despite manual receipt of the files.

Printed revision dates are not verified publication or effective dates. Original download timestamps remain unknown where no reliable download-time evidence exists. A latest-intake row labeled File quality review is retained for investigation, not cleared for normal use.

## Permissions and file-quality notes

- **400 documents** lack confirmed commercial redistribution permission. The other **10 documents** have conditional license records but are still not approved for product publication.
- Permission-held files are retained as user-supplied materials for isolated review. Their prior acquisition/use holds and website access stops have not been cleared.
- PDF and DOCX editions may represent the same legal instrument but have different bytes; both are retained. The 12-character hash suffix in a filename prevents same-name collisions and is not a legal version number.
- `unknown` means the information has not been verified. Check the metadata for older revision labels, font warnings, encryption flags, XFA viewer requirements, and mixed page-revision labels. Successful parsing does not establish legal validity or perfect text extraction.
- **62 existing physical response files** containing HTML, JSON, or error messages are excluded from the legal-document folders. Their original copies remain in the project.
- Folder names, inventory headings, and collection documentation are in English. Original legal documents and their extracted source text are not translated or rewritten; official bilingual content is preserved.

## Copying and maintaining this folder

You can copy this folder as a unit for internal browsing and review. It includes the documents, indexes, per-file metadata, extracted text, and checksums. It is **not a complete project backup**: original network capture logs and the research database remain in the parent project. Metadata retains source pages, original download URLs, original project paths, and historical evidence references.

Run these commands from the parent project directory:

```powershell
python scripts/organize.py --dry-run
python scripts/organize.py
python scripts/organize.py --verify
```

Repeated runs do not add duplicate files. If an organized file has been manually edited, or a changed classification makes previous paths obsolete, the program stops rather than overwriting or deleting those files. Keep the existing folder and use `--output organized-library-YYYYMMDD` to create a new snapshot.

**Statistics source timestamp (UTC):** 2026-10-14T07:26:58.249990+00:00

Document layout, jurisdictional applicability, current legal effect, and commercial reuse permission remain separate review requirements.
