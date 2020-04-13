import psycopg2

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

connection = psycopg2.connect(
    database='prod', user='user', password='pass', host='localhost', port='5432')
cursor = connection.cursor()

query = """INSERT INTO recruits(first_name, surname, chatname, github_name, id_number, personal_email, cohort) 
VALUES 
('Queen','Walker','QWalker','QWalkerGitHub','566608','QWalker@gmail.com','C28 Data Eng'),
('Thato','Hawks','THawks','THawksGitHub','143548','THawks@outlook.com','C28 Data Eng'),
('Valencia','Red','Vally','VRedGitHub','666265','VRed@yahoo.com','C28 Data Eng'),
('Fortunate','Shiks','FShiks','FortuGitHub','84492','fortu@hotmail.com','C28 Data Eng'),
('Fox','Shiks',Fox57,'FoxSGitHub','545646','fox@hotmail.com','C28 Data Eng');"""


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:user@localhost/prod'
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
    id_number = db.Column(db.NUMERIC(15), db.ForeignKey('user.id'))
    personal_email = db.Column(db.VARCHAR(20), unique=True)
    cohort = db.Column(db.VARCHAR(100))


cursor.execute(query)
connection.commit()
if __name__ == '__main__':
    # db.create_all()
    manager.run()
