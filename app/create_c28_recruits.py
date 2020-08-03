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
    first_name = db.Column(db.String(100), primary_key=True)
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
    recruit1 = Recruits('Jake', 'Rod', 'JRod92', 'JRod92',
                        9412075657951, 'JRod@gmail.com', 'C28_Data_Scientists')
    recruit2 = Recruits('Charly', 'Pop', 'CPop009!',
                        'CPop009!', 9512075607909, 'CPop@gmail.com', 'C28_Data_Scientists')
    recruit3 = Recruits('Allan', 'Brown', 'ABrown1000',
                        'ABrown', 9212075607903, 'ABrown1000@gmail.com', 'C28_Data_Scientists')
    recruit4 = Recruits('Sam', 'Husk', 'SamH009!',
                        'SamH009!', 9312073687909, 'SamH@gmail.com', 'C28_Data_Scientists')
    recruit5 = Recruits('Joe', 'Campbell', 'JoeC',
                        'JoeCl09', 9512075607705, 'JoeC@gmail.com', 'C28_Data_Scientists')
    db.session.add(recruit5)
    db.session.commit()


if __name__ == "__main__":
    # manager.run()
    main()
