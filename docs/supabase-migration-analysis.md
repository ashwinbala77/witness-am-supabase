# Airtable → Supabase (Postgres) Migration Analysis

_Source: `airtable_schema_2026-06-25.json` — 40 tables, ~2,380 fields._

## 1. What this base is
A real estate / hotel asset-management base. Two hub tables anchor everything:
- **`Investments`** (257 fields) — top-level investment records.
- **`Asset_detail`** (211 fields) — per-asset operating detail; links to 25 other tables.

## 2. Stored vs. computed fields
~770 of ~2,380 fields (≈⅓) are **computed** and must NOT become plain columns:

| Type | Count | Postgres equivalent |
|------|------:|---------------------|
| formula | 322 | View column, generated column, or app-side |
| multipleLookupValues | 297 | JOIN / view (value lives in linked table) |
| rollup | 127 | Aggregate in a view (SUM/AVG over children) |
| createdTime / lastModifiedTime / By | 28 | `created_at` / `updated_at` + triggers |
| autoNumber / button | 3 | `bigserial` / drop (UI only) |

**Implication:** migrate the ~1,600 "real" fields as columns; re-express the rest as views/generated columns.

## 3. Type mapping
| Airtable | Postgres | Notes |
|----------|----------|-------|
| singleLineText / multilineText / url | `text` | |
| number | `numeric` / `integer` | |
| currency (524) | `numeric(14,2)` | symbol is display-only |
| percent (144) | `numeric` | decide storage convention (0.05 vs 5) |
| date | `date` / `timestamptz` | |
| checkbox | `boolean` | |
| singleSelect (112) | `text` + CHECK, or `enum` | |
| multipleSelects (8) | `text[]` or child table | |
| multipleAttachments (6) | Supabase Storage + URL table | files not in DB |
| multipleRecordLinks (130) | FK (1:N) or junction table (M:N) | |

## 4. Relationship strategy
- **Hub-and-spoke:** most tables get a FK to `investments` and/or `asset_detail`.
- **Self-references:** `investment_positions`, `str_28_day_trend`, `hotel_actuals` → self-FK.
- **Many-to-many** (e.g. `lenders` ↔ `loan_summary_data`) → junction tables.
- Airtable `multipleRecordLinks` are M:N by default; most here are really 1:N. Each needs a per-link decision.

## 5. Recommended approach (phased)
1. **Naming pass** — snake_case all tables/columns; resolve duplicates (e.g. `Hotel_GSS_data` vs `_v2`).
2. **Core tables first** — `investments`, `asset_detail`, `investing_entities` with surrogate `id uuid` primary keys; keep Airtable record IDs in an `airtable_id text` column for traceable migration.
3. **Add foreign keys** for the hub-and-spoke links.
4. **Junction tables** for true M:N links.
5. **Selects → enums or lookup tables.**
6. **Recreate computed fields as views / generated columns** (last, once base data is in).
7. **Attachments → Supabase Storage.**
8. **Load data**, then add indexes on FK columns and enable Row Level Security (RLS).

## 6. Open decisions
- Keep all 257 columns on `Investments`, or split into logical sub-tables?
- Percent storage convention (fraction vs whole number)?
- Drop computed fields entirely, or recreate every one as a view?
- One-time migration vs ongoing Airtable→Supabase sync?
