## 1. 파이썬 공식 이미지를 베이스로 사용
#FROM python:3.11
#
## 2. 작업 디렉토리 설정
#WORKDIR /home/
#
#COPY . .
#
#WORKDIR /home/Pinterest
#
## 먼저 의존성 파일을 복사하여 캐시 효율을 높임
#COPY requirements.txt .
#RUN apt-get update && apt-get install -y default-mysql-client
#RUN pip install --upgrade pip
#RUN pip install --no-cache-dir -r requirements.txt
#
#RUN echo "SECRET_KEY=django-insecure-x^(odz3e-hyi*043imunwhw)7^yh_j92wn7h7we%t^@sxd@=&u" > .env
#
#COPY . .
#
#EXPOSE 8000
#
## CMD 명령어는 단일 실행 파일로
#CMD ["gunicorn", "pragmetic.wsgi", "--env", "DJANGO_SETTINGS_MODULE=pragmetic.settings.deploy", "--bind", "0.0.0.0:8000"]
##CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--env", "DJANGO_SETTINGS_MODULE=pragmetic.settings.deploy", "pragmetic.wsgi:application"]
##CMD ["bash", "-c", "python manage.py migrate --settings=pragmetic.settings.deploy && gunicorn pragmetic.wsgi --env DJANGO_SETTINGS_MODULE=pragmetic.settings.deploy --bind 0.0.0.0:8000"]


# 1. 베이스 이미지 선택 (가벼운 slim 버전 권장)
FROM python:3.11-slim

# 2. 시스템 패키지 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

# 3. 작업 디렉토리 설정 (요청하신 경로로 지정)
WORKDIR /home/Pinterest

# 4. 의존성 파일만 먼저 복사 (빌드 캐시 최적화)
# requirements.txt가 변경되지 않으면, 아래 pip install 과정은 캐시를 사용해 빌드 속도가 빨라집니다.
COPY requirements.txt .

# 5. 파이썬 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 6. 나머지 프로젝트 소스 코드 복사
# 코드가 변경되어도 위 패키지 설치 단계는 다시 실행하지 않습니다.
COPY . .

# 7. 포트 노출
EXPOSE 8000

# 8. Gunicorn 실행
CMD ["gunicorn", "pragmetic.wsgi", "--env", "DJANGO_SETTINGS_MODULE=pragmetic.settings.deploy", "--bind", "0.0.0.0:8000"]