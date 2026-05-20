from sqlalchemy.exc import IntegrityError

class AlreadyExists(Exception):
    pass

mapper = {
    IntegrityError.__name__: AlreadyExists
}