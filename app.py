from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

# my db connection
local_server= True
app = Flask(__name__)
app.secret_key='MIALY'

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/roaming'
db=SQLAlchemy(app) 


#here we will create db models that is tables
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
  
    
    
@app.route('/')
def hello_world():
    a=Test.query.all()
    print(a)
    return render_template('index.html')
    #try:
    #    Test.query.all()
    #    return 'My db is connected'
    #except:
    #    return 'My db is not connected'
     

@app.route('/encode')
def encode():
    return render_template('encode.html')

@app.route('/decode')
def decode():
    return render_template('decode.html')

if __name__ == '__main__':
    app.run()
