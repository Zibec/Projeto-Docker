FROM python:3.10-slim

WORKDIR /app

COPY app/server.py /app/server.py

RUN pip install flask psycopg2-binary redis

CMD ["python", "server.py"]
