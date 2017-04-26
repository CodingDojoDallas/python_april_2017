
from flask import Flask, render_template,request,redirect,session,flash
import os

app = Flask(__name__) 
app.secret_key = os.urandom(24)

@app.route('/') 
def index():

	return render_template('index.html') 

@app.route('/result') 
def result():
	return render_template('result.html') 
 

@app.route('/verification', methods=['POST']) 
def create_user():
	name = request.form['name'] #remember to put [] not () because it's tuple
	location = request.form['location']
	favorite_language = request.form['favorite_language']
	comment = request.form['comment']

	session['name'] = name
	session['location'] = location
	session['favorite_language'] = favorite_language
	session['comment'] = comment


	if len(name)<1 or len(comment)<1:
		error = False
		flash("Name and comment cannot be empty")
	
	elif len(comment)>120:
		error = False
		flash("commnet should not be more than 120")

	elif len(name)<1:
		flash("Name cannot be empty")
		error = False
	else:
		flash("Yor did it")
		error = True
		
	if error == False:
		return redirect('/')
	else:
		return redirect('/result')


app.run(debug=True)




