FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]
#CMD ["uvicorn", "src.drivers.rest.main:app", "--host", "0.0.0.0", "--port", "8001"]