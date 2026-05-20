from typing import Optional, Self
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker


class SessionManager:

    def __init__(self, engine:AsyncEngine) -> None:
        self.__engine = engine
        self.__session: Optional[AsyncSession] = None
    
    @property
    def session(self) -> AsyncSession:
        if self.__session is None:
            raise RuntimeError(
                "Session not initialized",
            )
        return self.__session
    
    async def __aenter__(self) -> Self:
        sessionmake = sessionmaker(bind=self.__engine, expire_on_commit=False, class_=AsyncSession)
        self.__session = sessionmake()
        if self.__session is None:
            raise RuntimeError("Failed to create session")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        try:
            if exc_type:
                await self.__session.rollback()
            else:
                await self.__session.commit()
        except Exception:
            await self.__session.rollback()
        finally:
            await self.__session.close()
            self.__session = None
