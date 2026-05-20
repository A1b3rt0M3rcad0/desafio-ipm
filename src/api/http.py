from typing import Any, TypeVar, Generic
from pydantic import BaseModel, Field

BodyT = TypeVar("BodyT", bound=BaseModel)
QueryT = TypeVar("QueryT", bound=BaseModel)
PathT = TypeVar("PathT", bound=BaseModel)
ResponseT = TypeVar("ResponseT")

class EmptyDTO(BaseModel):
    pass

class HttpRequest(BaseModel, Generic[BodyT, QueryT, PathT]):
    user: str | None = None
    url: str | None = None
    method: str | None = None
    headers: dict[str, Any] = Field(default_factory=dict)
    body: BodyT
    query_params: QueryT
    path_params: PathT


class HttpResponse(BaseModel, Generic[ResponseT]):
    status_code: int
    headers: dict[str, Any] = Field(default_factory=dict)
    body: ResponseT