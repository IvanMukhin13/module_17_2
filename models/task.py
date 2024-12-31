from all_python.module_17.mod_17.app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from all_python.module_17.mod_17.app.models import *


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer,  primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=True)
    slug = Column(String, unique=True, index=True)

    user = relationship('User', back_populates='tasks')


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship('Task', back_populates='user')



print(CreateTable(Task.__table__))