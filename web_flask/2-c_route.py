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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
