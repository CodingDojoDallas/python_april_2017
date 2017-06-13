from flask import *
import random

app=Flask(__name__)

app.secret_key ='thisissecret'

@app.route('/')
def index():
	if 'randomint' not in session:
		session['randomint']=random.randint(1,100)
	print session['randomint']
	print type(session['randomint'])
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	session['number'] = int(request.form['number'])
	print session['number'] > session['randomint'] 
	print type(session['number'])
	print session['number']
	if session['number'] > session['randomint']:
		session['status'] = "above"
	elif session['number'] < session['randomint']:
		session['status'] = "below"
	else:
		session['status'] = "on the money"
	print session['status']
	return redirect('/')

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)