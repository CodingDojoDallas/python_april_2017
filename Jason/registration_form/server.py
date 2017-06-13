from flask import Flask, render_template, redirect, session,request,flash
import re

app = Flask(__name__)
app.secret_key="yayyupdo"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['POST',])
def resister():
	session['email']=request.form['email']
	session['first_name']=request.form['first_name']
	session['last_name']=request.form['last_name']
	session['password']=request.form['password']
	session['confirm_password']=request.form['confirm_password']

	print request.form	

	if session['email'] is '' \
	   or session['first_name'] is '' \
	   or session['last_name'] is '' \
	   or session['password'] is '' \
	   or session['confirm_password'] is '':
		flash("All fields are required and must not be blank.", "empty_field")
 
	if re.compile('[0-9][A-Z]').search(session['first_name']) \
	   or re.compile('[0-9][A-Z]').search(session['last_name']):
		flash("First and Last Name cannot contain any numbers.", "invalid_name")

	if len(session['password']) < 8 :
		flash("Password should be more than 8 characters.", "password_error")	

	if session['password'] != session['confirm_password']:
		flash("Password and Password confirmation should match.", "password_error")
	
	if not re.compile('[0-9]+').match(session['password']) and not re.compile('[A-Z]+').match(session['password']):
	   	flash("Password must have one one uppercase letter and one numeric value.")

	return redirect('/')



app.run(debug=True)

print re.search('[a-z]',"ecGEG")