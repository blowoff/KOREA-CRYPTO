from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# 🔹 최신 데이터 저장 (메모리 변수)
latest_data = {"balance": None, "timestamp": None}

@app.route('/webhook', methods=['POST'])
def webhook():
    """트레이딩뷰 웹훅에서 데이터를 받아 저장하는 엔드포인트"""
    global latest_data
    try:
        data = request.json
        latest_data["balance"] = data.get("balance", 0)
        latest_data["timestamp"] = data.get("timestamp", 0)
        return jsonify({"status": "success", "message": "Data received"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/data/bithumb_krw', methods=['GET'])
def get_data():
    """저장된 최신 데이터를 반환하는 엔드포인트"""
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
