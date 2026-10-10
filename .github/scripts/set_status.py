# 이슈 제목 "[상태] mozzi-261010-2 업로드완료" → data/*.json 해당 항목 status 변경
import glob, json, os, re, sys
STATUSES = ["대기", "소스확보", "대본완료", "편집완료", "예약완료", "업로드완료"]
m = re.match(r"\[상태\]\s*(mozzi-\d{6}-\d)\s+(\S+)", sys.argv[1].strip())
out = os.environ.get("GITHUB_OUTPUT")
def say(msg):
    print(msg)
    if out:
        with open(out, "a", encoding="utf-8") as f: f.write(f"msg={msg}\n")
if not m or m.group(2) not in STATUSES:
    say("처리 실패: 제목은 '[상태] mozzi-YYMMDD-N 업로드완료' 형식이어야 해요"); sys.exit(1)
sid, st = m.groups()
for f in sorted(glob.glob("data/2026-*.json")) + sorted(glob.glob("data/20[3-9]*.json")):
    d = json.load(open(f, encoding="utf-8"))
    for it in d.get("items", []):
        if it.get("id") == sid:
            it["status"] = st
            json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            say(f"{sid} → {st} 반영했어요 (1~2분 뒤 제작표에 보여요)"); sys.exit(0)
say(f"처리 실패: {sid}를 제작표에서 찾지 못했어요"); sys.exit(1)
