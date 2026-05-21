"""Tipos genéricos HttpRequest e HttpResponse para desacoplamento do framework."""

from typing import Any, TypeVar, Generic, Optional
from pydantic import BaseModel, Field

class EmptyDTO(BaseModel):
    pass

BodyT = TypeVar("BodyT", bound=BaseModel, default=EmptyDTO)
QueryT = TypeVar("QueryT", bound=BaseModel, default=EmptyDTO)
PathT = TypeVar("PathT", bound=BaseModel, default=EmptyDTO)
ResponseT = TypeVar("ResponseT")

class HttpRequest(BaseModel, Generic[BodyT, QueryT, PathT]):
    user: str | None = None
    url: str | None = None
    method: str | None = None
    headers: dict[str, Any] = Field(default_factory=dict)
    body: Any = None
    query_params: Any = None
    path_params: Any = None


class HttpResponse(BaseModel, Generic[ResponseT]):
    status_code: int
    headers: dict[str, Any] = Field(default_factory=dict)
    body: ResponseT