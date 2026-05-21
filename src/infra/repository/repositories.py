"""Implementação concreta do repositório de usuários com SQLAlchemy."""

from typing import Optional
from uuid import UUID
from src.domain.entity.user import User as UserEntity
from src.infra.config.session_manager import SessionManager
from src.infra.repository.base_repository import BaseRepository
from src.infra.model.models import User as UserModel

class UserRepository(BaseRepository[UserEntity]):

    def __init__(self, session_manager:SessionManager) -> None:
        self.__session_manager = session_manager
    
    async def create(self, entity: UserEntity) -> UserEntity:
        """Insere um novo usuário no banco e retorna a entidade persistida."""
        session = self.__session_manager.session
        model = UserModel(**entity.model_dump(mode="python"))
        session.add(model)
        await session.flush()
        await session.refresh(model)
        return UserEntity.model_validate(model)

    async def read(self, id:UUID) -> Optional[UserEntity]:
        """Busca um usuário pelo ID e retorna a entidade ou None."""
        session = self.__session_manager.session
        model = await session.get(UserModel, id)
        if model is None:
            return None
        return UserEntity.model_validate(model)
    
    async def update(self, entity: UserEntity) -> UserEntity:
        """Atualiza os campos de um usuário existente e retorna a entidade atualizada."""
        session = self.__session_manager.session
        model = await session.get(UserModel, entity.id)
        if model is None:
            raise LookupError(f"User {entity.id} not found")

        if entity.name is not None:
            model.name = entity.name
        if entity.email is not None:
            model.email = entity.email
    
        await session.flush()
        await session.refresh(model)
        return UserEntity.model_validate(model)
    
    async def delete(self, id: UUID) -> Optional[UUID]:
        """Remove um usuário pelo ID e retorna o ID removido ou None."""
        session = self.__session_manager.session
        model = await session.get(UserModel, id)
        if model is None:
            return None
        await session.delete(model)
        await session.flush()
        return id
