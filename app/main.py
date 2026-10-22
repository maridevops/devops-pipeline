import os

from fastapi import FastAPI

app = FastAPI(title="DevOps Pipeline API", version="1.0.0")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Minha pipeline DevOps esta funcionando!"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/version")
def version() -> dict[str, str]:
    return {"version": os.getenv("APP_VERSION", "local")}
