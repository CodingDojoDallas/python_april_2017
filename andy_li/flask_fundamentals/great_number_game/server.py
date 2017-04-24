from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "my_secret_key"

@app.route("/", methods = ["GET", "POST"])
def index():
    if "num" not in session:
        session["num"] = random.randint(1, 100)
    print session

    if "msg" in session:
        return render_template("index.html", msg = session["msg"], num = session["num"])

    return render_template("index.html")

@app.route("/guess", methods = ["POST"])
def result():
    session["guess"] = int(request.form["guess_num"])

    if session["guess"] < session["num"]:
        session["msg"] = "low"
    elif session["guess"] > session["num"]:
        session["msg"] = "high"
    else:
        session["msg"] = "correct"

    return redirect("/")

@app.route("/correct", methods = ["POST"])
def correct():
    session.clear()

    return redirect("/")

app.run(debug = True)
