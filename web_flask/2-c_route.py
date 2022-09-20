#!/usr/bin/python3
"""
Write a script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ Returns hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ Returns hello HBNB """
    return 'HBNB'


@app.route('/c/<path:text>', strict_slashes=False)
def c_text(text):
    """ Returns hello HBNB """
    return 'C {}'.format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
