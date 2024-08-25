import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """ this clas manages storage using mysqlalchemy with my MYSQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """ initilizes the engine and session """
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST", "localhost")
        database = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        """ create the engine to enable connections to database"""
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}', pool_pre_ping=True)

        # DROP ALL TABLES IF THE ENVIRONMENT varible "env" is 'test'
        if env == "test":
            Base.metadata.drop_all(self.__engine)

        # create session as an instance attribute
        self.reload()

    def all(self, cls=None):
        """ query on the current database session (self.__session) all objects depending of the class name (argument cls)
            cls=None, query all types of objects (User, State, City, Amenity, Place and Review)
            this method must return a dictionary: (like FileStorage)
            key = <class-name>.<object-id>
            value = object
        """
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.user import User
        from models.review import Review
        from models.amenity import Amenity

        db_dictionary = {}
        if cls:
            query_result = self.__session.query(cls).all()
            for value in query_result:
                key = f'{value.__class__.__name__}.{value.id}'
                db_dictionary[key] = value
        else:
            class_names = [User, State, City, Amenity, Place, Review]
            for class_name in class_names:
                query_result = self.__session.query(class_name).all()
                for value in query_result:
                    key = f"{value.__class__.__name__}.{value.id}"
                    db_dictionary[key] = value

        return db_dictionary

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the databse and create a session """
        from models.state import State
        from models.user import User
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place

        # to create all tables that inherits from Base
        Base.metadata.create_all(self.__engine)
        # create a session factory
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # Use scoped_session to ensure thread safety
        Session = scoped_session(session_factory)
        # set the instance attribute __session
        self.__session = Session()

    def close(self):
        """ closes all sesions """
        self.__session.close()