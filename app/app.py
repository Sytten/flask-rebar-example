from flask import Flask
from flask_migrate import Migrate
from flask_rebar import Rebar
from flask_sqlalchemy import SQLAlchemy


rebar = Rebar()
registry = rebar.create_handler_registry(prefix='/api')
db = SQLAlchemy()
migrate = Migrate(db=db)


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_envvar("APP_CONFIG")

    rebar.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    return app
