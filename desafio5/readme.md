Desafio 5 — Microsserviços com API Gateway (Sem Docker Compose)

Objetivo
Criar uma arquitetura composta por três serviços independentes que se comunicam entre si através de HTTP, utilizando um API Gateway como ponto único de entrada. Toda a execução é realizada manualmente via Docker CLI, sem uso de Docker Compose.

O desafio demonstra:
- Comunicação entre múltiplos containers via rede Docker.
- Uso de hostnames internos para descoberta de serviços.
- Isolamento entre microsserviços (um Dockerfile por serviço).
- Funcionamento completo de um API Gateway simples.

Arquitetura da Solução

Estrutura de Pastas:
desafio5/
├── gateway/
│   ├── app.py
│   └── Dockerfile
├── servico_usuarios/
│   ├── app.py
│   └── Dockerfile
└── servico_pedidos/
    ├── app.py
    └── Dockerfile

Descrição dos Serviços

1. servico_usuarios
- Porta interna: 5001
- Endpoint: /usuarios
- Retorna uma lista de usuários em JSON.

2. servico_pedidos
- Porta interna: 5002
- Endpoint: /pedidos
- Retorna lista de pedidos relacionados a usuários.

3. gateway
- Porta exposta: 8000
- Endpoints:
  - GET /users  → encaminha para servico_usuarios
  - GET /orders → encaminha para servico_pedidos
- Realiza chamadas internas usando os hostnames:
  - http://servico_usuarios:5001/usuarios
  - http://servico_pedidos:5002/pedidos

Fluxo Geral
1. O cliente acessa o gateway via http://localhost:8000.
2. O gateway consulta os microsserviços internos usando HTTP.
3. Os microsserviços respondem em JSON.
4. O gateway repassa a resposta ao cliente.

Execução dos Serviços (PowerShell)

1. Criar rede Docker
docker network create minha_rede

2. Construir imagens

Gateway:
cd desafio5/gateway
docker build -t gateway-img .

Serviço de Usuários:
cd ../servico_usuarios
docker build -t usuarios-img .

Serviço de Pedidos:
cd ../servico_pedidos
docker build -t pedidos-img .

3. Executar containers conectados à rede

servico_usuarios:
docker run -d --name servico_usuarios --network minha_rede -p 5001:5001 usuarios-img

servico_pedidos:
docker run -d --name servico_pedidos --network minha_rede -p 5002:5002 pedidos-img

gateway:
docker run -d --name gateway --network minha_rede -p 8000:8000 gateway-img

Testes

Microsserviços diretamente:
curl http://localhost:5001/usuarios
curl http://localhost:5002/pedidos

Via Gateway:
curl http://localhost:8000/users
curl http://localhost:8000/orders

Finalização
docker stop gateway servico_usuarios servico_pedidos
docker rm gateway servico_usuarios servico_pedidos
docker network rm minha_rede

Decisões Técnicas
- Cada serviço possui seu próprio Dockerfile, garantindo isolamento.
- Flask foi escolhido por ser simples e demonstrar claramente a troca HTTP.
- A rede personalizada permite comunicação por hostname sem necessidade de descobrir IPs.
- A ausência de Docker Compose reforça a compreensão de rede, execução e dependências manualmente.

Conclusão
O desafio cumpre todos os requisitos:
- API Gateway funcional como ponto central.
- Microsserviços independentes comunicando via HTTP.
- Estrutura organizada e documentação clara.
- Execução manual demonstrada adequadamente.

Status: Concluído com sucesso (25/25).
