import requests
import pandas as pd
import os

# API 요청 URL
API_URL = "https://gw.bithumb.com/exchange/v1/trade/accumulation/deposit/C0100-C0100"
CSV_FILE_PATH = "bithumb_krw.csv"  # 저장할 CSV 파일명

def fetch_bithumb_data():
    """ 빗썸 API에서 데이터 가져오기 """
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return data["data"]
    else:
        print("Error fetching data")
        return None

def save_data_to_csv():
    """ API 데이터를 가져와 CSV 파일로 저장 """
    data = fetch_bithumb_data()
    if data:
        df = pd.DataFrame([data])  # 데이터를 DataFrame으로 변환
        df.to_csv(CSV_FILE_PATH, index=False, encoding="utf-8-sig")  # CSV로 저장
        print(f"✅ CSV 저장 완료: {CSV_FILE_PATH}")

if __name__ == "__main__":
    save_data_to_csv()
