#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Returns Hello HBNB at root"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
