# This file totally useless unless deployed in heroku as heroku treats
# only this file as the app and it is in always run mode. So that is why
# the `create_tables` function is set here.

from app import app
from db import db

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()
