from datetime import datetime, UTC
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy import UUID as SQLAlchemyUUID
from sqlalchemy import DateTime, String
from uuid6 import uuid7
from uuid import UUID

Base = declarative_base()

class BaseModel(Base):

    __abstract__ = True
    id:Mapped[UUID] = mapped_column(SQLAlchemyUUID, primary_key=True, default=uuid7)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))

class User(BaseModel):
    __tablename__ = "users"
    name:Mapped[str] = mapped_column(String, nullable=False)
    email:Mapped[str] = mapped_column(String, nullable=False, unique=True)