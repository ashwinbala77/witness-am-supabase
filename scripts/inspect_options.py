import json
with open(r"C:\Claude Code\airtable_schema_2026-06-25.json", encoding="utf-8-sig") as f:
    data = json.load(f)

# Find one example of each interesting type and print its full JSON
wanted = {"date","percent","currency","formula","rollup","multipleLookupValues",
          "multipleAttachments","multipleRecordLinks","count","number"}
seen = {}
for t in data["tables"]:
    for fld in t["fields"]:
        ty = fld["type"]
        if ty in wanted and ty not in seen:
            seen[ty] = (t["name"], fld)
    if len(seen) == len(wanted):
        break

for ty, (tname, fld) in seen.items():
    print(f"### {ty}  (from {tname})")
    print(json.dumps(fld, indent=2)[:900])
    print()
