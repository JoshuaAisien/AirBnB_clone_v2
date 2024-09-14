#!/usr/bin/python3
from flask import Flask, render_template
from models.__init__ import storage


app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """ closes the SQLALCHEMY session after each request """
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a list of all State objects"""
    from models.state import State
    # fetch all State objects from storage and sort by name
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda State: State.name) #sort states based on name
    return render_template('7-states_list.html', states=sorted_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)