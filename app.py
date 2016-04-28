from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False
db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run()
#
