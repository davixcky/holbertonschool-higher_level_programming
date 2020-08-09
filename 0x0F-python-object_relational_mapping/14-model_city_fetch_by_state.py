#!/usr/bin/python3
'''Lists all State objects from the database hbtn_0e_6_usa'''
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    connection = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(connection.format(*argv[1:]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session_m = sessionmaker(bind=engine)
    session = session_m()

    result = session.query(City, State).filter(State.id == City.state_id)\
                    .order_by(City.id).all()
    for city, state in result:
        # California: (1) San Francisco
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
