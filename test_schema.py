from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

# class City(Base):
#     __tablename__ = 'cities'
#     id = Column(String(60), primary_key=True, nullable=False)
#     name = Column(String(128), nullable=False)
#
# class Place(Base):
#     __tablename__ = 'places'
#     id = Column(String(60), primary_key=True, nullable=False)
#     city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
#     city = relationship('City', back_populates='places')
#
# City.places = relationship('Place', order_by=Place.id, back_populates='city')
#

#Setup engine and create tables
engine = create_engine('mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db')
Base.metadata.create_all(engine)

# Drop all tables
Base.metadata.drop_all(engine)

# Recreate all tables with the specified charset and collation
Base.metadata.create_all(engine)
