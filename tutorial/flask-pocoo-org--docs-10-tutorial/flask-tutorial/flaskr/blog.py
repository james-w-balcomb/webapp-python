from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flaskr.auth import login_required
from flaskr.db import get_db
from werkzeug.exceptions import abort

bp = Blueprint("blog", __name__)


def get_post(id, check_author=True):
    post = get_db().execute(
        "SELECT post.id, post.title, post.body, post.created, post.author_id, user.username"
        " FROM post INNER JOIN user ON post.author_id = user.id"
        " WHERE post.id = ?",
        (id,)
    ).fetchone()
    
    if post is None:
        abort(404, "Post id {0} does not exist.".format(id))
    
    if check_author and post["author_id"] != g.user["id"]:
        abort(403)
    
    return post


@bp.route("/")
def index():
    db = get_db()
    posts = db.execute("SELECT post.id, post.title, post.body, post.created, post.author_id, user.username FROM post INNER JOIN user ON post.author_id = user.id ORDER BY post.created DESC").fetchall()
    return render_template("blog/index.html", posts=posts)


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO post (title, body, author_id)"
                " VALUES (?, ?, ?)",
                (title, body, g.user["id"])
            )
            db.commit()
            return redirect(url_for("blog.index"))

    return render_template("blog/create.html")


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE post"
                " SET title = ?, body = ?"
                " WHERE id = ?",
                (title, body, id)
            )
            db.commit()
            return redirect(url_for("blog.index"))

    return render_template("blog/update.html", post=post)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute("DELETE FROM post WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("blog.index"))
