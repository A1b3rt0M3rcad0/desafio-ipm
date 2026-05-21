# desafio-ipm

API REST desenvolvida com **FastAPI** para gerenciamento de usuários e predições com modelo de Random Forest.

## Stack

- **FastAPI** + Uvicorn (servidor ASGI)
- **SQLAlchemy** (async) com Alembic (migrações)
- **PostgreSQL** (produção) ou **SQLite** (dev local)
- **JWT** (HS256) para autenticação
- **scikit-learn** (RandomForest) para predições

## Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) e Docker Compose

  **ou**

- Python 3.14+ e [uv](https://docs.astral.sh/uv/)

## Como iniciar

### Com Docker

```bash
cp env .env
docker compose up --build
```

### Local (desenvolvimento)

#### Baixe o uv antes de iniciar

```bash
cp env .env
uv sync
uv run python main.py
```

A API estará disponível em `http://localhost:8080`.

## Configuração

Tudo já está pré-configurado. Basta copiar o arquivo `env` para `.env`:

```bash
cp env .env
```

O `.env` já está ajustado para usar **SQLite** (`USE_SQLITE=1`).
Caso queira rodar com docker coloque o (`USE_SQLITE=0`)

### Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/users/login` | Login (público) — retorna token JWT |
| `POST` | `/users/create_user` | Criar usuário |
| `GET` | `/users/read_user` | Buscar usuário por ID |
| `PATCH` | `/users/update_user` | Atualizar usuário |
| `DELETE` | `/users/delete_user` | Remover usuário |
| `POST` | `/users/ml_prediction` | Predição do modelo ML |

### Credenciais padrão

- **Email:** `admin@gmail.com`
- **Senha:** `password`

> Os demais endpoints exigem autenticação via header `Authorization: Bearer <token>`.

### Docs

Acesse a rota `/docs` para acessar o Swagger

## Observações sobre a entrega

Todas as respostas, justificativas técnicas e explicações referentes às etapas do projeto estão documentadas no notebook `notebooks/prova.ipynb`.

O notebook contém o desenvolvimento das análises, decisões tomadas, explicações dos códigos implementados e respostas às questões propostas durante o desafio.

Quanto à persistência dos dados em volumes, optei por não incluí-la nesta entrega por se tratar de um desafio simples, cujo foco principal é a configuração e execução do ambiente da aplicação.