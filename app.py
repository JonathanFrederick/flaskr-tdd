from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE = 'flaskr_tdd'

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False
db = SQLAlchemy(app)


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


if __name__ == "__main__":
    app.run()
