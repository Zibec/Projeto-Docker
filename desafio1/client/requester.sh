#!/bin/bash
echo "Cliente iniciado. Enviando requisições a cada 5 segundos..."

while true; do
  echo "→ Fazendo requisição..."
  curl http://webserver:8080
  echo ""
  sleep 5
done
