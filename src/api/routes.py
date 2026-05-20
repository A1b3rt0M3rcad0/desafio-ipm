from typing import Annotated

from fastapi import Body, Request, APIRouter
from fastapi.responses import JSONResponse

from src.api.adapter import EmptyDTO, FastAPIAdapter
from src.api.composers import (
    create_user_composer,
    read_user_composer,
    update_user_composer,
    delete_user_composer,
)
from src.api.config import ENGINE
from src.infra.config.session_manager import SessionManager
from src.services.user_services import (
    CreateUserDTO,
    ReadUserDTO,
    UpdateUserDTO,
    DeleteDTO,
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/create_user")
async def create_user(
    request: Request,
    body: Annotated[CreateUserDTO, Body()],
) -> JSONResponse:
    async with SessionManager(ENGINE) as session_manager:
        controller = create_user_composer(session_manager)
        return await FastAPIAdapter.adapt(
            controller=controller,
            request=request,
            body_model=body,
            query_model=EmptyDTO(),
            path_model=EmptyDTO(),
        )


@router.post("/read_user")
async def read_user(
    request: Request,
    body: Annotated[ReadUserDTO, Body()],
) -> JSONResponse:
    async with SessionManager(ENGINE) as session_manager:
        controller = read_user_composer(session_manager)
        return await FastAPIAdapter.adapt(
            controller=controller,
            request=request,
            body_model=body,
            query_model=EmptyDTO(),
            path_model=EmptyDTO(),
        )


@router.post("/update_user")
async def update_user(
    request: Request,
    body: Annotated[UpdateUserDTO, Body()],
) -> JSONResponse:
    async with SessionManager(ENGINE) as session_manager:
        controller = update_user_composer(session_manager)
        return await FastAPIAdapter.adapt(
            controller=controller,
            request=request,
            body_model=body,
            query_model=EmptyDTO(),
            path_model=EmptyDTO(),
        )


@router.post("/delete_user")
async def delete_user(
    request: Request,
    body: Annotated[DeleteDTO, Body()],
) -> JSONResponse:
    async with SessionManager(ENGINE) as session_manager:
        controller = delete_user_composer(session_manager)
        return await FastAPIAdapter.adapt(
            controller=controller,
            request=request,
            body_model=body,
            query_model=EmptyDTO(),
            path_model=EmptyDTO(),
        )