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
('Thabo','Moprwa','Thiboz','SthiboGitHub','755669','thabo@yahoo.com','C27 Data Eng'),
('Prince','Rich','Princilo','PrinceGitHub','555765','prince@gmail.com','C27 Data Eng'),
('Rachel','Mayila','Rachie_Rich','RachelGitHub','654608','rachel@outlook.com','C27 Data Eng'),
('Mbali','Lindsay','Mabli28','MbaliGithub','45434789','mablenhle@yahoo.com','C27 Data Eng'),
('Nthabiseng','Queen','Nthabi','NthabiGitHub','23764','nthabi@yahoo.com','C27 Data Eng');"""


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/prod'
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
