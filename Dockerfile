FROM python:3.11

WORKDIR /home/

COPY . .

WORKDIR /home/Pinterest

RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt

#위험함 지울 예정
RUN echo "SECRET_KEY=django-insecure-x^(odz3e-hyi*043imunwhw)7^yh_j92wn7h7we%t^@sxd@=&u" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn","pragmetic.wsgi", "--bind", "0.0.0.0:8000"]

