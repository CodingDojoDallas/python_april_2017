from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,"email_valid_db")
app.secret_key = "my_secret_key"

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/error")
def error():
    print "E-mail invalid."
    return redirect("/")

@app.route('/success')
def success():
    #get necessary data from DB
    query = "select * from emails;"
    emails = mysql.query_db(query)

    #render success.html
    return render_template('success.html', all_emails = emails)

@app.route("/emails", methods = ["POST"])
def create_email():
    if len(request.form["email"]) < 1:
        flash("E-mail can't be blank!")
        return redirect("/")
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid E-mail address!")
        return redirect("/")
    else:
        query1 = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW());"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                 "email": request.form["email"],
               }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query1, data)

        query2 = "SELECT * FROM emails"                             # define your query
        emails = mysql.query_db(query2)                             # run query with query_db()
        flash("The e-mail address you entered ({}) is valid. Thanks!".format(emails[len(emails) - 1]["email"]))
        return redirect("/success")

@app.route("/delete/<email_id>", methods = ["POST"])
def delete(email_id):
    query1 = "DELETE from emails where emails.id = :id"
    data = {
             "id": email_id,
           }
    mysql.query_db(query1, data)

    return redirect("/success")


app.run(debug = True)
