import psycopg2
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import request, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/production'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Recruits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    chatname = db.Column(db.String(100))
    github_name = db.Column(db.String(100))
    id_number = db.Column(db.BigInteger)
    personal_email_address = db.Column(db.String(100), unique=True)

    def __init__(self, first_name, surname, chatname, github_name, id_number, personal_email_address, cohort):
        self.first_name = first_name
        self.surname = surname
        self.chatname = chatname
        self.github_name = github_name
        self.id_number = id_number
        self.personal_email_address = personal_email_address
        self.cohort = cohort


def main():
    recruit1 = Recruits('Jacky', 'Sledge', 'Jacky92',
                        'JackyS92', 9612075607900, 'JSledge@gmail.com')
    recruit2 = Recruits('Lucky', 'Black', 'LBlack009!',
                        'LuckyBlack009!', 9612075607900, 'LuckyBlue@gmail.com')
    db.session.add(recruit2)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
