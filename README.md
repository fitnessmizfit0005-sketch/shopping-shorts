# shopping-shorts

모찌코치 쇼핑쇼츠(인스타 릴스) 주간 제작표.

공개 URL: https://fitnessmizfit0005-sketch.github.io/shopping-shorts/

## 구조
- `index.html` — 주차 목록 + 제작 규칙
- `week.html?w=2026-10-10` — 주간 제작표 (데이터 파일을 읽어서 보여줌)
- `data/weeks.json` — 주차 목록
- `data/<주 시작일>.json` — 그 주의 슬롯 15개
- `data/rules.json` — 제작 규칙, 상태 값 목록

## 편집하는 법 (GitHub 웹에서)
1. 주간 페이지의 **✎ GitHub에서 이 주 편집** 버튼
2. 바꿀 값만 고치기. 예: `"status": "대기"` → `"status": "편집완료"`
3. **Commit changes** → 1~2분 뒤 페이지 반영

상태 값: `대기` · `소스확보` · `편집완료` · `예약완료` · `업로드완료`
메모는 `"memo": ""` 따옴표 안에, 상품번호는 `"product_no": "042번"` 처럼.

> 따옴표(")와 쉼표(,)는 지우지 마세요. 깨지면 페이지에 빨간 안내가 떠요.
