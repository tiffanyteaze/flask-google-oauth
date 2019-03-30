import datetime
from peewee import *

from flask import Flask, g
from flask import render_template, flash, redirect, url_for, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import check_password_hash

from flask_login import UserMixin
from flask_bcrypt import generate_password_hash

DATABASE = SqliteDatabase('dermatic.db')

class User(UserMixin, Model):
    username = CharField()
    email = CharField()
    first_name = CharField()
    last_name = CharField()
    skin_type = CharField()
    avatar = CharField()
    
    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()