from flask import Flask, render_template
from .github import get_user_data
from .exceptions import NotFoundException

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/users/<username>")
def user_info(username):
  try:
    repos = get_user_data(username)
    return render_template("user.html", repos=repos, username=username)
  except NotFoundException:
    return render_template("404.html"), 404
