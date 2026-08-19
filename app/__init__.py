from flask import Flask

from app.config import Config
from app.database import init_database
from app.routes import bp


def create_app(config_object: type[Config] | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object or Config)
    init_database(app.config["DATABASE_URL"])
    app.register_blueprint(bp)
    return app
