#!/usr/bin/python3
"""
A python script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage, State, City

app = Flask(__name__)
a_dict = storage.all('State').values()
b_dict = storage.all('City').values()


@app.route('/', strict_slashes=False)
def index():
    """index page"""
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb route"""
    return("HBNB")


@app.route('/c/<text>/', strict_slashes=False)
def c(text):
    """c route"""
    return("C {}".format(text))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>/', strict_slashes=False)
def python(text="is cool"):
    """python route"""
    if text != "is cool":
        new_text = text.replace("_", " ")
        return("Python {}".format(new_text))
    return("Python {}".format(text))


@app.route('/number/<int:n>/', strict_slashes=False)
def number(n):
    """number route"""
    return("{} is a number".format(n))


@app.route('/number_template/<int:n>/', strict_slashes=False)
def number_template(n=None):
    """number_template route"""
    return(render_template("5-number.html", n=n))


@app.route('/number_odd_or_even/<int:n>/', strict_slashes=False)
def odd_or_even(n=None):
    """number_odd_or_even route"""
    return(render_template("6-number_odd_or_even.html", n=n))


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Function that returns a list of states
    """
    return render_template('7-states_list.html', my_dict=a_dict)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """
    Function that returns a list of cities by states
    """
    return render_template('8-cities_by_states.html',
                           my_dict=a_dict, my_city=b_dict)


@app.teardown_appcontext
def teardown(exception=None):
    """
    Function closes the current session
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
