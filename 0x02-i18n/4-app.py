#!/usr/bin/env python3
"""
Forcing a particular locale by passing the locale=fr
Parameter to the app’s URLs.
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
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """
    Determines the best match
    With our supported languages
    """
    localLang = request.args.get('locale')
    supportLang = app.config['LANGUAGES']
    if localLang in supportLang:
        return localLang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
