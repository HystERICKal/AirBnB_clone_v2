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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_Python(text='is cool'):
    """show Python with text"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_checker(n):
    """ is it number? """
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
