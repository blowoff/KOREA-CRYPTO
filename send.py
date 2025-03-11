import requests
import csv
import os

# API URL (빗썸 API 예제)
API_URL = "https://gw.bithumb.com/exchange/v1/trade/accumulation/deposit/C0100-C0100"
CSV_FILE_PATH = "/app/data/bithumb_krw.csv"

# API 호출
response = requests.get(API_URL)
if response.status_code == 200:
    data = response.json()

    # CSV 파일 생성
    with open(CSV_FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "balance"])
        
        # 예제 데이터 저장
        for entry in data["data"]:
            writer.writerow([entry["timestamp"], entry["accumulationDepositAmt"]])

    print(f"✅ CSV 파일 생성 완료: {CSV_FILE_PATH}")

else:
    print(f"🚨 API 요청 실패! 상태 코드: {response.status_code}")
