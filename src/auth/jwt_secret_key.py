"""Leitura da chave secreta JWT a partir de variável de ambiente."""

import os

def get_jwt_secret_key():
    """Retorna a chave secreta JWT definida na variável de ambiente."""
    return os.getenv("JWT_SECRET_KEY")

JWT_SECRET_KEY = get_jwt_secret_key()