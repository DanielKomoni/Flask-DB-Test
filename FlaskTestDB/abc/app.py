from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/alchemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30), unique=True)

    def __init__(self,name):
        self.name=name

@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"