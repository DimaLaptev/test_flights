from flask import Flask, Blueprint, jsonify

app = Flask(__name__)
flights_bp = Blueprint('flights', __name__, url_prefix='/api/flights')


@flights_bp.route('/', methods=['GET'])
def get_flights():
    flights = [
        {
            'id': 1,
            'date': u'22.06.1941',
            'name': u'Moskow',
            'count': u'100',
            'distance': u'1300'
        }
    ]
    return jsonify({'flights': flights})
