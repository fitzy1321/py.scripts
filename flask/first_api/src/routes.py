# routes.py - flask api

from flask import render_template
from src import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Fitzy"}
    return render_template("index.html", title="Home", user=user)
    # return render_template("index.html", user=user)
