import flask
from flask import Blueprint, jsonify
from sqlalchemy import select
from models.flight import Flight

flights_bp = Blueprint('flights', __name__, url_prefix='/api/flights')


@flights_bp.route('/', methods=['GET'])
def get_flights():
    sm = flask.current_app.config.get('SESSION_MAKER')
    session = sm()
    stmt = select(Flight)
    flights = session.scalars(stmt).all()
    list_flights = [flight.as_dict() for flight in flights]
    return jsonify({"list": list_flights})
