#!/usr/bin/python3
"""Fourth flask app that handles the /number/<n> route"""
from flask import Flask


app = Flask(__name__)


@app.route("/number/<int:n>", strict_slashes=False)
def number_ret(n):
    """return Number <n> for /number/<n> url"""
    return ("{} is a number".format(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
