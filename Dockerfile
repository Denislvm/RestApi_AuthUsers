FROM python:3.8

WORKDIR /usr/src/

COPY . .

RUN pip3 install virtualenv

RUN pip install psycopg2

RUN pip install django

RUN pip install djangorestframework

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]