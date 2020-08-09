#!/usr/bin/python3
'''Lists all State objects from the database hbtn_0e_6_usa'''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    arguments, state = argv[1:4], "Louisiana"
    connection = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(connection.format(*arguments),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session_m = sessionmaker(bind=engine)
    session = session_m()

    new_state = State()
    new_state.name = state
    session.add(new_state)
    session.commit()

    print(new_state.id)
    session.close()
