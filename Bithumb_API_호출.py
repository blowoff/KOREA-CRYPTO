from flask import Flask, jsonify
import requests

app = Flask(__name__)  # ✅ Flask 애플리케이션 생성

def fetch_bithumb_data():
    url = "https://gw.bithumb.com/exchange/v1/trade/accumulation/deposit/C0100-C0100"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('data', {})
    return None

@app.route('/')
def home():
    return "Bithumb API Data Server is running!"

@app.route('/bithumb-data')
def get_data():
    data = fetch_bithumb_data()
    if data:
        return jsonify(data)
    return jsonify({"error": "Failed to fetch data"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)  # ✅ Flask 앱 실행
