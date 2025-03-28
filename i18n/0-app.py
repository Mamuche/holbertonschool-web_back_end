#!/usr/bin/env python3
""" use Flask with Babel """


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    return render_template('0-index.html')
