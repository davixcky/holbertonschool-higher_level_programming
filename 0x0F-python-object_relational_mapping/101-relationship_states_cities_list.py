#!/usr/bin/python3
'''Lists all State objects from the database hbtn_0e_6_usa'''
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    connection = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(connection.format(*argv[1:]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session_m = sessionmaker(bind=engine)
    session = session_m()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        # <state id>: <state name>
        # <tabulation><city id>: <city name>
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))
    session.close()
