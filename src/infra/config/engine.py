from src.infra.config.url_connections import BaseUrlConnection
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

class CreateEngine:

    @staticmethod
    def create(url:BaseUrlConnection) -> AsyncEngine:
        return create_async_engine(url=url.get_url())
