FROM python:3.12-slim

# Instala o uv copiando o binário oficial
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copia os arquivos de configuração primeiro para cache
COPY pyproject.toml uv.lock ./

# Sincroniza dependências de forma limpa
RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --frozen --no-dev

# Copia o restante do código da sua aplicação
COPY . .

# CRITICAL FIX: Remove qualquer pasta .venv antiga que tenha vindo da sua máquina local
RUN rm -rf .venv && uv sync --frozen --no-dev

# Expõe a porta padrão do FastAPI
EXPOSE 8000

# Executa usando a sintaxe de módulo (app.main:app) que resolve o erro de rota do FastAPI
CMD ["uv", "run", "fastapi", "run", "--host", "0.0.0.0", "--port", "8000"]

