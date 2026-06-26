import json, collections

with open(r"C:\Claude Code\airtable_schema_2026-06-25.json", encoding="utf-8-sig") as f:
    data = json.load(f)

tables = data["tables"]
id2name = {t["id"]: t["name"] for t in tables}

COMPUTED = {"formula","rollup","count","lookup","multipleLookupValues","autoNumber","createdTime","lastModifiedTime","createdBy","lastModifiedBy","button"}

print(f"TOTAL TABLES: {len(tables)}\n")
print(f"{'TABLE':<35}{'FIELDS':>7}{'COMPUTED':>9}{'LINKS':>6}")
print("-"*60)
links = []  # (from, to)
grand_types = collections.Counter()
for t in tables:
    nf = len(t["fields"])
    nc = sum(1 for f in t["fields"] if f["type"] in COMPUTED)
    nl = 0
    for f in t["fields"]:
        grand_types[f["type"]] += 1
        if f["type"] in ("multipleRecordLinks","singleRecordLink"):
            nl += 1
            tgt = (f.get("options") or {}).get("linkedTableId")
            links.append((t["name"], id2name.get(tgt, tgt)))
    print(f"{t['name']:<35}{nf:>7}{nc:>9}{nl:>6}")

print("\n\nFIELD TYPE FREQUENCY (all tables):")
for typ,n in grand_types.most_common():
    tag = "  <-- COMPUTED (no direct column)" if typ in COMPUTED else ""
    print(f"   {n:5d}  {typ}{tag}")

print(f"\n\nRELATIONSHIPS ({len(links)} link fields):")
# dedupe directed pairs
seen = collections.Counter()
for a,b in links:
    seen[(a,b)] += 1
for (a,b),n in sorted(seen.items()):
    print(f"   {a}  ->  {b}" + (f"  (x{n})" if n>1 else ""))
