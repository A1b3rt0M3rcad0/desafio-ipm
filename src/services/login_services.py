"""Serviço de login com validação de credenciais e geração de token JWT."""

from src.auth.jwt_access_token import JWTAccessToken, JwtData
from src.auth.password import hash_password, verify_password
from pydantic import BaseModel
import os

class LoginDTO(BaseModel):
    email:str
    password:str

class LoginService:
    def __init__(self):
        self.jwt_access_token = JWTAccessToken()

    def execute(self, login_dto: LoginDTO) -> str:
        """Valida as credenciais contra variáveis de ambiente e retorna um token JWT."""
        admin_email = os.getenv("ADMIN_EMAIL")
        admin_password = os.getenv("ADMIN_PASSWORD")

        if login_dto.email == admin_email and login_dto.password == admin_password:
            jwt_data = JwtData(email=login_dto.email)
            return self.jwt_access_token.tokenize(jwt_data)

        raise ValueError("Your credentials are invalid")