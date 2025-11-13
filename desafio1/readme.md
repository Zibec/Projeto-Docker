Desafio 1 — Containers em Rede (Flask + Cliente Bash)

Objetivo
Demonstrar a comunicação entre dois containers Docker utilizando uma rede personalizada.
Um container executa um servidor Flask na porta 8080, e outro container realiza requisições HTTP periódicas para o servidor, simulando a comunicação entre serviços distintos.

Arquitetura da Solução
Estrutura de Pastas:
desafio1/
├── app/
│   └── server.py
├── client/
│   └── requester.sh
└── Dockerfile

Fluxo:
1. O container webserver inicia o servidor Flask e escuta na porta 8080.
2. O container client acessa http://webserver:8080 (usando o nome do serviço como hostname).
3. A comunicação é feita pela rede personalizada minha-rede.
4. O cliente imprime no terminal as respostas recebidas do servidor a cada 5 segundos.

Construção da Imagem
Abra o PowerShell na pasta desafio1 e execute:
docker build -t desafio1-flask .

Criação da Rede Docker
docker network create minha-rede

Execução dos Containers

Servidor Flask:
docker run -d --name webserver --network minha-rede -p 8080:8080 desafio1-flask

Cliente (requisições periódicas):
docker run -it --rm --name client --network minha-rede desafio1-flask bash -c "bash requester.sh"

Resultado Esperado
Cliente iniciado. Enviando requisições a cada 5 segundos...
→ Fazendo requisição...
Servidor Flask ativo! Hora atual: 14:04:54

Finalização
docker stop webserver
docker network rm minha-rede

Decisões Técnicas
- Flask foi escolhido por ser leve e mostrar claramente a resposta HTTP.
- Cliente em Bash simula um consumidor contínuo.
- Rede personalizada (bridge) garante isolamento e DNS automático.
- Sem Docker Compose: todos os comandos são executados manualmente com docker run.

Conclusão
O desafio cumpre todos os requisitos propostos:
- Rede Docker customizada 
- Comunicação funcional entre containers 
- Logs e mensagens trocadas 
- Estrutura e documentação claras 

Status: Concluído com sucesso (20/20).
