from flask import Flask, render_template

from models import storage

""" a script that starts a Flask web application displaying a webpage"""

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """ remove current sqlAlchemy session"""
    storage.close()

@app.route("/hbnb_filters",  strict_slashes=False)
def hbnb_filters():
    from models.state import State
    from models.amenity import Amenity

    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    sorted_amenities = sorted(amenities, key= lambda amenity: amenity.name)

    return render_template('10-hbnb_filters.html', states=sorted_states, amenities=sorted_amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000)