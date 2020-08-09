#!/usr/bin/python3
'''Lists all State objects from the database hbtn_0e_6_usa'''
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, backref, relationship


if __name__ == '__main__':
    connection = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(connection.format(*argv[1:]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session_m = sessionmaker(bind=engine)
    session = session_m()

    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()

    session.close()
