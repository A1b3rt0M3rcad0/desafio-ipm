from src.auth.jwt_secret_key import JWT_SECRET_KEY
from pydantic import BaseModel, Field
import jwt

class JwtData(BaseModel):
    email: str
    expires_in: int | None = None

    def to_dict(self) -> dict:
        return {"email": self.email}

class JWTAccessToken(BaseModel):
    secret_key: str | None = Field(default=JWT_SECRET_KEY)
    algorithm: str = "HS256"

    def tokenize(self, data: JwtData) -> str:
        return jwt.encode(data.to_dict(), self.secret_key, algorithm=self.algorithm)

    def decode_token(self, token: str) -> JwtData:
        try:
            data = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return JwtData(**data)
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token")