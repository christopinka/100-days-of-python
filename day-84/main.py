from flask import Flask, redirect, render_template, request
from replit import db

app = Flask(__name__)


@app.route("/signup", methods=["POST"])
def createUser():
    keys = db.keys()
    form = request.form
    if form["username"] not in keys:
        db[form["username"]] = {
            "name": form["name"],
            "password": form["password"]
        }
        return redirect("/login")
    else:
        return redirect("/signup")


@app.route("/login", methods=["POST"])
def doLogin():
    keys = db.keys()
    form = request.form
    if form["username"] not in keys:
        return redirect("/login")
    else:
        if form["password"] == db[form["username"]]["password"]:
            return f"""Hello {db[form["username"]]["name"]}"""
        else:
            return redirect("/login")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route('/')
def index():
    page = """<p><a href="/signup">Sign up</a></p>
    <p><a href="/login">Log in</a></p>"""
    return page


app.run(host='0.0.0.0', port=81)
