# 1. 파이썬 공식 이미지를 베이스로 사용
FROM python:3.11

# 2. 작업 디렉토리 설정
WORKDIR /home/

COPY . .

WORKDIR /home/Pinterest

# 먼저 의존성 파일을 복사하여 캐시 효율을 높임
COPY requirements.txt .
RUN pip install mysqlclient
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-x^(odz3e-hyi*043imunwhw)7^yh_j92wn7h7we%t^@sxd@=&u" > .env

EXPOSE 8000

# CMD 명령어는 단일 실행 파일로
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--env", "DJANGO_SETTINGS_MODULE=pragmetic.settings.deploy", "pragmetic.wsgi:application"]
CMD ["bash", "-c", "python manage.py migrate --settings=pragmetic.settings.deploy && gunicorn pragmetic.wsgi --env DJANGO_SETTINGS_MODULE=pragmetic.settings.deploy --bind 0.0.0.0:8000"]