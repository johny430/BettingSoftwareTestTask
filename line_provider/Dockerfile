FROM python:3.10

WORKDIR /app

COPY line_provider/requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .