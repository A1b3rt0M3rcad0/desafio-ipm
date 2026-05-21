from src.auth.jwt_secret_key import JWT_SECRET_KEY
from pydantic import BaseModel, Field
import jwt
import os
from datetime import datetime, timedelta, timezone

JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

class JwtData(BaseModel):
    email: str
    exp: int | None = None

    def to_dict(self) -> dict:
        return {"email": self.email, "exp": self.exp}

class JWTAccessToken(BaseModel):
    secret_key: str | None = Field(default=JWT_SECRET_KEY)
    algorithm: str = "HS256"

    def tokenize(self, data: JwtData) -> str:
        if data.exp is None:
            exp = int((datetime.now(timezone.utc) + timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)).timestamp())
        else:
            exp = data.exp
        payload = {**data.to_dict(), "exp": exp}
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def decode_token(self, token: str) -> JwtData:
        try:
            data = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return JwtData(**data)
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token")