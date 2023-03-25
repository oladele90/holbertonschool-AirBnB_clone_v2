#!/usr/bin/python3
"""Third flask module that handles the /c/<text> module"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """return Hello HBNB! for / url"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return HBNB for /hbnb url"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """return C <text> for /c/<text> url and replace "_" with " " """
    return ("C {}".format(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
