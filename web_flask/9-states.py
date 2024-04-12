#!/usr/bin/python3
"""Create Flask App"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states", defaults={'id': None}, strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def listen(id):
    from models import storage
    states = storage.all("State").values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state, id=id)
    if id is None:
        return render_template('9-states.html', states=states, id=id)
    return render_template('9-states.html')


@app.teardown_appcontext
def stop(e):
    from models import storage
    storage.close()


if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=5000, debug=False)
