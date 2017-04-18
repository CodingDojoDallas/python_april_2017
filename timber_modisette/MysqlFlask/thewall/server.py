import re
import md5
import os, binascii
from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = os.urandom(24)

mysql = MySQLConnector(app, 'thewall')


@app.route('/')
def index():

	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
	if request.form['name'].isalpha() == False:
		flash("Please Ennter a name more than 2 characters long (Only Letters)")
		return redirect('/')
	if len(request.form['name']) < 2:
		flash("you done fucked up")
		return redirect('/')
	if not EMAIL_REGEX.match(request.form['email']):
		flash("please enter a valid email so i can properly spam you")
		return redirect('/')
	if len(request.form['password']) < 8:
		flash("add some bitches to your password. must be at least 8")
		return redirect('/')
	if request.form['password'] != request.form['passwordConfirm']:
		flash('Passwords do not mactch')
		return redirect('/')
	elif request.form['password'] == request.form['passwordConfirm']:
		userPassword = md5.new(request.form['password']).hexdigest(); 
	# print userPassword
	flash("successful registration")

	query = "INSERT INTO users (name, email, password, created_at, updated_at) VALUES(:name, :email, :password, NOW(), NOW())"
	data = {'name': request.form['name'], 'email': request.form['email'], 'password': userPassword}
	user = mysql.query_db(query, data)


	return redirect('/')

@app.route('/login', methods=['POST'])
def login():
 

	query = "SELECT * FROM users WHERE email = :email"
	data = {'email': request.form['email']}
	userlogin = mysql.query_db(query,data)


	if len(userlogin) != 0 and md5.new(request.form['password']).hexdigest() == userlogin[0]['password']:
		session['name'] = userlogin[0]['name']
		session['user_id'] = userlogin[0]['id']
		return redirect('/wall')

	else:
		flash('invalid credentials')
		return redirect('/')

@app.route('/logout', methods=['post'])
def logout():
	
	session.clear()
	
	return redirect('/')


@app.route('/wall')
def show():
	
	if 'user_id' not in session:
		return redirect('/')
	else:
		username = session['name']

		query = "SELECT messages.content from messages"
		messages = mysql.query_db(query)
		print messages


		
		return render_template('wall.html', messages=messages)





@app.route('/messages', methods=['POST'])
def post():
	print "what"
	print session['user_id']
	query = "INSERT INTO messages (content, users_id, created_at, updated_at ) VALUES(:message, :users_id, NOW(), NOW())"
	data = {'message': request.form['textarea'], 'users_id': session['user_id']}
	print data
	this = mysql.query_db(query, data)

	return redirect('/wall')

# @app.route('/posted')
# def postmessage():
# 	query = "SELECT * FROM messages"
# 	messages = mysql.query_db(query)

# 	print messages


# 	return render_template('wall.html', messages= messages)



app.run(debug=True)




