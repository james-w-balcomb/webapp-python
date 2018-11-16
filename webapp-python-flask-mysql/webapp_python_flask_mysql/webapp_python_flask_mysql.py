import pymysql

from flask import Flask

SQL_SELECT_HELLO_WORLD = "SELECT `hello_world`.`hello_world` FROM `hello_world`.`hello_world`;"

webapp_python_flask_mysql_app = Flask(__name__, instance_relative_config=True)

webapp_python_flask_mysql_app.config.from_object("config")
webapp_python_flask_mysql_app.config.from_pyfile("config.py")


def get_mysql_connection(host, port, user, passwd, db):
    
    mysql_connection = pymysql.connect(host = host,
                                       port = port,
                                       user = user,
                                       passwd = passwd,
                                       db = db)
    
    return mysql_connection


def get_mysql_cursor(mysql_connection):
    
    mysql_cursor = mysql_connection.cursor()
    
    return mysql_cursor


@webapp_python_flask_mysql_app.route("/")
def wsgi_script_alias_root():
    
    host = webapp_python_flask_mysql_app.config["MYSQL_HOST"]
    port = webapp_python_flask_mysql_app.config["MYSQL_PORT"]
    user = webapp_python_flask_mysql_app.config["MYSQL_USER"]
    passwd = webapp_python_flask_mysql_app.config["MYSQL_PASSWD"]
    db = webapp_python_flask_mysql_app.config["MYSQL_DB"]
    
    mysql_connection = get_mysql_connection(host, port, user, passwd, db)
    
    mysql_cursor = get_mysql_cursor(mysql_connection)
    
    query_results = mysql_cursor.execute(SQL_SELECT_HELLO_WORLD)
    
    records = mysql_cursor.fetchall()
    
    return str(records[0][0])
