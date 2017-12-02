import os
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
manager = Manager(app)
app.config['SECRET_KEY'] = 'hard xvvv'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "mysql://root:1234@localhost/robo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def helloword():
    return 'hello, world'

if __name__ == '__main__':
    manager.run()



