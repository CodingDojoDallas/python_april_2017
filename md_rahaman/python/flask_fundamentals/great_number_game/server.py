
from flask import Flask, render_template,request,redirect,session
import os
from random import randint


app = Flask(__name__) 
app.secret_key = os.urandom(24)

@app.route('/') 
def index():
	if 'random' not in session:
		session['random'] = randint(1,100) #generate random between 1-100
	print 'random num: ',session['random']
	# print session.get('random')



	return render_template('index.html')


@app.route('/usernum', methods = ['POST'])
def user_num():
	num = int(request.form['num'])

	print type(num)
	#was the guess high, low, or accurate?
	if num == session.get('random'):
		session['userkey'] = 'Accurate' #saving to session dictionary
		print 'Accurate'
	elif num < session.get('random'):
		session['userkey'] = 'Too Low' #saving to session dictionary
		print 'Too Low'
	else:
		session['userkey'] = 'Too High' #saving to session dictionary
		print 'Too high'


	return redirect('/')

@app.route('/restart', methods = ['POST'])
def restart():
	session.pop('random',None)
	session.pop('userkey',None)
	return redirect('/')

 
app.run(debug=True)