#!/usr/bin/env python3
"""This contains the declaration for the flask application."""

from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Set default configurations for the application."""
    # Set the available languages
    LANGUAGES = ['en', 'fr']

    # Set the default language
    BABEL_DEFAULT_LOCALE = 'en'

    # set the default timezone
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    """Gets the user details if information passed"""
    try:
        user_key = int(request.args.get('login_as'))
        return users.get(user_key, None)
    except EXCEPTION:
        return None


@app.before_request
def before_request():
    """Sets the global g.user."""
    g.user = get_user()


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
    username = None
    if g.user:
        print(g.user)
        username = g.user.get("name", None)
    return render_template('5-index.html', username=username)


if __name__ == "__main__":
    app.run()
