Projeto — Desafios de Docker e Microsserviços

Introdução
Este repositório contém a resolução de cinco desafios práticos envolvendo Docker, redes de containers, persistência, orquestração manual e arquitetura baseada em microsserviços.

Objetivos Gerais do Projeto
1. Demonstrar entendimento sobre criação e execução de containers.
2. Comprovar domínio de redes Docker e comunicação entre serviços.
3. Aplicar persistência com volumes Docker.
4. Orquestrar múltiplos serviços manualmente via CLI.
5. Estruturar aplicações em microsserviços com isolamento.
6. Implementar API Gateway de forma manual.
7. Produzir documentação técnica padronizada.

Sumário dos Desafios

Desafio 1 — Containers em Rede
Implementação de dois containers comunicando-se em rede Docker personalizada. Um serviço expõe uma API Flask, e outro realiza requisições periódicas.

Desafio 2 — Volumes e Persistência
Container executando SQLite com arquivo de banco persistido em volume Docker. Persistência comprovada após recriação do container.

Desafio 3 — Múltiplos Serviços em Rede
Simulação de aplicação com três serviços: API Flask, PostgreSQL e Redis, conectados manualmente por rede Docker. A aplicação registra acessos no banco e contabiliza visitas no Redis.

Desafio 4 — Microsserviços Independentes
Dois microsserviços Flask comunicando-se via HTTP, cada um com imagem Docker própria. Comunicação usando hostnames internos.

Desafio 5 — Microsserviços com API Gateway
Arquitetura com três serviços: usuários, pedidos e gateway. Gateway atua como ponto único de entrada e realiza chamadas internas. Todos executados manualmente via Docker CLI.

Estrutura Geral do Repositório
Projeto2-Docker/
├── desafio1/
├── desafio2/
├── desafio3/
├── desafio4/
└── desafio5/

Metodologia
1. Dockerfiles escritos manualmente.
2. Construção das imagens com docker build.
3. Criação explícita de redes com docker network create.
4. Execução manual dos containers via docker run.
5. Testes realizados com curl, navegador ou logs.
6. Documentação individual por desafio.

Decisões Técnicas Gerais
- Python + Flask para APIs simples e rápidas.
- Hostnames de containers usados para comunicação interna.
- Volumes nomeados para persistência e isolamento.
- Dockerfiles separados para reforçar independência entre serviços.
- Ausência de Docker Compose para aprofundar entendimento manual da orquestração.

Conclusão
O repositório demonstra domínio prático sobre Docker, redes, volumes, execução manual de containers e arquitetura em microsserviços.
Todos os requisitos foram atendidos:
- Funcionamento técnico completo
- Documentação clara
- Estrutura organizada
- Originalidade e autoria preservadas
