from flask import Flask

webapp_python_flask = Flask(__name__)


@webapp_python_flask.route("/")
def wsgi_script_alias_root():
    return "Hello World"
