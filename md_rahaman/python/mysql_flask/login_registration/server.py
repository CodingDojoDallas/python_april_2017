from flask import Flask, request, redirect, render_template, session, flash
import os, binascii
from mysqlconnection import MySQLConnector
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = os.urandom(24)

mysql = MySQLConnector(app,'login_registration')
@app.route('/')

def index():
	if 'user_id' not in session:
		session['user_id'] = 0
	# user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"

	# query = "SELECT * FROM users"
	# friends = mysql.query_db(query)
	# print friends
	return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
	query_data = {'email':email}
	user = mysql.query_db(user_query, query_data)
	session['user_id'] =user[0]['id']

	if user[0]:
		encrypted_password = md5.new(password + user[0]['salt']).hexdigest();
		# print 'new encrypted password', encrypted_password
		if user[0]['password'] == encrypted_password:
			print 'successful'
			return render_template('success.html')
		else:
			flash('invalid password')
	else:
		flash('invalid email')
	return redirect('/')


@app.route('/regestration', methods=['POST'])
def regestration():
	email = request.form['email']
	print 'email-',email
	print len(email)

	first_name = request.form['first-name']
	print 'First name-',first_name
	print len(first_name)

	last_name = request.form['last-name']
	print 'Last name-',last_name
	print len(last_name)

	password = request.form['password']
	print 'password-',password
	print len(password)

	confirm_password = request.form['passwordconfirm']
	print 'confirm password-',confirm_password
	print len(confirm_password)

	error = True
	#len(first_name) & len(last_name) & len(password) & len(confirm_password)<1
	if len(first_name)<2 or len(last_name)<2:
		flash('letters only, at least 2 characters and that it was submitted')
		error = False
	elif not str.isalpha(str(first_name)) or not str.isalpha(str(last_name)):
		flash('letters only, at least 2 characters and that it was submitted')
		error = False
	elif not EMAIL_REGEX.match(email):
		flash('email shoud be vaild email')
		error = False
	elif len(password)<9:
		flash('password should be more than 8 characters')
		error = False
	elif password != confirm_password:
		flash('password not match')
		error = False

				##############################
				# inserting to database		#
				##############################
	if error == True:
		salt = binascii.b2a_hex(os.urandom(15))
		encrypted_pw = md5.new(password + salt).hexdigest()
		# print encrypted_pw
		# print salt
		insert_query = "INSERT INTO users (first_name,last_name,email,password,salt,created_at,updated_at) VALUES (:first_name, :last_name,:email, :encrypted_pw, :salt, NOW(), NOW())"
		query_data = {
					  'first_name':first_name,
		              'last_name':last_name,
					  'email': email, 
					  'encrypted_pw': encrypted_pw, 
					  'salt': salt, 
					  }

		session['user_id'] = mysql.query_db(insert_query, query_data)

		return render_template('success.html')
	return redirect('/')

	# user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"

	

	
	
app.run(debug=True)