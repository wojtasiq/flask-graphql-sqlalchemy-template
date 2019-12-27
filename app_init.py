from services.database import db
from app import app


def init_app():
    init_db()
    init_routes()


def init_db():
    db.init_app(app)
    from models.user import ModelUser
    from models.user import ModelRole
    from models.user import ModelUsersModelRoles

def init_routes():
    from routes.routes import routes_list
    routes_list(app)
