"""Casos de uso de CRUD de usuários com DTOs de entrada e saída."""

from typing import Optional
from src.domain.entity.user import User
from src.infra.repository.base_repository import BaseRepository
from pydantic import BaseModel
from uuid import UUID

#################
###### User #####
#################

class CreateUserDTO(BaseModel):
    name:str
    email:str

class UserOutput(BaseModel):
    id:UUID|None
    name:str|None
    email:str|None

class CreateUser:

    def __init__(self, user_repositoty:BaseRepository[User]) -> None:
        self.__user_repositoty = user_repositoty

    async def execute(self, data:CreateUserDTO) -> UserOutput:
        """Cria um novo usuário e retorna os dados persistidos."""
        user =  User(name=data.name, email=data.email)
        user_entity = await self.__user_repositoty.create(user)
        return UserOutput(
            id=user_entity.id,
            name= user_entity.name,
            email=user_entity.email
        )


class ReadUserDTO(BaseModel):
    id:UUID

class ReadUser:

    def __init__(self, user_repositoty:BaseRepository[User]) -> None:
        self.__user_repositoty = user_repositoty

    async def execute(self, data:ReadUserDTO) -> Optional[UserOutput]:
        """Busca um usuário pelo ID e retorna seus dados ou None."""
        user_entity =  await self.__user_repositoty.read(id=data.id)
        if user_entity is None:
            return None
        return UserOutput(
            id=user_entity.id,
            name= user_entity.name,
            email=user_entity.email
        )

class UpdateUserDTO(BaseModel):
    id:UUID
    name:Optional[str] = None
    email:Optional[str] = None

class UpdateUser:

    def __init__(self, user_repository: BaseRepository[User]) -> None:
        self.__user_repository = user_repository

    async def execute(self, data: UpdateUserDTO) -> Optional[UserOutput]:
        """Atualiza um usuário existente com os campos fornecidos e retorna os dados atualizados."""
        current_user = await self.__user_repository.read(data.id)
        if current_user is None:
            return None
        update_data = data.model_dump(exclude_none=True)
        update_data.pop("id", None)
        updated_user = current_user.model_copy(update=update_data)
        user_entity = await self.__user_repository.update(updated_user)
        return UserOutput(
            id=user_entity.id,
            name=user_entity.name,
            email=user_entity.email,
        )

class DeleteUserOutputDTO(BaseModel):
    message:str
    result:bool

class DeleteDTO(BaseModel):
    id:UUID

class DeleteUser:
    
    def __init__(self, user_repositoty:BaseRepository[User]) -> None:
        self.__user_repositoty = user_repositoty
    
    async def execute(self, data:DeleteDTO) -> DeleteUserOutputDTO:
        """Remove um usuário pelo ID e retorna o resultado da operação."""
        user_id = await self.__user_repositoty.delete(data.id)
        if user_id:
            return DeleteUserOutputDTO(message="User deleted successfully", result=True)
        else:
            return DeleteUserOutputDTO(message="User not found", result=False)