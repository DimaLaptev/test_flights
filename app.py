from flask import Flask
from routes.flights import flights_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(flights_bp)
    return app
