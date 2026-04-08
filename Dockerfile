FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn pydantic openenv-core

EXPOSE 7860

CMD ["python", "-m", "server.app"]