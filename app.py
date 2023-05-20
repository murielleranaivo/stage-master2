from flask import render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,logout_user
from sqlalchemy import text
from encode import encode_records_to_tap
from models.CdrModel import CdrModel
from datetime import datetime
from providers import get_app, get_db

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

# Function to parse the date string into a datetime object
def parse_date(date_string):
    return datetime.strptime(date_string, '%Y%m%d%H%M%S')

def insert_cdrs_to_db(cdrpath):
    cdr_records = []
    with open(cdrpath, 'r') as file:
        cdr_records = file.readlines()
        
    records = []
    for cdr_record in cdr_records:
        cdr_record = cdr_record.strip()
        cdr_fields = cdr_record.split("|")
        record = CdrModel(
            call_type=int(cdr_fields[0]),
            service_code=int(cdr_fields[1]),
            ne_code=cdr_fields[2].strip(),
            in_route=cdr_fields[3].strip(),
            out_route=cdr_fields[4].strip(),
            imsi=cdr_fields[5].strip(),
            sgsn_address=cdr_fields[6].strip(),
            a_number=cdr_fields[7].strip(),
            b_number=cdr_fields[8].strip(),
            c_number=cdr_fields[9].strip(),
            apn_address=cdr_fields[10].strip(),
            pdp_address=cdr_fields[11].strip(),
            call_date=parse_date(cdr_fields[12]),
            call_duration=int(cdr_fields[13]),
            data_volume_inc=int(cdr_fields[14]),
            data_volume_out=int(cdr_fields[15]),
            teleservice=cdr_fields[16].strip(),
            bearerservice=cdr_fields[17].strip(),
            camel_flag=cdr_fields[18].strip(),
            camel_service_level=cdr_fields[19].strip(),
            camel_service_key=cdr_fields[20].strip(),
            camel_default_call_handling=cdr_fields[21].strip(),
            camel_server_address=cdr_fields[22].strip(),
            camel_msc_address=cdr_fields[23].strip(),
            camel_call_ref_num=cdr_fields[24].strip(),
            camel_init_cf_indicator=cdr_fields[25].strip(),
            camel_destination_num=cdr_fields[26].strip(),
            camel_modification=cdr_fields[27].strip(),
            supplimentary_num=cdr_fields[28].strip(),
            network_time=cdr_fields[29].strip(),
            reason_for_cleardown=cdr_fields[30].strip(),
            partial_indicator=cdr_fields[31].strip(),
            partial_seq_num=cdr_fields[32].strip(),
            imei_num=cdr_fields[33].strip(),
            chrono_num=cdr_fields[34].strip(),
            charging_id=cdr_fields[35].strip(),
            subscriber_type=cdr_fields[36].strip()
        )
        records.append(record)
        
    db.session.add_all(records)
    db.session.commit()

@app.route('/encode')
def encode():
    cdr_records = CdrModel.query.all()
    
    encode_records_to_tap(cdr_records)
    
    return render_template('encode.html')

@app.route('/decode')
def decode():
    filepath = 'demo.tap'
    
    
    
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
