import json, io, glob, os, sys

SETS  = "data/sets"
SCOPE = "all"   # "all" = ทั้งคลัง · "set" = เฉพาะ topics มี "1"

def gen_id(sid, qno):
    return f"{sid}-q{int(qno):02d}"

# ---- PHASE 0: normalize id เดิมที่ไม่ pad → q01 (portal ยืนยัน refs=0/0 ปลอดภัย) ----
norm = 0; norm_files = set()
for fp in sorted(glob.glob(f"{SETS}/*.json")):
    d = json.load(io.open(fp, encoding="utf-8"))
    stem = os.path.splitext(os.path.basename(fp))[0]
    chg = False
    for q in d.get("questions", []):
        if q.get("id"):
            qno = q.get("questionNumber")
            if qno is not None:
                exp = gen_id(q.get("setId", stem), qno)
                if q["id"] != exp:
                    q["id"] = exp; norm += 1; chg = True
    if chg:
        io.open(fp, "w", encoding="utf-8", newline="\n").write(
            json.dumps(d, ensure_ascii=False, indent=2))
        norm_files.add(os.path.basename(fp))
print(f"PHASE0 normalize {norm} id · {len(norm_files)} files")

# ---- PHASE 1: guard — id เดิมทุกตัวต้องตรงสูตรแล้ว (ไม่ตรง = abort) ----
bad = []
for fp in sorted(glob.glob(f"{SETS}/*.json")):
    d = json.load(io.open(fp, encoding="utf-8"))
    stem = os.path.splitext(os.path.basename(fp))[0]
    for q in d.get("questions", []):
        if q.get("id"):
            exp = gen_id(q.get("setId", stem), q.get("questionNumber"))
            if q["id"] != exp:
                bad.append((os.path.basename(fp), q["id"], exp))
if bad:
    print("ABORT — id เดิมไม่ตรงสูตร:")
    for b in bad[:20]: print("  ", b)
    sys.exit(1)
print("PHASE1 OK — id เดิมทุกตัวตรงสูตร")

# ---- PHASE 2: เติม id ที่หาย (id เป็น key แรก) ----
added = changed = 0; collisions = []; no_qno = []
for fp in sorted(glob.glob(f"{SETS}/*.json")):
    d = json.load(io.open(fp, encoding="utf-8"))
    stem = os.path.splitext(os.path.basename(fp))[0]
    seen = {q["id"] for q in d.get("questions", []) if q.get("id")}
    fchg = False
    for q in d.get("questions", []):
        if q.get("id"): continue
        if SCOPE == "set" and "1" not in q.get("topics", []): continue
        qno = q.get("questionNumber")
        if qno is None: no_qno.append(os.path.basename(fp)); continue
        nid = gen_id(q.get("setId", stem), qno)
        if nid in seen: collisions.append((os.path.basename(fp), nid)); continue
        seen.add(nid)
        newq = {"id": nid}; newq.update(q)
        q.clear(); q.update(newq)
        added += 1; fchg = True
    if fchg:
        io.open(fp, "w", encoding="utf-8", newline="\n").write(
            json.dumps(d, ensure_ascii=False, indent=2))
        changed += 1
if collisions: print("COLLISION:", collisions)
if no_qno:     print("NO questionNumber:", set(no_qno))
print(f"PHASE2 added {added} id · {changed} files · scope={SCOPE}")
