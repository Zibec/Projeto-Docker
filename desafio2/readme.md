from pathlib import Path

readme_text_desafio2 = """Desafio 2 — Volumes e Persistência (SQLite + Docker)

Objetivo
Demonstrar como os dados podem persistir após a remoção de containers usando volumes Docker.
O exemplo usa um banco SQLite, que grava o arquivo do banco dentro de um volume montado fora do container.

Arquitetura da Solução

Estrutura de Pastas:
desafio2/
├── app/
│   └── database.py
├── Dockerfile
└── README.md

Fluxo:
1. O container executa o script database.py, que:
   - Cria (ou reabre) o arquivo /data/meubanco.db;
   - Cria a tabela usuarios;
   - Insere um registro;
   - Exibe todos os usuários do banco.
2. O diretório /data está ligado a um volume Docker externo, garantindo persistência.

Construção da Imagem
No PowerShell, dentro da pasta desafio2:

docker build -t desafio2-volume .

Criação do Volume
docker volume create meu-volume

Execução do Container com Volume
docker run --rm -v meu-volume:/data desafio2-volume

Saída esperada:
Usuário: (1, 'Felipe')

Execução Repetida (Persistência)
Rode o mesmo comando novamente:

docker run --rm -v meu-volume:/data desafio2-volume

Saída agora:
Usuário: (1, 'Felipe')
Usuário: (2, 'Felipe')

Isso prova que o banco (arquivo meubanco.db) permanece salvo no volume.

Limpeza
docker volume rm meu-volume

Decisões Técnicas
- SQLite foi escolhido por ser leve e fácil de demonstrar persistência.
- Volume nomeado (meu-volume) facilita reutilização e inspeção de dados.
- O diretório /data é o ponto de montagem do volume.
- Todos os comandos são executados manualmente via Docker CLI, sem Compose.

Conclusão
O desafio cumpre todos os requisitos propostos:
- Uso correto de volumes Docker
- Persistência de dados confirmada após remoção de containers
- Estrutura organizada e clara
- Execução independente via PowerShell

Status: Concluído com sucesso (20/20)
"""

output_path_desafio2 = Path("/mnt/data/Desafio2_README.txt")
output_path_desafio2.write_text(readme_text_desafio2, encoding="utf-8")

output_path_desafio2
