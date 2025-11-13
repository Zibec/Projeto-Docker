Desafio 4 — Microsserviços Independentes

Objetivo
Criar dois microsserviços independentes que se comunicam entre si via HTTP, sem uso de API Gateway e sem Docker Compose. Cada serviço possui sua própria imagem Docker e executa individualmente através de docker run.

Este desafio demonstra:
- Comunicação entre serviços via rede Docker.
- Isolamento por container.
- Uso de hostnames internos na rede.
- API em Flask (Python).

Arquitetura da Solução

desafio4/
├── servicoA/
│   ├── app.py
│   └── Dockerfile
└── servicoB/
    ├── app.py
    └── Dockerfile

Serviço A (API de Usuários)
- Porta interna: 5001
- Endpoint: /usuarios
- Retorna uma lista fixa de usuários em JSON.

Serviço B (Consumidor)
- Porta interna: 5002
- Endpoint: /
- Consome o Serviço A via HTTP usando o hostname interno servicoA:5001
- Renderiza uma página HTML com os usuários.

Execução dos Serviços (PowerShell)

1. Criar rede
docker network create rede-ms

2. Serviço A
docker build -t servico-a .
docker run -d --name servicoA --network rede-ms -p 5001:5001 servico-a

3. Serviço B
docker build -t servico-b .
docker run -d --name servicoB --network rede-ms -p 5002:5002 servico-b

Acessos:
Serviço A: http://localhost:5001/usuarios
Serviço B: http://localhost:5002

Finalização
docker stop servicoA servicoB
docker rm servicoA servicoB
docker network rm rede-ms
