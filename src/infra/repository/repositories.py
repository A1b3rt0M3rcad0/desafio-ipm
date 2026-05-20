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
        session = self.__session_manager.session
        model = UserModel(**entity.model_dump(mode="python"))
        session.add(model)
        await session.flush()
        await session.refresh(model)
        return UserEntity.model_validate(model)

    async def read(self, id:UUID) -> Optional[UserEntity]:
        session = self.__session_manager.session
        model = await session.get(UserModel, id)
        if model is None:
            return None
        return UserEntity.model_validate(model)
    
    async def update(self, entity: UserEntity) -> UserEntity:
        session = self.__session_manager.session
        model = await session.get(UserModel, entity.id)
        if model is None:
            raise LookupError(f"User {entity.id} not found")

        model.name = entity.name
        model.email = entity.email
    
        await session.flush()
        await session.refresh(model)
        return UserEntity.model_validate(model)
    
    async def delete(self, id: UUID) -> None:
        session = self.__session_manager.session
        model = await session.get(UserModel, id)
        if model is None:
            raise LookupError(f"User {id} not found")
        await session.delete(model)
        await session.flush()
        
