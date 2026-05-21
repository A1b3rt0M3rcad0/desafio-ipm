"""Factory de criação de AsyncEngine do SQLAlchemy."""

from src.infra.config.url_connections import BaseUrlConnection
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from typing import Type

class CreateEngine:

    @staticmethod
    def create(url:Type[BaseUrlConnection]) -> AsyncEngine:
        """Cria uma AsyncEngine do SQLAlchemy a partir da estratégia de URL fornecida."""
        return create_async_engine(url=url.get_url())
