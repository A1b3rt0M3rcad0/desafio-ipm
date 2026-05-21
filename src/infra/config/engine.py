from src.infra.config.url_connections import BaseUrlConnection
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from typing import Type

class CreateEngine:

    @staticmethod
    def create(url:Type[BaseUrlConnection]) -> AsyncEngine:
        return create_async_engine(url=url.get_url())
