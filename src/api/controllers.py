from typing import Union
from abc import ABC, abstractmethod
from src.api.http import HttpRequest, HttpResponse
from src.services.user_services import UserOutput
from src.services.user_services import CreateUser
from src.services.user_services import CreateUserDTO
from src.services.user_services import ReadUser
from src.services.user_services import ReadUserDTO
from src.services.user_services import UpdateUser
from src.services.user_services import UpdateUserDTO
from src.services.user_services import DeleteDTO
from src.services.user_services import DeleteUserOutputDTO
from pydantic import BaseModel

class ErrorDTO(BaseModel):
    message:str
    error:str

class BaseController(ABC):

    @abstractmethod
    async def handle(self, request:HttpRequest) -> HttpResponse:...


class CreateUserController(BaseController):

    def __init__(self, create_user_service:CreateUser) -> None:
        self.__create_user_service = create_user_service
    
    async def handle(self, request: HttpRequest[CreateUserDTO]) -> Union[HttpResponse[UserOutput], HttpResponse[ErrorDTO]]:
        try:
            body = CreateUserDTO.model_validate(request.body)
            result = await self.__create_user_service.execute(data=body)
            return HttpResponse[UserOutput](
                status_code=201,
                body=result
            )
        except Exception as e:
            result = ErrorDTO(
                message="User not created",
                error=str(e)
            )
            return HttpResponse[ErrorDTO](
                status_code=500,
                body=result
            )