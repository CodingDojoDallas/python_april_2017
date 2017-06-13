from flask import Flask, request, redirect, render_template, session, flash
import os
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = os.urandom(24)

mysql = MySQLConnector(app,'email')
@app.route('/')
def index():
	# friends = mysql.query_db("SELECT * FROM friends")
	# print friends

	# query = "SELECT * FROM friends"
	# friends = mysql.query_db(query)
	return render_template('index.html')
# @app.route('/friends/<friend_id>')
# def show():
#     # add a friend to the database!
# 	query = "SELECT * FROM friends WHERE id = :specific_id"
# 	data = {'specific_id': friend_id}
# 	friends = mysql.query_db(query, data)
# 	return render_template('index.html', one_friend=friends[0])

# @app.route('/success')
# def success():


@app.route('/validation', methods=['POST'])
def validation():
	email = request.form['email']
	# print email
	if not EMAIL_REGEX.match(email):
		flash('email shoud be vaild email')
	else:
		query = "INSERT INTO users (email, created_at, updated_at)VALUES (:email, NOW(), NOW())"
		data = {
	 
	             'email': request.form['email']
	           }
	    # Run query, with dictionary values injected into the query.
		mysql.query_db(query, data)
		flash('The email address you entered (--'+request.form['email']+'--) is a VALID email address! Thank you!')
		emails = mysql.query_db("SELECT * FROM users")
		print emails
		return render_template('success.html', all_emails = emails)
		
	return redirect('/')
	

app.run(debug=True)