#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Returns Hello HBNB at root"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns Hello HBNB at /hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Returns /c/<text>"""
    letext = text.replace('_', ' ')
    return 'C %s' % letext


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text):
    """Returns /python, with a default text 'is cool'"""
    letext = text.replace('_', ' ')
    return 'Python %s' % letext


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Returns a string if n is int"""
    if type(n) == int:
        return '%i is a number' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0')
