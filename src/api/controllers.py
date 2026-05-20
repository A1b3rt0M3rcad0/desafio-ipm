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
from src.services.user_services import DeleteUser
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


class ReadUserController(BaseController):

    def __init__(self, read_user_service: ReadUser) -> None:
        self.__read_user_service = read_user_service

    async def handle(self, request: HttpRequest[ReadUserDTO]) -> Union[HttpResponse[UserOutput], HttpResponse[ErrorDTO]]:
        try:
            body = ReadUserDTO.model_validate(request.body)
            result = await self.__read_user_service.execute(data=body)
            if result is None:
                return HttpResponse[ErrorDTO](
                    status_code=404,
                    body=ErrorDTO(
                        message="User not found",
                        error="User not found"
                    )
                )
            return HttpResponse[UserOutput](
                status_code=200,
                body=result
            )
        except Exception as e:
            return HttpResponse[ErrorDTO](
                status_code=500,
                body=ErrorDTO(
                    message="Error reading user",
                    error=str(e)
                )
            )


class UpdateUserController(BaseController):

    def __init__(self, update_user_service: UpdateUser) -> None:
        self.__update_user_service = update_user_service

    async def handle(self, request: HttpRequest[UpdateUserDTO]) -> Union[HttpResponse[UserOutput], HttpResponse[ErrorDTO]]:
        try:
            body = UpdateUserDTO.model_validate(request.body)
            result = await self.__update_user_service.execute(data=body)
            if result is None:
                return HttpResponse[ErrorDTO](
                    status_code=404,
                    body=ErrorDTO(
                        message="User not found",
                        error="User not found"
                    )
                )
            return HttpResponse[UserOutput](
                status_code=200,
                body=result
            )
        except Exception as e:
            return HttpResponse[ErrorDTO](
                status_code=500,
                body=ErrorDTO(
                    message="Error updating user",
                    error=str(e)
                )
            )


class DeleteUserController(BaseController):

    def __init__(self, delete_user_service: DeleteUser) -> None:
        self.__delete_user_service = delete_user_service

    async def handle(self, request: HttpRequest[DeleteDTO]) -> Union[HttpResponse[DeleteUserOutputDTO], HttpResponse[ErrorDTO]]:
        try:
            body = DeleteDTO.model_validate(request.body)
            result = await self.__delete_user_service.execute(data=body)
            return HttpResponse[DeleteUserOutputDTO](
                status_code=200,
                body=result
            )
        except Exception as e:
            return HttpResponse[ErrorDTO](
                status_code=500,
                body=ErrorDTO(
                    message="Error deleting user",
                    error=str(e)
                )
            )