import os

def get_jwt_secret_key():
    return os.getenv("JWT_SECRET_KEY")

JWT_SECRET_KEY = get_jwt_secret_key()