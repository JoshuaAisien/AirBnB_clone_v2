from flask import Flask, render_template
from sqlalchemy.sql.ddl import sort_tables

from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session"""
    storage.close()

@app.route('/states', strict_slashes=False)
def list_states():
    """Dispaly a list of all states objects sorted by name """
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda State: State.name )
    return render_template('9-states.html', states=sorted_states)

@app.route('/states/<id>', strict_slashes=False)
def state_detail(id=None):
    """ display details of a specific State and its cities """
    states = storage.all(State)
    key = f'State.{id}'
    state = states.get(key)
    if state:
        # Retrieve all cities and filter by state_id

        cities = storage.all(City)
        state_cities = [city for city in cities.values() if city.state_id == id ]
        sorted_cities = sorted(state_cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=sorted_cities)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
