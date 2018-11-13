import os

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.sqlite"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)


@app.route("/", methods=["GET", "POST"])
def home():
    books = None
    if request.form:
        try:
            book = Book(title=request.form.get("title"))
            db.session.add(book)
            db.session.commit()
        except Exception as ex:
            print("Failed to add book")
            print(ex)

    books = Book.query.all()
    
    return render_template("home.html", books=books)


@app.route("/update", methods=["POST"])
def update():
    try:
        new_title = request.form.get("new_title")
        old_title = request.form.get("old_title")
        book = Book.query.filter_by(title=old_title).first()
        book.title = new_title
        db.session.commit()
    except Exception as ex:
        print("Failed to update book title")
        print(ex)
    
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    try:
        title = request.form.get("title")
        book = Book.query.filter_by(title=title).first()
        db.session.delete(book)
        db.session.commit()
    except Exception as ex:
        print("Failed to delete book")
        print(ex)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
