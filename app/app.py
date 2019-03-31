from flask import Flask
from flask_rebar import Rebar


rebar = Rebar()
registry = rebar.create_handler_registry(prefix='/api')


def create_app() -> Flask:
    app = Flask(__name__)
    rebar.init_app(app)
    return app


if __name__ == '__main__':
    create_app().run()
