from flask import Flask
from sqlalchemy import create_engine, Integer, String
from routes.flights import flights_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(flights_bp)
    return app


engine = create_engine('postgresql+psycopg2://postgres:1234@localhost/WelbeX_test', echo=True, future=True)
engine.connect()
print(engine)
