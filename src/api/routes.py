from typing import Annotated

from fastapi import Body, Query, Request, APIRouter, Depends
from fastapi.responses import JSONResponse
from src.api.middleware import protect

from src.services.login_services import LoginDTO
from src.services.ml_services import MLInputPredictionDTO
from src.api.adapter import EmptyDTO, FastAPIAdapter
from src.api.composers import (
    create_user_composer,
    read_user_composer,
    update_user_composer,
    delete_user_composer,
    ml_prediction_composer,
    login_composer
)
from src.api.config import ENGINE
from src.infra.config.session_manager import SessionManager
from src.services.user_services import (
    CreateUserDTO,
    ReadUserDTO,
    UpdateUserDTO,
    DeleteDTO,
)
from uuid import UUID

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/create_user")
async def create_user(
    request: Request,
    body: Annotated[CreateUserDTO, Body()],
    _: Annotated[dict, Depends(protect)]
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


@router.get("/read_user")
async def read_user(
    request: Request,
    id: Annotated[UUID, Query()],
    _: Annotated[dict, Depends(protect)]
) -> JSONResponse:
    async with SessionManager(ENGINE) as session_manager:
        controller = read_user_composer(session_manager)
        query = ReadUserDTO(id=id)
        return await FastAPIAdapter.adapt(
            controller=controller,
            request=request,
            body_model=EmptyDTO(),
            query_model=query,
            path_model=EmptyDTO(),
        )


@router.patch("/update_user")
async def update_user(
    request: Request,
    body: Annotated[UpdateUserDTO, Body()],
    _: Annotated[dict, Depends(protect)]
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


@router.delete("/delete_user")
async def delete_user(
    request: Request,
    body: Annotated[DeleteDTO, Body()],
    _: Annotated[dict, Depends(protect)]
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

@router.post("/ml_prediction")
async def ml_prediction(
    request: Request,
    body: Annotated[MLInputPredictionDTO, Body()],
    _: Annotated[dict, Depends(protect)]
) -> JSONResponse:
    controller = ml_prediction_composer()
    return await FastAPIAdapter.adapt(
        controller=controller,
        request=request,
        body_model=body,
        query_model=EmptyDTO(),
        path_model=EmptyDTO(),
    )

@router.post("/login")
async def login(
    request: Request,
    body: Annotated[LoginDTO, Body()],
) -> JSONResponse:
    controller = login_composer()
    return await FastAPIAdapter.adapt(
        controller=controller,
        request=request,
        body_model=body,
        query_model=EmptyDTO(),
        path_model=EmptyDTO(),
    )