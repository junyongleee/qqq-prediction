# Fastapi 엔트리 포인트 (라우터 등록)
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, QQQ Forecast!"}