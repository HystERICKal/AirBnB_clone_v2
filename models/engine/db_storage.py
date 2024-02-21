#!/usr/bin/python3
"""dbstorage"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class DBStorage():
    """DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all"""
        if cls:
            temp = self.__session.query(classes[cls])
        else:
            temp = self.__session.query(State).all()
            temp = temp + self.__session.query(City).all()
            temp = temp + self.__session.query(User).all()
            temp = temp + self.__session.query(Place).all()
            temp = temp + self.__session.query(Amenity).all()
            temp = temp + self.__session.query(Review).all()

        temp_dict = {}
        for i in temp:
            x = '{}.{}'.format(type(i).__name__, i.id)
            temp_dict[x] = i
        return temp_dict

    def new(self, i):
        """new"""
        self.__session.add(i)
        self.__session.commit()

    def save(self):
        """save"""
        self.__session.commit()

    def delete(self, i=None):
        """delete"""
        if i is not None:
            self.__session.delete(i)

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        the_sesh = sessionmaker(bind=self.__engine, expire_on_commit=False)
        sesh = scoped_session(the_sesh)
        self.__session = sesh

    def close(self):
        """close"""
        self.__session.remove()
