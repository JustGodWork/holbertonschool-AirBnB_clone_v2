#!/usr/bin/python3
"""Create Flask App"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def listen(id=None):
    states = storage.all("State").values()
    states = sorted(states, key=lambda x: x.name)
    if id:
        state = next((state for state in states if state.id == id), None)
        if state:
            cities = sorted(state.cities, key=lambda x: x.name)
            return render_template(
                '9-states.html',
                states=states,
                state=state,
                cities=cities
            )
        else:
            return render_template('9-states.html', states=False, state=None)
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def stop(e):
    storage.close()


if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=5000, debug=False)
