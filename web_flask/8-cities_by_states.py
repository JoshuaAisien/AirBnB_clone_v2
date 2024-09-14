#!/usr/bin/python3
from flask import Flask, render_template
from models.__init__ import storage
"""  a script that starts a Flask web application """

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current sqlsession"""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def list_of_cities():
    from models.state import State
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda State: State.name)
    return render_template("8-cities_by_states.html", states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)