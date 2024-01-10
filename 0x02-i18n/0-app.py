#!/usr/bin/env python3
"""This contains the declaration for the flask application."""

from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Homepage of website. """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
