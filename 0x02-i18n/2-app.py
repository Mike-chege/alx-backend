#!/usr/bin/env python3
"""
Creating get_locale function
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
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """
    Determines the best match
    With our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
