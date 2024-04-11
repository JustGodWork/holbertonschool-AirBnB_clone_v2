#!/usr/bin/python3
"""Create Flask App"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def listen():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def listen_hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def listen_c(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
