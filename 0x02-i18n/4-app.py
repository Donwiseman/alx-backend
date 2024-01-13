#!/usr/bin/env python3
"""This contains the declaration for the flask application."""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Set default configurations for the application."""
    # Set the available languages
    LANGUAGES = ['en', 'fr']

    # Set the default language
    BABEL_DEFAULT_LOCALE = 'en'

    # set the default timezone
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale(lang=None):
    """Selector for appropraite URL language in request."""
    lang = request.args.get('locale')
    if lang:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home():
    """ Homepage of website. """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
