#!/usr/bin/env python3
"""
Instatiating Babel object
"""

from flask import Flask, render_template
from flask_babel import Babel

babel = Babel(app)
app = Flask(__name__)


class Config(object):
    """
    Configuring available languages
    """
    LANGUAGES = ['en', 'fr']
    # Inherent defaults
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Sets the class config as the configuration for the app
app.config.from_object('1-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    GET / route and return 1-index.html
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
