#!/usr/bin/python3
"""flask app that handles the /states_list url"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_ret():
    """retrieves all states and renders them into html doc"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tearit(torn):
    """module closes current session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
