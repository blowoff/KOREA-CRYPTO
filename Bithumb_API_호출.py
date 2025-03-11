import requests
import json

# 트레이딩뷰 Webhook URL (설정에서 Webhook URL 생성 후 입력)
TRADINGVIEW_WEBHOOK_URL = "https://your-tradingview-webhook-url"

# Bithumb API에서 데이터 가져오기
def fetch_bithumb_data():
    url = "https://gw.bithumb.com/exchange/v1/trade/accumulation/deposit/C0100-C0100"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('data', {})
    else:
        print("Error fetching data")
        return None

# 트레이딩뷰 Webhook으로 데이터 전송
def send_to_tradingview(data):
    if not data:
        print("No data to send")
        return

    payload = {
        "coinType": data.get("coinType", "Unknown"),
        "accumulationDepositAmt": data.get("accumulationDepositAmt", 0),
        "depositChangeRate": data.get("depositChangeRate", 0),
        "timestamp": data.get("timestamp", "")
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(TRADINGVIEW_WEBHOOK_URL, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        print("✅ 트레이딩뷰 Webhook 전송 성공!")
    else:
        print(f"❌ Webhook 전송 실패: {response.status_code}, {response.text}")

# 실행
data = fetch_bithumb_data()
send_to_tradingview(data)