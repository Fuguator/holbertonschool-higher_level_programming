#!/usr/bin/python3
"""
Connecting to a database and listing words which start with uppercase N.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv

Base = declarative_base()

class State(Base):
    """State model for the states table."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))

if __name__ == "__main__":

    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')

    Session = sessionmaker(bind=engine)

    session = Session()
    try:
        results = session.query(State).filter(State.name.like('N%')).order_by(State.id).all()
    except Exception as e:
        print(e)
    else:
        for state in results:
            print(state.id, state.name)

    session.close()
