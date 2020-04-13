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
('Adrian','Shikwambana','Beast','AdriGitHub','4657464416','adrian@yahoo.com','C26 Data Eng'),
('James','King','JameIV','JMGitHub','6465456','JamesK@outlook.com','C26 Data Eng'),
('Floyd','Rogers','Flo278','PRogersGitHub','587464','FloydRogers12@gmail.com','C26 Data Eng'),
('Dangerous','Black','DangerZone58','DangerGihtub','65664','Dangerous@yahoo.com','C26 Data Eng'),
('Danny','Peters','Danny_boy12','DannyGitHub','65464','DannyyBO@gmail.com','C26 Data Eng');"""


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
    manager.run()
    db.create_all()
