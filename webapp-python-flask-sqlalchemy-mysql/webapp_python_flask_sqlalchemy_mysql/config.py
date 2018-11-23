import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

SECRET_KEY = "qwertyuiopasdfghjklzxcvbnm"

SQLALCHEMY_DATABASE_URI = "mysql://WebappPythonFlask:WebappPythonFlask*$@127.0.0.1:33061/hello_world"
