from flask import Flask
import service_container


def init_app():
    app = Flask(__name__)
    return app


def init_db(app):
    service_container.db.init_app(app)
