from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# my db connection
local_server= True
app = Flask(__name__)
app.secret_key='MIALY'

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/roaming'
db=SQLAlchemy(app)
migrate = Migrate(app, db)

#here we will create db models that is tables
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

@app.route('/')
def hello_world():
    try:
       User.query.all()
       return 'My db is connected'
    except:
       return 'My db is not connected'
    # return render_template('index.html')
     

@app.route('/encode')
def encode():
    return render_template('encode.html')

@app.route('/decode')
def decode():
    return render_template('decode.html')

if __name__ == '__main__':
    app.run()
