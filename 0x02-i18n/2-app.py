#!/usr/bin/env python3
"""This contains the declaration for the flask application."""

from flask import Flask, render_template, request, redirect, url_for
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Set default configurations for the application."""
    # Set the available languages
    LANGUAGES = ['en', 'es', 'fr']

    # Set the default language
    BABEL_DEFAULT_LOCALE = 'en'

    # set the default timezone
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Selector for appropraite URL language in request."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home():
    """ Homepage of website. """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
