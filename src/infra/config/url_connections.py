"""Estratégias de URL de conexão para SQLite e PostgreSQL."""

from abc import ABC, abstractmethod
import os

class BaseUrlConnection(ABC):

    @classmethod
    @abstractmethod
    def get_url(cls) -> str:...


class SQLiteUrlConnetion(BaseUrlConnection):
    url = "sqlite+aiosqlite:///sqlite.db"

    @classmethod
    def get_url(cls) -> str:
        """Retorna a URL de conexão SQLite."""
        return cls.url

class PostgresUrlConnection(BaseUrlConnection):
    postgres_user = os.getenv("POSTGRES_USER", "postgres")
    postgres_password = os.getenv("POSTGRES_PASSWORD", "password")
    postgres_host = os.getenv("POSTGRES_HOST", "postgres")
    postgres_port = os.getenv("POSTGRES_PORT", "5432")
    postgres_db = os.getenv("POSTGRES_DB", "ipm_db")

    url = (
        f"postgresql+psycopg://"
        f"{postgres_user}:{postgres_password}"
        f"@{postgres_host}:{postgres_port}/{postgres_db}"
    )

    @classmethod
    def get_url(cls) -> str:
        """Retorna a URL de conexão PostgreSQL."""
        return cls.url