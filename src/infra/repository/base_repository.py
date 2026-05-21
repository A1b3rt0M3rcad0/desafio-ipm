"""Interface genérica de repositório com operações CRUD abstratas."""

from typing import Generic, TypeVar, Optional
from abc import ABC, abstractmethod
from uuid import UUID

T = TypeVar("T")

class BaseRepository(ABC, Generic[T]):

    @abstractmethod
    async def create(self, entity:T) -> T:...

    @abstractmethod
    async def read(self, id:UUID) -> T:...

    @abstractmethod
    async def update(self, entity:T) -> T:...

    @abstractmethod
    async def delete(self, id:UUID) -> None:...