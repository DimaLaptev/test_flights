from sqlalchemy import select
from models.flight import Flight


def get_flights(session):
    stmt = select(Flight)
    return session.scalars(stmt).all()


def get_flight(session, id):
    stmt = select(Flight).where(Flight.id == id)
    return session.scalars(stmt).one()
