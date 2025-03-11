from flask import Flask, request, jsonify
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

CSV_FILE = "bithumb_krw.csv"

# 🔹 웹훅 데이터 받기
@app.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.json
    if not data or "balance" not in data:
        return jsonify({"error": "Invalid data"}), 400

    # 📌 받은 데이터 저장 (CSV 파일 업데이트)
    new_data = pd.DataFrame([{
        "timestamp": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        "balance": data["balance"]
    }])

    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        df = pd.concat([df, new_data], ignore_index=True)
    else:
        df = new_data

    df.to_csv(CSV_FILE, index=False)
    return jsonify({"status": "success"}), 200

# 🔹 JSON 데이터 제공 (트레이딩뷰에서 가져갈 API)
@app.route('/data/bithumb_krw.json', methods=['GET'])
def get_json():
    if not os.path.exists(CSV_FILE):
        return jsonify({"error": "No data available"}), 404

    df = pd.read_csv(CSV_FILE)
    
    # 📌 TradingView에서 사용 가능한 JSON 포맷 변환
    data = {
        "s": "ok",
        "t": df["timestamp"].tolist(),
        "c": df["balance"].tolist()
    }
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
