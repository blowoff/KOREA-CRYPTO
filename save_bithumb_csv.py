import requests
import csv
import os

# CSV 파일 경로
CSV_FILE_PATH = "data/bithumb_krw.csv"
API_URL = "https://gw.bithumb.com/exchange/v1/trade/accumulation/deposit/C0100-C0100"

def fetch_bithumb_data():
    """ Bithumb API에서 데이터를 가져와 CSV로 저장 """
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json().get("data", {})

            # 데이터 필드 추출
            coin_type = data.get("coinType", "N/A")
            deposit_amount = data.get("accumulationDepositAmt", 0)
            deposit_change_rate = data.get("depositChangeRate", 0)
            timestamp = data.get("timestamp", "N/A")

            # CSV 저장
            os.makedirs("data", exist_ok=True)
            with open(CSV_FILE_PATH, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["timestamp", "coinType", "depositAmount", "depositChangeRate"])
                writer.writerow([timestamp, coin_type, deposit_amount, deposit_change_rate])

            print(f"✅ CSV 저장 완료: {CSV_FILE_PATH}")
        else:
            print(f"🚨 API 요청 실패: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"🚨 오류 발생: {str(e)}")

if __name__ == "__main__":
    fetch_bithumb_data()
