from flask import Flask, jsonify, send_from_directory
import os
import requests
import csv

app = Flask(__name__)

CSV_FILE_PATH = "data/bithumb_krw.csv"
API_URL = "https://gw.bithumb.com/exchange/v1/trade/accumulation/deposit/C0100-C0100"

# ✅ 서버 시작 시 CSV 자동 저장
def fetch_bithumb_data():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json().get("data", {})
            os.makedirs("data", exist_ok=True)
            with open(CSV_FILE_PATH, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["timestamp", "coinType", "depositAmount", "depositChangeRate"])
                writer.writerow([data.get("timestamp", "N/A"), data.get("coinType", "N/A"), data.get("accumulationDepositAmt", 0), data.get("depositChangeRate", 0)])
            print("✅ CSV 파일 저장 완료")
        else:
            print("🚨 API 요청 실패")
    except Exception as e:
        print(f"🚨 오류 발생: {e}")

fetch_bithumb_data()

@app.route("/data/bithumb_krw.csv", methods=["GET"])
def get_csv():
    return send_from_directory("data", "bithumb_krw.csv", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
