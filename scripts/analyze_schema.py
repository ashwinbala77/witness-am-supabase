import json, collections, sys

with open(r"C:\Claude Code\airtable_schema_2026-06-25.json", encoding="utf-8-sig") as f:
    data = json.load(f)

tables = data["tables"]
print(f"TOTAL TABLES: {len(tables)}\n")

# id -> name map for resolving links
id2name = {t["id"]: t["name"] for t in tables}

type_counter = collections.Counter()
print("=" * 80)
print("TABLE OVERVIEW")
print("=" * 80)
for t in tables:
    print(f"\n## {t['name']}  ({t['id']})  — {len(t['fields'])} fields")
    pf = t.get("primaryFieldId")
    for fld in t["fields"]:
        ftype = fld["type"]
        type_counter[ftype] += 1
        extra = ""
        opts = fld.get("options") or {}
        if ftype in ("multipleRecordLinks", "singleRecordLink"):
            linked = opts.get("linkedTableId")
            extra = f" -> links to [{id2name.get(linked, linked)}]"
            if opts.get("prefersSingleRecordLink"):
                extra += " (single)"
        elif ftype in ("singleSelect", "multipleSelects"):
            choices = [c["name"] for c in opts.get("choices", [])]
            extra = f" choices={choices}"
        elif ftype in ("formula", "rollup", "count", "lookup", "multipleLookupValues"):
            extra = " (COMPUTED)"
        primary = "  [PRIMARY]" if fld["id"] == pf else ""
        print(f"   - {fld['name']}: {ftype}{primary}{extra}")

print("\n" + "=" * 80)
print("FIELD TYPE FREQUENCY (across all tables)")
print("=" * 80)
for typ, n in type_counter.most_common():
    print(f"   {n:4d}  {typ}")
