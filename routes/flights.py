import flask
from flask import Blueprint, jsonify
from sqlalchemy import select

from models import Flight

flights_bp = Blueprint('flights', __name__, url_prefix='/api/flights')


@flights_bp.route('/', methods=['GET'])
def get_flights():
    sm = flask.current_app.config.get('SESSION_MAKER')
    session = sm()
    stmt = select(Flight)
    flights = session.scalars(stmt).all()
#    for u in session.query(flights).all():
#        print(u.__dict__)
#    print(flights)
    return jsonify(flights)
