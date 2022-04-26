import flask
from flask import Flask, Blueprint, jsonify, g, current_app
from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker
from models import Flight, Base

flights_bp = Blueprint('flights', __name__, url_prefix='/api/flights')


@flights_bp.route('/', methods=['GET'])
def get_flights():
    with flask.current_app.app_context():
        sm = flask.current_app.config.get('SESSION_MAKER')
        session = sm()
        print(g.get('engine', None))
        stmt = select(Flight)
        flights = session.scalars(stmt)
        for flight in flights:
            print(flight)
    return jsonify({'data' : []})

# with Session(g) as session:

#    Moskow = Flight(
#        date='2022-09-21',
#        count='211',
#        distance='2100.5',
#        name='Moskow'
#    )

#    session.add(Moskow)

#    session.commit()

#
