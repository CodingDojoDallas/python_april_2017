
from flask import Flask, render_template,request,redirect,session
import os

app = Flask(__name__) 
app.secret_key = os.urandom(24)

@app.route('/') 
def index():
	if session.get('counter') is None:
		session['counter'] = 1

	# else:
	# 	print 'ajsf;ljsaf;ldjaflkdasj'
	# 	if session['counter'] == 0:
	# 		session['counter'] = 0

	return render_template('index.html')

@app.route('/increment')
def incrementsession():
	# session['counter'] = 0 
	session['counter'] +=2
	return redirect('/')

@app.route('/reset')
def reset():
	session['counter'] = 1
	return redirect('/')

 
app.run(debug=True)