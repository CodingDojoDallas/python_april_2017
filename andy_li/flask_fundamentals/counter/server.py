from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "my_secret_key"

@app.route("/", methods = ["GET", "POST"])
def index():
    if len(session) == 0:
        session["count"] = 0

    session["count"] += 1
    return render_template("index.html", count=session["count"])

@app.route("/lvl1", methods = ["POST"])
def lvl1():
    session["count"] += 1
    return redirect("/")

@app.route("/lvl2", methods = ["POST"])
def lvl2():
    session["count"] = 0
    return redirect("/")

app.run(debug = True)
