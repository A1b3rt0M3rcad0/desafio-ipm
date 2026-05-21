"""Instância principal do FastAPI e registro de rotas."""

from fastapi import FastAPI
from src.api.routes import router as user_router

app = FastAPI()
app.include_router(user_router)