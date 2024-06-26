import logging

from flask import Flask
from werkzeug.exceptions import Unauthorized

from auth_service.src.middlewares.auth_middleware import jwt_wrapper
from auth_service.src.middlewares.exception_handlers import exception_handler, unauthorized_handler
from auth_service.src.routes.health_route import health_blueprint
from auth_service.src.routes.user_route import user_blueprint
from auth_service.src.routes.auth_route import auth_blueprint

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret'

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


def create_app():
    _register_error_handlers(app)
    _register_blueprint(app)
    _register_middlewares(app)

    return app


def _register_blueprint(flask_app):
    flask_app.register_blueprint(blueprint=health_blueprint)
    flask_app.register_blueprint(blueprint=user_blueprint, url_prefix="/user")
    flask_app.register_blueprint(blueprint=auth_blueprint, url_prefix="/auth")


def _register_middlewares(flask_app):
    jwt_wrapper(flask_app)


def _register_error_handlers(flask_app):
    flask_app.register_error_handler(Unauthorized, unauthorized_handler)
    flask_app.register_error_handler(Exception, exception_handler)
