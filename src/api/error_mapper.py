from sqlalchemy.exc import IntegrityError

class AlreadyExists(Exception):
    pass

mapper = {
    IntegrityError.__class__.__name__: AlreadyExists
}