from flask import Flask, jsonify, send_from_directory
import requests
import csv
import os

app = Flask(__name__)

CSV_FILE_PATH = "data/bithumb_krw.csv"  # CSV 저장 경로
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

            return {"success": True, "message": "CSV 저장 완료"}
        else:
            return {"success": False, "error": "API 요청 실패"}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.route("/update_csv", methods=["GET"])
def update_csv():
    """ CSV 데이터를 업데이트하는 API """
    result = fetch_bithumb_data()
    return jsonify(result)

@app.route("/data/bithumb_krw.csv", methods=["GET"])
def get_csv():
    """ CSV 파일을 제공하는 API """
    return send_from_directory("data", "bithumb_krw.csv", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
