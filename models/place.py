#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.amenity import place_amenity

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    # Relationship with User and city
    reviews = relationship("Review", back_populates="place", cascade="all, delete-orphan")
    cities = relationship('City', back_populates='places')
    user = relationship('User', back_populates='places')
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False, back_populates='place_amenities')
    @property
    def review_list(self):
        """  returns the list of Review instances with place_id equals to the current Place.id """
        from models import storage
        from models.review import Review
        return [review_list for review_list in storage.all(Review).values() if review_list.place_id == self.id]


to_set = {'goat', 'school','class'}
print(to_set[0])