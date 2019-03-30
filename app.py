import os
from flask import Flask, g
from flask import render_template, flash, redirect, url_for

import json
import models

DEBUG = True
PORT = 8000

template_dir = os.path.abspath('./')
app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'adkjfalj.adflja.dfnasdf.asd'

@app.before_request
def before_request():
    """Connect to the DB before each request."""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
