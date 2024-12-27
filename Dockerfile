FROM python:3.11.8-slim-bullseye AS builder

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1

#
RUN pip install poetry==1.7.1

#
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

#
WORKDIR /app
# 
COPY pyproject.toml poetry.lock README.md ./

#
RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

FROM python:3.11.8-slim-bullseye AS runtime 

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh
COPY app ./app
COPY .env.docker ./.env

CMD ["/bin/sh", "-c", "./docker-entrypoint.sh"]