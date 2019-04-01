import os
from flask import Flask, redirect, url_for, flash, redirect, session, g, render_template, Response
from flask_dance.contrib.google import make_google_blueprint, google

import json
import models
import functools
import flask

# from authlib.client import OAuth2Session
# import google.oauth2.credentials
# import googleapiclient.discovery


GOOGLE_CLIENT_ID = '214512520695-9om7eammcfcefjedqao6lk0erf14fpq7.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'C48_DSE_KeHnHMXhpRrPsCko'
REDIRECT_URI = '/authorized'

ACCESS_TOKEN_URI = 'https://www.googleapis.com/oauth2/v4/token'
AUTHORIZATION_URL = 'https://accounts.google.com/o/oauth2/v2/auth?access_type=offline&prompt=consent'
AUTHORIZATION_SCOPE ='openid email profile'

AUTH_REDIRECT_URI = os.environ.get("http://localhost:8000/authorized", default=False)
BASE_URI = os.environ.get("http://localhost:8000", default=False)
CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", default=False)
CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", default=False)

AUTH_TOKEN_KEY = 'auth_token'
AUTH_STATE_KEY = 'auth_state'
USER_INFO_KEY = 'user_info'

SECRET_KEY = 'oauthsecretkey'
DEBUG = True
PORT = 8000

template_dir = os.path.abspath('./')
app = Flask(__name__, template_folder=template_dir)
# app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")
# app.config["GOOGLE_OAUTH_CLIENT_ID"] = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
# app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
# google_bp = make_google_blueprint(scope=["profile", "email"])
# blueprint = make_google_blueprint()
# app.register_blueprint(google_bp, url_prefix="/login")
app.secret_key = "supersekrit"
blueprint = make_google_blueprint(
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")

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

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v1/userinfo")
    assert resp.ok, resp.text
    return "You are {email} on Google".format(email=resp.json()["email"])

@app.route("/logout")
def logout():
    token = blueprint.token["access_token"]
    resp = google.post(
        "https://accounts.google.com/o/oauth2/revoke",
        params={"token": token},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    del app.blueprints['google'].token
    # if resp.ok:
        # del app.blueprints['google'].token
        # resp.set_cookie('session', 'bar', max_age=0)
        # resp.delete_cookie('session')
        # logout_user() 
    return redirect(url_for('index'))

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
