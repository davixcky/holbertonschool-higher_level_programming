#!/usr/bin/python3
'''Class definition of a State and an instance Base = declarative_base()'''
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State
from sqlalchemy.orm import relationship


class City (Base):
    '''City class for table cities'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False, )
