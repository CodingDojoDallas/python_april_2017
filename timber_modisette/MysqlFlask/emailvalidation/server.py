import re
from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'theendisnigh'
mysql = MySQLConnector(app, 'email')


@app.route('/')
def index():
	# query = "SELECT * FROM emails"
	# emails = mysql.query_db(query)

	return render_template('index.html') 

@app.route('/process', methods=['POST'])
def process():
	email = request.form['email']
	if len(request.form['email']) < 1:
		flash("Email cannont be empty")
		return redirect('/')

	elif not EMAIL_REGEX.match(request.form['email']):
		flash("invalid Email Address")
		return redirect('/')
	else:
		flash("success")

	query = "INSERT INTO emails (email, created_at) VALUES(:email, NOW())"
	data = {'email': request.form['email']}
	user = mysql.query_db(query, data)
	

	return redirect('/success')


@app.route('/success')
def display():
	flash("success")
	query = "SELECT * FROM emails"
	emails = mysql.query_db(query)
	print emails

	return	render_template('success.html', all_emails=emails)

app.run(debug=True)








