#!/usr/bin/env python3
"""
Instatiating Babel object
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
"""Instantiate the Babel object"""


class Config(object):
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
"""Use the class as config for Flask app"""


@app.route('/')
def root():
    """
    The Flask app
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
