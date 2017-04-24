from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "my_secret_key"

@app.route("/")
def index():
    if "gold_ttl" and "msgs" not in session:
        session["gold_ttl"] = 0
        session["msgs"] = []

    print session
    return render_template("index.html", gold_total = session["gold_ttl"], activity_msgs = session["msgs"])

@app.route("/process_money", methods = ["POST"])
def process_money():
    clicked_bldg = request.form["bldg"]

    if clicked_bldg == "farm":
        gold = random.randint(10, 20)
        session["gold_ttl"] += gold
    elif clicked_bldg == "cave":
        gold = random.randint(5, 10)
        session["gold_ttl"] += gold
    elif clicked_bldg == "house":
        gold = random.randint(2, 5)
        session["gold_ttl"] += gold
    elif clicked_bldg == "casino":
        gold = random.randint(-50, 50)
        session["gold_ttl"] += gold

    msg_dict = {}
    if gold >= 0:
        result = "Earned"
        msg_dict["color"] = "green"
    elif gold < 0:
        result = "Lost"
        msg_dict["color"] = "red"

    msg_str = "{} {} gold from the {}!".format(result, abs(gold), clicked_bldg)
    msg_dict["msg"] = msg_str
    session["msgs"].insert(0, msg_dict)

    print session
    return redirect("/")

@app.route("/reset", methods = ["POST"])
def reset():
    session.clear()
    return redirect("/")

app.run(debug = True)
