#!/usr/bin/python3
"""This is the DBStorage class for AirBnB"""
import json
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import environ, getenv


import models
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


all_classes = {"State": State, "City": City, "Place": Place,
               "User": User, "Review": Review, "Amenity": Amenity}


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __engine: None
        __Session: None
    """
    __engine = None
    __session = None

    def __init__(self):
        """initialize DBStorage class"""

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB'),
                pool_pre_ping=True))

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """show all instance of a class"""
        store_dict = {}
        for c in classes:
            if cls is None or cls is classes[c] or cls is c:
                objs = self.__session.query(classes[c]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    store_dict[key] = obj
        return (store_dict)

    def new(self, obj):
        """add object"""
        self.__session.add(obj)

    def save(self):
        """save the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete the obj"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload database"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()
