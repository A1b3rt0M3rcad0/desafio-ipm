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
    body: BodyT | None = None
    query_params: QueryT | None = None
    path_params: PathT | None = None


class HttpResponse(BaseModel, Generic[ResponseT]):
    status_code: int
    headers: dict[str, Any] = Field(default_factory=dict)
    body: ResponseT