from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "ImASecret"
import random

@app.route('/')
def index():
	if 'randomNumber' not in session:
		session['randomNumber'] = random.randint(1, 100)
	
	print "got random"
	print session
	if "low_high" in session: 
		return render_template("index.html", guess = session['guess'], low_high = session['low_high'])
	
	if 'guess' in session:
		return render_template("index.html", guess = session['guess'], low_high = session['low_high'])
	
	return render_template("index.html")

@app.route('/playing', methods=['POST'])
def playing():
	

	session['guess'] = request.form['guess']
	
	print session['guess']
	print "got session guess"
	

	print "guess is {}".format(session['guess'])

	if int(session['guess']) < session['randomNumber']:
		session['low_high'] = 'low'
		print session['low_high']
		print "guess is too {}".format(session['low_high'])
	elif int(session['guess']) > session['randomNumber']:
		session['low_high'] = 'high'
		print "guess is too {}".format(session['low_high'])
	elif int(session['guess']) == session['randomNumber']:
		session['low_high'] = 'same'
	

	return redirect('/')

@app.route('/again', methods=['GET'])
def again():

	session.clear()
	
	return redirect('/')

app.run(debug = True)