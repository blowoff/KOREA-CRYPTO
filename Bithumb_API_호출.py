import requests

def fetch_bithumb_data():
    url = "https://gw.bithumb.com/exchange/v1/trade/accumulation/deposit/C0100-C0100"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # API 응답 데이터를 JSON으로 파싱
        return data['data']
    else:
        print("Error fetching data")
        return None

# 데이터 출력 예시
data = fetch_bithumb_data()
if data:
    print(f"Coin Type: {data['coinType']}")
    print(f"Accumulation Deposit Amount: {data['accumulationDepositAmt']}")
    print(f"Deposit Change Rate: {data['depositChangeRate']}")
    print(f"Timestamp: {data['timestamp']}")
