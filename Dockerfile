#dockerイメージを指定。
FROM python:3.9-slim
RUN apt-get -y update && apt-get -y upgrade

WORKDIR /


RUN mkdir app

COPY app/ app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENV DATABASE_URL=postgresql://postgres:postgres@db:5432/db 
# ?schema=postgres

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]