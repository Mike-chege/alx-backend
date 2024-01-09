#!/usr/bin/env python3
"""
Parametizing the templates
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)
"""Instantiate the Babel object"""


class Config(object):
    """
    The Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
"""Use the class as config for the Flask app"""


@app.route('/')
def root():
    """
    The Flask app
    """
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    """
    Determine the best match
    With our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
