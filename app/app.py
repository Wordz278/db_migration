from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
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


def main():
    db.create_all()


if __name__ == "__main__":
    manager.run()
