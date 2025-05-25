#!/usr/bin/env python3
from datetime import datetime

from sqlalchemy import (create_engine,Column, Integer, String, desc,CheckConstraint,
    PrimaryKeyConstraint, UniqueConstraint, Index, DateTime)
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)

      
    Session = sessionmaker(bind=engine)  # use our engine to configure a 'Session' class
    Session = Session  # use 'Session' class to create 'session' object
 
 