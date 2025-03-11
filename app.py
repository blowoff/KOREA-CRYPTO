from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "bithumb_krw.json"

@app.route('/webhook', methods=['POST'])
def receive_webhook():
    try:
        data = request.json  # JSON 데이터 받기
        if not data or "balance" not in data:
            return jsonify({"error": "Invalid data"}), 400

        # 최신 데이터 저장
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)

        return jsonify({"message": "Data received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/data/bithumb_krw')
def get_data():
    if not os.path.exists(DATA_FILE):
        return jsonify({"error": "No data available"}), 404

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    return jsonify({
        "s": "ok",
        "d": [
            data["timestamp"],  # 시간
            data["balance"],  # 빗썸 원화 보유량
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
