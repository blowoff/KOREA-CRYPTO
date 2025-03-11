from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()  # JSON 데이터 받기
    print("Received Webhook Data:", data)

    # 여기에서 트레이딩뷰로 데이터를 보낼 수도 있음
    return {"message": "Webhook received successfully!"}
