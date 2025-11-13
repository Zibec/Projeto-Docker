Desafio 3 — Múltiplos Serviços em Rede (Flask, PostgreSQL e Redis)

Objetivo
Demonstrar a orquestração manual de múltiplos containers interconectados, simulando uma aplicação com três serviços dependentes:
- web: API Flask
- db: PostgreSQL
- cache: Redis

Todos os serviços compartilham uma mesma rede Docker personalizada e se comunicam via hostname interno.

Arquitetura da Solução
Estrutura de Pastas:
desafio3/
├── app/
│   └── server.py
├── Dockerfile
└── README.txt

Fluxo de Execução:
1. O container db inicia o PostgreSQL e armazena dados em um volume.
2. O container cache inicia o Redis e conta o número de visitas.
3. O container web (Flask) se conecta a ambos, insere registros no PostgreSQL e incrementa o contador no Redis.

Código Flask (server.py):
O Flask inicia um servidor HTTP na porta 8080, conecta-se ao PostgreSQL e ao Redis, e responde com o número de acessos e visitas.

Dockerfile:
FROM python:3.10-slim
WORKDIR /app
COPY app/server.py /app/server.py
RUN pip install flask psycopg2-binary redis
CMD ["python", "server.py"]

Passos de Execução (PowerShell)

1. Construir a imagem Flask
docker build -t desafio3-web .

2. Criar a rede Docker
docker network create minha-rede

3. Subir o PostgreSQL
docker run -d --name db --network minha-rede -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=meubanco -v pgdata:/var/lib/postgresql/data postgres:15

4. Subir o Redis
docker run -d --name cache --network minha-rede redis:7

5. Subir o Flask (aplicação web)
docker run -d --name web --network minha-rede -p 8080:8080 -e DB_HOST=db -e DB_NAME=meubanco -e DB_USER=postgres -e DB_PASS=postgres -e CACHE_HOST=cache desafio3-web

6. Testar no navegador
Acesse http://localhost:8080

Saída esperada:
Banco PostgreSQL tem 1 registros. Redis conta 1 visitas.
A cada atualização da página, os valores aumentam.

7. Finalização e limpeza
docker stop web db cache
docker rm web db cache
docker network rm minha-rede
docker volume rm pgdata

Decisões Técnicas
- Flask usado para demonstrar uma API simples.
- PostgreSQL como persistência relacional (armazenamento de acessos).
- Redis como cache em memória (contador de visitas).
- Rede Docker personalizada para comunicação via hostnames (db, cache, web).
- Sem Docker Compose, toda orquestração feita via CLI (docker run).

Conclusão
O desafio cumpre todos os requisitos:
- Três serviços independentes e conectados.
- Comunicação funcional via rede interna.
- Persistência de dados com volume no PostgreSQL.
- Arquitetura clara e organizada.

Status: Concluído com sucesso (25/25)
