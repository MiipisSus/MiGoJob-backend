FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "MiGoJob.asgi:application", "--host", "0.0.0.0", "--port", "8000"]