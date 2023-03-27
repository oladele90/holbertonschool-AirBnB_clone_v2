#!/usr/bin/python3
"""Fifth flask app that handles the /number__odd_or_even/<n> route"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def numb_O_E(n):
    """return html doc with Number <n> is even or odd"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
