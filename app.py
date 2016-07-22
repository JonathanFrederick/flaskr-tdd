from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import os
import re
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE = 'flaskr_tdd'


def create_app(configuration):
    app = Flask(__name__)
    app.config.from_object(configuration)
    app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False
    return app


def init_db(db_name=DATABASE):
    """Function to create a database"""
    engine = create_engine('postgresql+psycopg2://127.0.0.1:5432/postgres')
    session = sessionmaker(bind=engine)()
    session.connection().connection.set_isolation_level(0)
    session.execute('CREATE DATABASE {};'.format(db_name))
    session.connection().connection.set_isolation_level(1)


def drop_db(db_name=DATABASE):
    """Function to drop a database"""
    engine = create_engine('postgresql+psycopg2://127.0.0.1:5432/postgres')
    session = sessionmaker(bind=engine)()
    session.connection().connection.set_isolation_level(0)
    session.execute('DROP DATABASE {};'.format(db_name))
    session.connection().connection.set_isolation_level(1)


def name_from_uri(uri):
    """A helper function to retrieve the database name from
    the end of the uri"""
    return re.search(r'/\w+$', uri).group(0)[1:]


def connect_db():
    conn = psycopg2.connect(database=name_from_uri(os.environ['DATABASE_URL']))
    cursor = conn.cursor()
    return cursor


app = create_app(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
from models import Posting


@app.route('/')
def show_entries():
    """Searches the database for entries, then displays them."""
    entries = db.session.query(Posting).all()
    return render_template('index.html', entries=entries)


if __name__ == "__main__":
    app.run()
