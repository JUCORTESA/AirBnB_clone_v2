#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from models import storage, State, City
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False
a_dict = storage.all('State').values()
b_dict = storage.all('City').values()


@app.route('/states_list')
def states_list():
    """
    Function that returns a list of states
    """
    return render_template('7-states_list.html', my_dict=a_dict)


@app.route('/cities_by_states')
def cities_list():
    return render_template('8-cities_by_states.html',
                           my_dict=a_dict, my_city=b_dict)


@app.teardown_appcontext
def teardown(exception=None):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
