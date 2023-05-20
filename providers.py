from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app_instance = None
db_instance = None

def get_app():
    global app_instance
    if app_instance is None:
        app = Flask(__name__)
        app.secret_key='MIALY'
        app.debug = True
        app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/roaming'
        app.config['TEMPLATES_AUTO_RELOAD'] = True
        app_instance = app
    return app_instance

def get_db():
    global db_instance
    if db_instance is None:
        db = SQLAlchemy(get_app())
        db_instance = db
    return db_instance