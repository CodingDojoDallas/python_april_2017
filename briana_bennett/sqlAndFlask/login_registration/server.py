from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re, md5, os, binascii

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


app = Flask(__name__)
mysql = MySQLConnector(app,'login_registration')
app.secret_key = "briannanadandiSECretqui"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['post'])
def create():
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	confirm_pwd = request.form['confirm_pwd']

	if not first_name.isalpha() or len(first_name) <= 2:
		flash("invalid first name")
		return redirect('/')
	elif not last_name.isalpha() or len(last_name) <= 2:
		flash("invalid last name")
		return redirect('/')
	elif not EMAIL_REGEX.match(email):
		flash("invalid email")
		return redirect('/')
	elif len(password) < 8:
		flash("your password must be at least 8 characters")
		return redirect('/')
	elif confirm_pwd != password:
		flash('passwords do not match')
		return redirect('/')

	else:
		salt = binascii.b2a_hex(os.urandom(16))
		hashed_pw = md5.new(password + salt).hexdigest()
		
		query = "insert into users (first_name, last_name, email, password, salt) values (:first_name, :last_name, :email, :password, :salt);" 
		data = {
			"first_name": first_name,
			"last_name": last_name,
			"email": email,
			"password": hashed_pw,
			'salt': salt
		}


		user_id = mysql.query_db(query, data)
		session['user_id'] = user_id
		#save user_id in session
		print data
		return redirect('/success')

@app.route('/login', methods=['POST'])
def login():

	query = 'select * from users where email = :email;'
	data = {
		"email": request.form['email']
	}

	user = mysql.query_db(query, data)
	
	# if len(user) != 0 and user[0]['password'] == md5.new(request.form['password'] + user[0]['salt']).hexdigest():
	# 	session['user_id'] = user[0]['id']

	if len(user) == 0:
		print "no email"
		flash("sorry, we don't recognize that email")
		return redirect('/')
	if user[0]['password'] != md5.new(request.form['password'] + user[0]['salt']).hexdigest():
		session['user_id'] = user[0]['id']
		flash("incorrect password")
		return redirect('/')
	else:
		return redirect('/success')

	# else:
	# 	flash('login invalid')
	# 	return redirect('/')

@app.route('/success')
def success():
	if 'user_id' not in session:
		return redirect('/')
	else:
		return render_template('success.html')

@app.route('/logout', methods=['POST'])
def logout():
	session.clear()
	return redirect('/')


app.run(debug = True)