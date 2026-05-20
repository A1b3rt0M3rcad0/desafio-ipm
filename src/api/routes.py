from typing import Annotated

from fastapi import Body, Request, APIRouter
from fastapi.responses import JSONResponse

from src.api.adapter import EmptyDTO, FastAPIAdapter
from src.api.composers import create_user_composer
from src.api.config import ENGINE
from src.infra.config.session_manager import SessionManager
from src.services.user_services import CreateUserDTO

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