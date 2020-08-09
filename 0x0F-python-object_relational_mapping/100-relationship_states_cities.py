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

    #Write a script that creates the State “California” 
    #with the City “San Francisco” from the database hbtn_0e_100_usa: 
    # (100-relationship_states_cities.py)
    
    new_state = State()
    new_state.name = "California"
    session.add(new_state)
    session.commit()

    new_city = City()
    new_city.state_id = new_state.id
    new_city.name = "San Francisco"
    session.add(new_city)

    session.commit()
    session.close()
