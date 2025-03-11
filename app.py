from flask import Flask, request, jsonify, send_from_directory
import os
import json

app = Flask(__name__)

# 🔹 최신 데이터 저장 (메모리 변수)
latest_data = {"balance": None, "timestamp": None}


# ✅ 트레이딩뷰 웹훅에서 데이터를 받아 저장
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


# ✅ 최신 웹훅 데이터를 반환하는 API
@app.route('/data/bithumb_krw', methods=['GET'])
def get_data():
    """저장된 최신 데이터를 반환하는 엔드포인트"""
    return jsonify(latest_data)


# ✅ JSON 데이터 제공하는 API 추가
@app.route('/data/bithumb_krw.json', methods=['GET'])
def get_json():
    """JSON 데이터를 반환하는 API"""
    json_file_path = "data/bithumb_krw.json"
    if os.path.exists(json_file_path):
        return send_from_directory("data", "bithumb_krw.json", as_attachment=True)
    else:
        return jsonify({"error": "JSON 파일이 존재하지 않습니다."}), 404


# ✅ Flask 서버 실행
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)  debug=True
