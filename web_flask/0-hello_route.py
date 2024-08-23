#!/usr/bin/python
from flask import Flask
""" Initiallization file for the Web_glask package"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Route that returns 'Hello HBNB!."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)