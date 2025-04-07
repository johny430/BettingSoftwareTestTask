FROM python:3.10

WORKDIR /bet_app

COPY requirements.txt .

ENV PYTHONPATH=/bet_app

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .