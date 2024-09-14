from flask import Flask, render_template
from models.__init__ import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """ remove current SQLAlchemy Session"""
    storage.close()

@app.route("/hbnb", strict_slashes=False)
def hbnb_list():
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place)

    sorted_states = sorted(states, key=lambda state :state.name)
    sorted_cities = sorted(cities, key=lambda city: city.name)
    sorted_amenities = sorted(amenities, key=lambda amenity: amenity.name)
    sorted_places = sorted(places, key=lambda place: place.name)

    return render_template('100-hbnb.html',states=sorted_states, city=sorted_cities, amenities=sorted_amenities, palces=sorted_places)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)