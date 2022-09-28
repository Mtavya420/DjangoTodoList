FROM python:3.10

WORKDIR /usr/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]