#!/usr/bin/python3
"""starting FLask"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """show Htmal"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tearitdown(exception):
    """shutdown and close"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
