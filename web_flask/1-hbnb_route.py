#!/usr/bin/python3
"""Second flask app that handles the /hbnb route"""
from flask import Flask


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return HBNB for /hbnb url"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
