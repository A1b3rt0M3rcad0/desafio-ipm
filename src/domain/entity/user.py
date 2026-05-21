"""Entidade de domínio User."""

from typing import Optional
from uuid6 import uuid7
from datetime import datetime, UTC
from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID

class User(BaseModel):
    model_config = ConfigDict(validate_assignment=True, from_attributes=True)
    id:Optional[UUID] = Field(default=None, description="This field is the ID from user")
    name:Optional[str] = Field(description="This field is a Name from user")
    email:Optional[str] = Field(description="This field is the Email from user")
    created_at:Optional[datetime] = Field(default=None, description="Creation data")