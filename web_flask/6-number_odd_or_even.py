#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Route that returns 'Hello HBNB!'."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route that returns 'HBNB'."""
    return "HBNB!"

@app.route('/C/<text>', strict_slashes=False)
def text(text):
    """Route that displays 'C' followed by the value of text variable."""
    return "C " + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Route that displays 'Python' followed by the value of text variable."""
    return "Python " + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Route that displays 'n is a number' only if n is an integer."""
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """Display an HTML page with H1 tag: 'Number: n' inside the BODY."""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """Display an HTML page with H1 tag: 'Number: n is even|odd' inside the BODY."""
    parity = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', number=n, condition=parity)

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
