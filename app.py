from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from routes.flights import flights_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(flights_bp)
    session_maker = sessionmaker(future=True)
    engine = create_engine('postgresql+psycopg2://postgres:1234@localhost/WelbeX_test', echo=True, future=True)
    session_maker.configure(bind=engine)
    app.config['SESSION_MAKER'] = session_maker
    print(session_maker)
    return app
