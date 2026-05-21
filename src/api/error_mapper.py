"""Mapeamento de exceções de infraestrutura para erros de domínio."""

from sqlalchemy.exc import IntegrityError

class AlreadyExists(Exception):
    pass

mapper = {
    IntegrityError.__name__: AlreadyExists
}