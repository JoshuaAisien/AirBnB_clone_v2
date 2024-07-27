#!/usr/bin/pyhton3
from flask import Flask

"""Initialization of web_flask project"""

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Route that returns 'Hello HBNB!."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route that returns 'HBNB' """
    return "HBNB!"


@app.route('/C/<text>',strict_slashes=False)
def text(text):
    """route that display C with the cvalue of text variable"""
    return "C " + text.replace('_',' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """route that display's pyhton followed bt the value of the text variable"""
    return "Python "+text.replace("_", " ")


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')