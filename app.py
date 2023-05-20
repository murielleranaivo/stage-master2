from flask import render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,logout_user
from sqlalchemy import text
from decode import decode_tap_to_csv
from encode import encode_records_to_tap
from insert import insert_cdrs_to_db, insert_tap_to_db
from models.CdrModel import CdrModel
from providers import get_app, get_db
import os

# my db connection
local_server= True

app = get_app()

db = get_db()

#here we will create db models that is tables
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(1000))
    
    
@app.route('/')
def hello_world():
    # try:
    #    User.query.all()
    #    return 'My db is connected'
    # except:
    #    return 'My db is not connected'
    return render_template('index.html')

@app.route('/encode')
def encode():
    cdr_records = CdrModel.query.all()
    
    encode_records_to_tap(cdr_records)
    
    return render_template('encode.html')

@app.route('/decode')
def decode():
    filepath = 'demo.tap'
    
    decode_tap_to_csv(filepath)
    
    return render_template('decode.html')

@app.route('/insert')
def insert():
    cdrpath = 'demo.tap' #cdr.txt|demo.tap
    
    extension = os.path.splitext(cdrpath)[1]

    if extension == ".txt":
        insert_cdrs_to_db(cdrpath)
    elif extension == ".tap":
        insert_tap_to_db(cdrpath)
    
    return render_template('decode.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method =="POST":
        
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        
        user=User.query.filter_by(email=email).first()
        if user:
            print('email already exists')
            return render_template('/signup.html')
        
        encpassword=generate_password_hash(password)
        query=f"INSERT INTO `user` (`username`, `email`, `password`) VALUES ('{username}', '{email}', '{encpassword}')"
        db.session.execute(text(query))
        db.session.commit()
        
        return render_template('login.html')

    return render_template('signup.html')

@app.route('/lougout')
def lougout():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
