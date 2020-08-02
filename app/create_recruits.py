import psycopg2
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_script import Manager
from flask import request, jsonify
from app import Recruits

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Recruits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    github_name = db.Column(db.String(100))
    id_number = db.Column(db.BigInteger)

    def __init__(self, first_name, surname, github_name, id_number):
        self.first_name = first_name
        self.surname = surname
        self.github_name = github_name
        self.id_number = id_number


def main():
    recruit = Recruits('Floyd', 'Shikwambana', 'Javas278', 9612075607998)
    db.session.add(recruit)
    db.session.commit()


if __name__ == "__main__":
    main()
