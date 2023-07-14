#!/usr/bin/python3

"""
Script that lists all State objects from a database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State) \
            .filter(City.state_id == State.id) \
            .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
