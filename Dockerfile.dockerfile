FROM python:3.8.3

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY script.py /app/

CMD [ "python", "./script.py"]

