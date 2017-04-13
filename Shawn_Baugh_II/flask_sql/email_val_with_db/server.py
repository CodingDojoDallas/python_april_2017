from flask import Flask, redirect, render_template, session, flash, request
from mysqlconnection import MySQLConnector
import re
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'thisissecret'
mysql = MySQLConnector(app, 'email_val')

@app.route('/')
def index():
    query = "SELECT * FROM email_val"
    emails = mysql.query_db(query)
    return render_template('index.html', all_emails=emails)

@app.route('/process', methods=['POST'])
def process():



    is_valid = True
    if len(request.form['email']) < 1:
        is_valid = False
        flash('Email cannot be empty')
    elif not email_regex.match(request.form['email']):
        flash('Invalid Email Address!')
        is_valid = False
    if is_valid == False:
        return redirect('/')

    else:
        flash('Success!')

        query = "INSERT INTO email_val (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"

        data = {
            'email': request.form['email']
        }
        mysql.query_db(query, data)

        return redirect('/success')


@app.route('/success')
def success():
    query = "select * from email_val"
    emails = mysql.query_db(query)
    return render_template('success.html',emails=emails)

app.run(debug=True)
