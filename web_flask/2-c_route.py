#!/usr/bin/python3
''' starting Flask...well Hello Flask! '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def start_Flask():
    """ show 'Hello HBNB' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ show 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """ show custom text """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
