#!/usr/bin/python3
"""Fourth flask app that handles the /python/<text> route"""
from flask import Flask


app = Flask(__name__)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", defaults={"text": "is_cool"})
@app.route("/python/", defaults={"text": "is_cool"})
def python_text(text):
    """return Python <text> for /python/<text> url with defoult value for text"""
    return ("Python {}".format(text.replace("_", " ")))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
