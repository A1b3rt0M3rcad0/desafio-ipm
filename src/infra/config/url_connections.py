from abc import ABC, abstractmethod

class BaseUrlConnection(ABC):

    @abstractmethod
    @classmethod
    def get_url(cls) -> str:...


class SQLiteUrlConnetion(BaseUrlConnection):
    url = "sqlite+aiosqlite:///sqlite.db"

    @classmethod
    def get_url(cls) -> str:
        return cls.url