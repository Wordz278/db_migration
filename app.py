import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/dev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    recruit = db.relationship('Recruit', backref='owner', lazy='dynamic')


class Recruits(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(20))
    surname = db.Column(db.String(20))
    chatname = db.Column(db.VARCHAR(15))
    github_name = db.Column(db.VARCHAR(20))
    id_number = db.Column(db.NUMERIC(15))
    personal_email = db.Column(db.VARCHAR(20), unique=True)
    cohort = db.Column(db.VARCHAR(100))


if __name__ == '__main__':
    manager.run()
