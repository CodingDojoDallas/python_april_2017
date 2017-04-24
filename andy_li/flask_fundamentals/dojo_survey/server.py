from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods = ["POST"])
def result():
    data = {
        "name" : request.form["name"],
        "loc_select" : request.form["loc_select"],
        "fav_lang" : request.form["fav_lang"],
        "comment" : request.form["comment"]}

    print data["name"]
    print data["loc_select"]
    print data["fav_lang"]
    print data["comment"]

    return render_template("result.html", data = data)

app.run(debug = True)
