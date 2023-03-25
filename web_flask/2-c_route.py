#!/usr/bin/python3
"""C is Fun Module"""
from flask import Flask


app = Flask(__name__)


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """return C <text> for /c/<text> url
    and replace "_" with " " """
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
