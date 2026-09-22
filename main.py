from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()  # FastAPI 애플리케이션 인스턴스 생성

# ── CORS 설정 ──────────────────────────────────────────
# 브라우저는 다른 출처(도메인/포트)로의 요청을 기본 차단한다.
# 프론트(localhost:5173)에서 백엔드(localhost:8000)를 부르려면 허용이 필요.

import os
origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# ── 데이터 모델 (Pydantic v2) ──────────────────────────
class MemoIn(BaseModel):        # 요청 본문: 클라이언트가 보내는 데이터
    content: str
class MemoOut(BaseModel):       # 응답 본문: 서버가 돌려주는 데이터
    id: int
    content: str

# ── 인메모리 저장소 ────────────────────────────────────
memos: list[dict] = []          # 리스트에 저장(서버 재시작 시 사라짐)
next_id = 1

@app.get("/memos", response_model=list[MemoOut])
def list_memos():
    return memos                # 전체 메모 목록 반환

@app.post("/memos", response_model=MemoOut)
def create_memo(memo: MemoIn):
    global next_id
    new = {"id": next_id, "content": memo.content}
    memos.append(new)
    next_id += 1
    return new

@app.delete("/memos/{memo_id}")
def delete_memo(memo_id: int):
    global memos
    for m in memos:
        if m["id"] == memo_id:
            memos = [x for x in memos if x["id"] != memo_id]
            return {"ok": True}
    raise HTTPException(status_code=404, detail="Memo not found")