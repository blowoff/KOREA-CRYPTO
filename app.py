from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/data/bithumb_krw.json')
def get_bithumb_data():
    # CSV 파일을 읽어 JSON으로 변환
    df = pd.read_csv('bithumb_krw.csv')
    data = df.iloc[-1].to_dict()  # 최신 데이터만 가져오기
    return jsonify(data)  # JSON 반환

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
