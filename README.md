# memo-backend

FastAPI로 구현한 메모 CRUD API입니다. 데이터는 인메모리(파이썬 리스트)에 저장됩니다.

## 프로젝트 소개

- `GET /memos`, `POST /memos`, `DELETE /memos/{id}` 세 개의 엔드포인트를 제공합니다.
- [memo-frontend](https://github.com/skk1001072/memo-frontend)에서 이 API를 호출해 메모를 조회·추가·삭제합니다.

## 주요 구성

| 파일 | 내용 |
| --- | --- |
| `main.py` | FastAPI 앱, CORS 설정, 엔드포인트 3종 |
| `requirements.txt` | 의존성 목록 |

## 로컬 실행

```bash
python -m venv .venv
.venv\Scripts\activate        # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
fastapi dev main.py
```

`http://127.0.0.1:8000/docs`에서 Swagger UI로 API를 테스트할 수 있습니다.

## 환경변수

- `ALLOWED_ORIGINS`: CORS 허용 출처(콤마로 구분). 배포 시 Vercel 프론트엔드 주소를 등록합니다.
  예: `https://memo-frontend.vercel.app`

## 배포 주소

- Render(Swagger UI): https://memo-backend-17xm.onrender.com/docs
- 프론트엔드: https://memo-frontend-kohl.vercel.app
- 프론트엔드 저장소: https://github.com/skk1001072/memo-frontend
