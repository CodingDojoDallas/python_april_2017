
from flask import Flask, render_template,request,redirect,session,flash
import os
# the "re" module will let us perform some regular expression operations
import re

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d+$')

app = Flask(__name__) 
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET']) 
def index():

	return render_template('index.html') 

# @app.route('/result') 
# def result():
# 	return render_template('result.html') 
 

@app.route('/process', methods=['POST']) 
def submit():

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

	#len(first_name) & len(last_name) & len(password) & len(confirm_password)<1
	if len(email)<1:
		flash('All field are must be required')
	elif len(first_name)<1:
		flash('All field are must be required')
	elif len(last_name)<1:
		flash('All field are must be required')
	elif len(password)<1:
		flash('All field are must be required')
	elif len(confirm_password)<1:
		flash('All field are must be required')

	elif not EMAIL_REGEX.match(email):
		flash('email shoud be vaild email')

	# elif not str.isalpha(str(first_name)) & str.isalpha(str(last_name)):
	# 	print 'First and Last Name cannot contain any numbers'

	elif not str.isalpha(str(first_name)):
		flash('First and Last Name cannot contain any numbers')
	elif not str.isalpha(str(last_name)):
		flash('First and Last Name cannot contain any numbers')
	elif len(password)<9:
		flash('password should be more than 8 characters')
	elif password != confirm_password:
		flash('password not match')
	elif not PASSWORD_REGEX.match(password):
		flash('password should contain one Caps and 1 numeric')
	else:
		flash('Thanks for submitting your information')

	return redirect('/')


app.run(debug=True)

# str.isalpha()

# app = Flask(__name__)
# app.secret_key = "ThisIsSecret!"
# @app.route('/', methods=['GET'])

# def index():
#   return render_template("index.html")


# @app.route('/process', methods=['POST'])
# def submit():
#     if len(request.form['email']) < 1:
#         flash("Email cannot be blank!")
#     # else if email doesn't match regular expression display an "invalid email address" message
#     else:
#         flash("Success!")
#     return redirect('/')






