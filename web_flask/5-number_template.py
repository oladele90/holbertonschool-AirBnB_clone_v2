#!/usr/bin/python3
"""Fifth flask app that handles the /number_template/<n> route"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_ret(n):
    """return html doc with Number <n> = n variable"""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
