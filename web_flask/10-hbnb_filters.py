#!/usr/bin/python3
"""Create Flask App"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def listen():
    states = list(storage.all("State").values())
    states.sort(key=lambda x: x.name)
    amenities = list(storage.all("Amenity").values())
    amenities.sort(key=lambda x: x.name)
    return render_template(
        '10-hbnb_filters.html',
        states=states,
        amenities=amenities
    )


@app.teardown_appcontext
def stop(e):
    storage.close()


if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=5000, debug=False)
