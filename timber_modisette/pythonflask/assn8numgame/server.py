import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "theendisnigh"

@app.route('/')
def index():
	
	if 'randomNum' not in session:
		session['randomNum'] = random.randint(1,101)

	print session['randomNum']
	return render_template('index.html')



@app.route('/userguess', methods=['POST'])
def user_guess():

	num = int(request.form['textbox'])
	print num
	print type(num)



	if num == session.get('randomNum'):
		session['userinput'] = "accurate"
		# session.pop('randomNum', None)
		

	elif num < session.get('randomNum'):
		session['userinput'] = "too low"
	

	elif num > session.get('randomNum'):
		session['userinput'] = "too high"

	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():

	session.pop('randomNum', None)
	session.pop('userinput', None)

	return redirect('/')

app.run(debug=True)






