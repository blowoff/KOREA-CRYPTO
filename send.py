from flask import Flask, send_file

app = Flask(__name__)

CSV_FILE_PATH = "bithumb_krw.csv"

@app.route("/data/bithumb_krw.csv")
def get_csv():
    """ 저장된 CSV 파일을 제공하는 엔드포인트 """
    return send_file(CSV_FILE_PATH, as_attachment=True, mimetype="text/csv")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
