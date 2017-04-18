import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key= 'theendisnigh'

@app.route('/')
def index():
	# if 'gold' not in session:
	if 'gold' not in session:
		session['gold'] = 2
	if 'activities' not in session:
		session['activities'] = [ ]

	
	

	# print session['gold']
	

	return render_template('index.html')



@app.route('/processmoney', methods=['POST'])
def process_money():

	if request.form['action'] == '1020':
		randomnum = random.randint(10,20)
		message = "earned {} golds from the farm".format(randomnum)
		session['activities'].append({'color':'green', 'message': message})
		session['gold'] = randomnum +session['gold']
		

		
	elif request.form['action'] == '0510':
		randomnum = random.randint(5,10)
		message = "earned {} golds from the cave".format(randomnum)
		session['activities'].append({'color':'green', 'message': message})
		session['gold'] = randomnum +session['gold']

	elif request.form['action'] == '0205':
		randomnum = random.randint(2,5)
		message = "earned {} golds from the house".format(randomnum)
		session['activities'].append({'color':'green', 'message': message})
		session['gold'] = randomnum +session['gold']

	elif request.form['action'] == '050':
		select = random.randint(1,2)
		if select == 1:
			randomnum = random.randint(60,100)
			message = "lost {} golds from the casino".format(randomnum)
			session['activities'].append({'color':'red', 'message': message})
			session['gold'] = session['gold'] - randomnum
		else:
			randomnum = random.randint(0,100)
			message = "earned {} golds from the casino".format(randomnum)
			session['activities'].append({'color':'green', 'message': message})
			session['gold'] = randomnum + session['gold']


	if session['gold'] > 500:
		session['gold'] = "You Have Won!"

	if request.form['action'] == 'resetbutton':
		session.pop('gold', None)
		session.pop('activites', None)
		


	if session['gold'] < 1:
		session['gold'] = "You Have Lost!"

	if request.form['action'] == 'resetbutton2':
		session.pop('gold', None)
		session.pop('activities', None)




	return redirect('/')


app.run(debug=True)