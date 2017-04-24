from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "my_secret_key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods = ["POST"])
def result():
    if len(request.form["name"]) == 0 or len(request.form["comment"]) == 0:
        flash("Name and/or comment can't be blank. Please enter a valid name/comment.")
        return redirect("/")

    if len(request.form["comment"]) > 120:
        flash("Comments are limited to 120 characters. Please enter comments up to 120 characters.")
        return redirect("/")

    else:
        data = {
            "name" : request.form["name"],
            "loc_select" : request.form["loc_select"],
            "fav_lang" : request.form["fav_lang"],
            "comment" : request.form["comment"]}

        print data
        return render_template("result.html", data = data)

app.run(debug = True)
