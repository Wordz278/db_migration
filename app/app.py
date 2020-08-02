from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/prod'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Recruits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    github_name = db.Column(db.String(100))
    id_number = db.Column(db.BigInteger)
    personal_email_address = db.Column(db.String(100), unique=True)


if __name__ == "__main__":
    manager.run()
