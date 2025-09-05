# 1. 파이썬 공식 이미지를 베이스로 사용
FROM python:3.11

# 2. 작업 디렉토리 설정
WORKDIR /home/Pinterest

# 3. 필요한 파일 복사 및 패키지 설치
# 먼저 의존성 파일을 복사하여 캐시 효율을 높임
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 5. 프로젝트 소스 코드 복사
# 의존성 설치 후 소스 코드를 복사하여 불필요한 빌드를 줄임
COPY . .

# 6. 환경 변수 파일 생성
# 컨테이너 실행 시 .env 파일을 사용하지 않는다면 필요 없음
# docker-compose.yml에서 환경변수를 직접 주입하는 것을 권장
RUN echo "SECRET_KEY=django-insecure-x^(odz3e-hyi*043imunwhw)7^yh_j92wn7h7we%t^@sxd@=&u" > .env


# 7. 포트 노출
EXPOSE 8000

# 8. 컨테이너 실행 명령어
# CMD 명령어는 단일 실행 파일로
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--env", "DJANGO_SETTINGS_MODULE=pragmetic.settings.deploy", "pragmetic.wsgi:application"]

CMD ["bash", "-c", "python manage.py migrate --settings=pragmetic.settings.deploy && gunicorn pragmetic.wsgi --env DJANGO_SETTINGS_MODULE=pragmetic.settings.deploy --bind 0.0.0.0:8000"]