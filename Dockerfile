# 공식 Python 이미지 사용 (버전에 따라 변경 가능)
FROM python:3.9

# 작업 디렉터리 설정
WORKDIR /app

# 필요한 파일 복사
COPY . /app

# 필요한 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# Gunicorn을 사용해 Flask 애플리케이션 실행
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "SEEDROUND1:app"]

FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "SEEDROUND1:app"]
