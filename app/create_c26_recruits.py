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
    cohort = db.Column(db.String(100))

    def __init__(self, first_name, surname, chatname, github_name, id_number, personal_email_address, cohort):
        self.first_name = first_name
        self.surname = surname
        self.chatname = chatname
        self.github_name = github_name
        self.id_number = id_number
        self.personal_email_address = personal_email_address
        self.cohort = cohort


def main():
    recruit1 = Recruits('Oslo', 'King', 'OSKing92', 'OS92',
                        9612075607950, 'OD92@gmail.com', 'C26_JAVA')
    recruit2 = Recruits('Jane', 'Doe', 'JDoe009!',
                        'JaneDoe009!', 9612075607900, 'JDoe@gmail.com', 'C26_JAVA')
    recruit3 = Recruits('Floyd', 'Money', 'FMoney1000',
                        'MoneyFloyd', 9212075607900, 'FM1000@gmail.com', 'C26_JAVA')
    recruit4 = Recruits('Woody', 'Green', 'WG009!',
                        'WoodyG009!', 9612075607900, 'WG@gmail.com', 'C26_JAVA')
    recruit5 = Recruits('Tumelo', 'Khoza', 'TK_Oct',
                        'TK009!', 9112075607700, 'TK@gmail.com', 'C26_JAVA')
    db.session.add(recruit5)
    db.session.commit()


if __name__ == "__main__":
    # manager.run()
    main()
