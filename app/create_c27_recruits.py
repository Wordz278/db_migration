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
    rocketchat_user = db.Column(db.String(100))
    github_name = db.Column(db.String(100))
    id_number = db.Column(db.BigInteger)
    personal_email_address = db.Column(db.String(100), unique=True)
    cohort = db.Column(db.String(100))

    def __init__(self, first_name, surname, rocketchat_user, github_name, id_number, personal_email_address, cohort):
        self.first_name = first_name
        self.surname = surname
        self.rocketchat_user = rocketchat_user
        self.github_name = github_name
        self.id_number = id_number
        self.personal_email_address = personal_email_address
        self.cohort = cohort


def main():
    recruit1 = Recruits('Julia', 'Cage', 'JCage92', 'JCage92',
                        9412075657950, 'JCage@gmail.com', 'C27_Web_Dev')
    recruit2 = Recruits('Timu', 'Grey', 'TimuGrey009!',
                        'TimuGrey009!', 9612075607901, 'TGrey@gmail.com', 'C27_Web_Dev')
    recruit3 = Recruits('Fortunate', 'Blue', 'FBlue1000',
                        'MoneyFloyd', 9212075607902, 'FBlue1000@gmail.com', 'C27_Web_Dev')
    recruit4 = Recruits('Micky', 'Black', 'MK009!',
                        'MickyB009!', 9412075607903, 'MK@gmail.com', 'C27_Web_Dev')
    recruit5 = Recruits('Zoe', 'Yellow', 'ZoeY',
                        'ZoeYel09', 9212075607704, 'ZY@gmail.com', 'C27_Web_Dev')
    db.session.add(recruit5)
    db.session.commit()


if __name__ == "__main__":
    # manager.run()
    main()
