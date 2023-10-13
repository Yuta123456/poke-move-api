#dockerイメージを指定。
FROM python:3.9-slim
RUN apt-get -y update && apt-get -y upgrade

WORKDIR /


RUN mkdir app

COPY src/ app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]