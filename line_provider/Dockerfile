FROM python:3.10

WORKDIR /line_app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/"

COPY . .