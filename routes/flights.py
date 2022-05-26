import flask
from flask import Blueprint, jsonify
from services.flights import get_flights, get_flight

flights_bp = Blueprint('flights', __name__, url_prefix='/api/flights')


@flights_bp.route('/', methods=['GET'])
def get_flights_api():
    sm = flask.current_app.config.get('SESSION_MAKER')
    session = sm()
    flights = get_flights(session)
    list_flights = [flight.as_dict() for flight in flights]
    return jsonify({"list": list_flights})

@flights_bp.route('/<id>', methods=['GET'])
def get_flight_api(id):
    sm = flask.current_app.config.get('SESSION_MAKER')
    session = sm()
    flight = get_flight(session, id)
    return jsonify(flight.as_dict())

