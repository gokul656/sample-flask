from flask_jwt_extended import JWTManager # type: ignore

from auth_service.src.models.user_model import User


def jwt_wrapper(flask_app):
    jwt = JWTManager(flask_app)
    jwt.user_identity_loader(user_identity_lookup)
    jwt.user_lookup_loader(user_lookup_callback)


def user_identity_lookup(user):
    return user


def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"] # user data
    return User("gokul65", "gokul656@gmail.com", "test@12345")
