
import csv
import json
import os

# CSV 파일 경로
csv_file_path = "/app/data/bithumb_krw.csv"
json_file_path = "/app/data/bithumb_krw.json"

# CSV 파일이 존재하는지 확인
if not os.path.exists(csv_file_path):
    print(f"🚨 CSV 파일이 존재하지 않습니다: {csv_file_path}")
    exit(1)

# CSV → JSON 변환
data = []
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

# JSON 파일 저장
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)

print(f"✅ 변환 완료: {json_file_path}")
