"""Hash e verificação de senhas com bcrypt via passlib."""

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Retorna o hash bcrypt da senha fornecida."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha em texto plano corresponde ao hash bcrypt."""
    return pwd_context.verify(plain_password, hashed_password)


if __name__ == "__main__":
    password = "my_secure_password"
    hashed = hash_password(password)
    print(f"Hashed password: {hashed}")
    assert verify_password(password, hashed) == True
    assert verify_password("wrong_password", hashed) == False