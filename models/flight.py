from dataclasses import dataclass

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


@dataclass
class Flight(Base):
    __tablename__ = 'Flights'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    date = sa.Column(sa.Date, nullable=False)
    count = sa.Column(sa.Integer)
    distance = sa.Column(sa.Numeric)
    name = sa.Column(sa.Text)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

