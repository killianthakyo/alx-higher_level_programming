#!/usr/bin/python3

"""
Print state object using given arg
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    flag_check = 0
    """for state in session.query(State):
        if state.name == argv[4]:
            print("{}".format(state.id))
            flag_check = 1
            break
    if (flag_check != 1):
        print("Not found")"""
    state = session.query(State).filter(State.name == argv[4]).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
