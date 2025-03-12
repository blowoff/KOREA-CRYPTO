from flask import Flask, request, jsonify, send_file
import os
import json

app = Flask(__name__)

# 🔹 JSON 데이터 저장 경로
JSON_FILE_PATH = "data/bithumb_krw.json"

@app.route('/data/bithumb_krw.json', methods=['GET'])
def get_json():
    """ JSON 데이터 반환 """
    if os.path.exists(JSON_FILE_PATH):
        return send_file(JSON_FILE_PATH, mimetype='application/json')
    else:
        return jsonify({"error": "JSON 파일이 존재하지 않습니다."}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
