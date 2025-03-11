# 공식 Python 이미지 사용
FROM python:3.9

# 작업 디렉터리 설정
WORKDIR /app

# 필요한 파일 복사
COPY . /app

# 필요한 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 데이터 저장 디렉터리 생성
RUN mkdir -p /app/data

# Gunicorn을
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "app:app"]
