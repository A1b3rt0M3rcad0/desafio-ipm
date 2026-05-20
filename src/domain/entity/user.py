from uuid6 import uuid7
from datetime import datetime, UTC
from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID

class User(BaseModel):
    model_config = ConfigDict(validate_assignment=True, from_attributes=True)
    id:UUID = Field(description="This field is the ID from user", default_factory=uuid7)
    name:str = Field(description="This field is a Name from user")
    email:str = Field(description="This field is the Email from user")
    created_at:datetime = Field(default_factory=lambda: datetime.now(UTC), description="Creation data")