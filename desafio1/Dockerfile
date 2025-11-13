FROM python:3.10-slim

WORKDIR /app

COPY app/server.py /app/server.py
COPY client/requester.sh /app/requester.sh

RUN pip install flask && apt-get update && apt-get install -y curl

CMD ["python", "server.py"]
