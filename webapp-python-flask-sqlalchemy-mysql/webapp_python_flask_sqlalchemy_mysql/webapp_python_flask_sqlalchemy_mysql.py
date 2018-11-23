import pymysql

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

webapp_python_flask_sqlalchemy_mysql_app = Flask(__name__, instance_relative_config=True)
webapp_python_flask_sqlalchemy_mysql_app.config.from_object("config")
webapp_python_flask_sqlalchemy_mysql_app.config.from_pyfile("config.py")

db = SQLAlchemy(webapp_python_flask_sqlalchemy_mysql_app)

from models import HelloWorld

@webapp_python_flask_sqlalchemy_mysql_app.route("/")
def wsgi_script_alias_root():

    hello_world = HelloWorld.query.one()
    
    return str(hello_world.hello_world)
