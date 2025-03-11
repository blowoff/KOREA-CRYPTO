# 공식 Python 3.9 이미지 사용
FROM python:3.9

# 작업 디렉터리 설정
WORKDIR /app

# 필요한 파일을 컨테이너 내부로 복사
COPY requirements.txt .  

# 필요한 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 전체 코드 복사
COPY . .

# Gunicorn을 사용해 Flask 애플리케이션 실행
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "Bithumb_API_호출:app"]
