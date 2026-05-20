from src.infra.config.session_manager import SessionManager
from src.infra.repository.repositories import UserRepository
from src.api.controllers import BaseController, MLPredictionController

from src.api.controllers import CreateUserController
from src.api.controllers import ReadUserController
from src.api.controllers import UpdateUserController
from src.api.controllers import DeleteUserController
from src.api.controllers import LoginController
from src.services.user_services import CreateUser
from src.services.user_services import ReadUser
from src.services.user_services import UpdateUser
from src.services.user_services import DeleteUser
from src.services.ml_services import MLPredictionService
from src.services.login_services import LoginService

def create_user_composer(session_manager: SessionManager) -> BaseController:
    user_repository = UserRepository(session_manager)
    create_user_service = CreateUser(user_repository)
    controller = CreateUserController(create_user_service)
    return controller

def read_user_composer(session_manager: SessionManager) -> BaseController:
    user_repository = UserRepository(session_manager)
    read_user_service = ReadUser(user_repository)
    controller = ReadUserController(read_user_service)
    return controller

def update_user_composer(session_manager: SessionManager) -> BaseController:
    user_repository = UserRepository(session_manager)
    update_user_service = UpdateUser(user_repository)
    controller = UpdateUserController(update_user_service)
    return controller

def delete_user_composer(session_manager: SessionManager) -> BaseController:
    user_repository = UserRepository(session_manager)
    delete_user_service = DeleteUser(user_repository)
    controller = DeleteUserController(delete_user_service)
    return controller

def ml_prediction_composer() -> BaseController:
    ml_prediction_service = MLPredictionService()
    controller = MLPredictionController(ml_prediction_service)
    return controller

def login_composer() -> BaseController:
    login_service = LoginService()
    controller = LoginController(login_service)
    return controller