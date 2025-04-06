FROM python:3.10

WORKDIR /app

COPY requirements.txt .

ENV PYTHONPATH=/app

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .