from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import md5, os, binascii

app = Flask(__name__)

mysql = MySQLConnector(app, 'flask_login_w03948')

app.secret_key = 'adlfkjasd;flkj'


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
	salt = binascii.b2a_hex(os.urandom(15))
	query = 'INSERT INTO users (name, email, password, salt, created_at, updated_at) VALUES (:name, :email, :password, :salt, NOW(), NOW())'
	values = {
		'name': request.form['name'],
		'email': request.form['email'],
		'password': md5.new(request.form['password'] + salt).hexdigest(),
		'salt': salt,
	}

	mysql.query_db(query, values)
	return redirect('/users')


@app.route('/login', methods=['POST'])
def login():
	#go to the db check the email
	query = 'SELECT * FROM users WHERE email = :email;'
	values = { 'email': request.form['email'] }

	user = mysql.query_db(query, values)

	if len(user) != 0 and md5.new(request.form['password'] + user[0]['salt']).hexdigest() == user[0]['password']:
		session['user_id'] = user[0]['id']
		return redirect('/users')
	else:
		flash('invalid credentials')
		return redirect('/')

@app.route('/logout')
def logout():
	session.clear()
	return redirect('/')

@app.route('/users')
def users():
	if 'user_id' not in session:
		return redirect('/')
	else:
		return render_template('success.html')

app.run(debug=True) 