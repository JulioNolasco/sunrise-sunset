
# Use a imagem base do Python
FROM python:3.11.3

WORKDIR /app
COPY ./poetry.lock pyproject.toml /app/
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev
COPY . .
EXPOSE ${APP_PORT}
CMD ["flask", "run", "--host", "0.0.0.0"]

