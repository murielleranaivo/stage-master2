from flask import render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
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

#this is for getting unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



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
    
    if not User.is_authenticated:
        return render_template('login.html')
    else:

        return render_template('decode.html',username=current_user.username)
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

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method =="POST":
        
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        
        user=User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Login Success","primary")
            return redirect(url_for('decode'))
        else :
            flash('invalid credentials','danger')
            return render_template('login.html')  
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
@login_required
def lougout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
    

#username=current_user.username
