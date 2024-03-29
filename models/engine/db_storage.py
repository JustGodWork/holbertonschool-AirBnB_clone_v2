from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


user = os.getenv("HBNB_MYSQL_USER")
password = os.getenv("HBNB_MYSQL_PWD")
host = os.getenv("HBNB_MYSQL_HOST")
database = os.getenv("HBNB_MYSQL_DB")
env = os.getenv("HBNB_ENV")


class DBStorage:
    """This class manages storage of hbnb models in a database"""
    __engine = None
    __session = None

    def __init__(self):
        """
        Instantiates a new DBStorage singleton instance
        """
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{database}',
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage
        """
        objects = {}
        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                key = "{}.{}".format(cls.__name__, obj.id)
                objects[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for i in range(len(classes)):
                if (issubclass(classes[i], Base)):
                    query = self.__session.query(classes[i]).all()
                    for obj in query:
                        key = "{}.{}".format(
                            classes[i].__name__,
                            obj.id
                        )
                        objects[key] = obj
        return objects

    def new(self, obj):
        """
        Adds new object to storage dictionary
        """
        self.__session.add(obj)

    def save(self):
        """
        Saves storage dictionary to file
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from __objects if it’s inside
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Loads storage dictionary from file
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        """
        Calls remove() method on the private session attribute
        """
        self.__session.remove()
