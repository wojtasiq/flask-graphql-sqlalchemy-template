from services.database import db
from services.jwt import jwt
from app import app


def init_app():
    init_db()
    init_jwt()
    init_routes()


def init_db():
    db.init_app(app)
    from models.user import ModelUser
    from models.user import ModelRole
    from models.user import ModelUsersModelRoles


def init_jwt():
    jwt.init_app(app)


def init_routes():
    from routes.routes import routes_list
    routes_list(app)
