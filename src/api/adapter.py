from typing import Any

from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError

from src.api.controllers import BaseController, ErrorDTO
from src.api.http import HttpRequest, EmptyDTO

from typing import Type


class FastAPIAdapter:
    @staticmethod
    async def adapt(
        controller: BaseController,
        request: Request,
        body_model: Type[BaseModel] = EmptyDTO,
        query_model: Type[BaseModel] = EmptyDTO,
        path_model: Type[BaseModel] = EmptyDTO,
    ) -> JSONResponse:
        try:
            raw_body: Any = await request.json()
        except Exception:
            raw_body = {}

        try:
            http_request = HttpRequest(
                url=str(request.url),
                method=request.method,
                headers=dict(request.headers),
                body=FastAPIAdapter.__resolve(body_model, raw_body),
                query_params=FastAPIAdapter.__resolve(
                    query_model, dict(request.query_params)
                ),
                path_params=FastAPIAdapter.__resolve(
                    path_model, dict(request.path_params)
                ),
                user=getattr(request.state, "user", None),
            )
        except ValidationError as error:
            return JSONResponse(
                status_code=422,
                content=ErrorDTO(
                    message="Invalid request",
                    error=error.errors(),
                ).model_dump(mode="json"),
            )

        http_response = await controller.handle(http_request)

        return JSONResponse(
            status_code=http_response.status_code,
            content=FastAPIAdapter.__serialize(http_response.body),
            headers=http_response.headers,
        )

    @staticmethod
    def __resolve(model: Type[BaseModel] | BaseModel, raw: Any) -> Any:
        if isinstance(model, BaseModel):
            return model
        return model.model_validate(raw)

    @staticmethod
    def __serialize(body: Any) -> Any:
        if isinstance(body, BaseModel):
            return body.model_dump(mode="json")

        if isinstance(body, list):
            return [
                FastAPIAdapter.__serialize(item)
                for item in body
            ]

        if isinstance(body, dict):
            return {
                key: FastAPIAdapter.__serialize(value)
                for key, value in body.items()
            }

        return body