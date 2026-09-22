import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ── CORS 설정 ──────────────────────────────────────────
# 로컬 개발(localhost:5173)과 배포된 프론트엔드 도메인을 허용한다.
origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# ── 개인 소개 데이터 ────────────────────────────────────
# 프론트엔드(/)가 이 데이터를 GET /profile로 가져와 화면에 그린다.
PROFILE = {
    "name": "김선경 (SK Kim)",
    "headline": "공급망 리스크를 지속가능성·기후(Sustainability & Climate)의 렌즈로 다시 읽습니다.",
    "role": {
        "company": "MSCI Inc.",
        "title": "이사 · Research & Development",
        "location": "서울",
        "period": "2017 — 현재",
        "description": "공급망(Supply Chain) 리스크를 지속가능성·기후 관점과 연계해 분석하며, 글로벌 연기금과 자산운용사를 대상으로 한 리서치 자료 발간과 engagement로 연결하고 있습니다.",
    },
    "education": [
        {"school": "KAIST 경영전문대학원", "detail": "디지털금융 MBA · 7기", "period": "2025 — 재학 중"},
        {"school": "Shanghai Advanced Institute of Finance (SAIF)", "detail": "Shanghai Jiao Tong University · 석사", "period": "2015 — 2017"},
        {"school": "이화여자대학교", "detail": "영어영문학, 경영학 전공", "period": "2010 — 2015"},
    ],
    "publications": [
        {
            "title": "Do You Know the Real Geographic Exposure of Your Portfolio?",
            "summary": "지수 구성상 국가 비중과 매출·공급망 기준 실제 익스포저의 차이를 분석 (MSCI, 2026.06)",
            "url": "https://www.msci.com/research-and-insights/quick-take/do-you-know-the-real-geographic-exposure-of-your-portfolio",
        },
        {
            "title": "Hormuz Disruption Highlights Supply Chain Risk in Fertilizer Stocks",
            "summary": "호르무즈 해협 이슈가 질소비료 공급망에 미친 영향과 기업별 리스크 노출 분석 (MSCI, 2026.05)",
            "url": "https://www.msci.com/research-and-insights/quick-take/hormuz-disruption-highlights-supply-chain-risk-in-fertilizer-stocks",
        },
    ],
    "interests": ["Sustainability & Climate", "공급망 데이터", "AI & 풀스택 개발", "부동산", "정치"],
    "links": {
        "github": "https://github.com/skk1001072",
        "linkedin": "https://www.linkedin.com/in/skkim15/",
    },
}


@app.get("/profile")
def get_profile():
    return PROFILE
