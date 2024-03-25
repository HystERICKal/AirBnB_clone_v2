#!/usr/bin/python3
"""starting flask"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def showing_html():
    """show html"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def tearitdown(exc):
    """closing"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
