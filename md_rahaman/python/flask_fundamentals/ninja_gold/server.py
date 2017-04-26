
from flask import Flask,render_template,session,request,redirect,jsonify
import os
from random import randint
import datetime

app = Flask(__name__) 
app.secret_key = os.urandom(24) #generating randon sting 
# now = datetime.datetime.now()

@app.route('/')
def index():
	if 'gold' not in session:
		session['gold'] = 0
		session['money'] = []
		session['activities'] = []

	return render_template('index.html')


@app.route('/process',methods = ['POST'])
def process():
	now = datetime.datetime.now()

	if request.form['action'] == 'farm':   #name has to be action for all
		rand = randint(10,20)
		session['money'] = rand
		message = "Earned {} golds from {} {}".format(session['money'],'farm', now)
		session['activities'].append({'color': 'green', 'message':message})
		session['gold'] = session['gold'] + rand

	elif request.form['action'] == 'cave':
		rand = randint(5,10)
		session['money'] = rand
		message = "Earned {} golds from {} {}".format(session['money'],'cave', now)
		session['activities'].append({'color': 'green', 'message': message})
		session['gold'] = session['gold'] + rand

	elif request.form['action'] == 'house':
		rand = randint(2,5)
		session['money'] = rand
		message = "Earned {} golds from {} {}".format(session['money'],'house', now)
		session['activities'].append({'color': 'green', 'message': message})
		session['gold'] = session['gold'] + rand

	else:
		rand = randint(-50,50)
		session['money'] = rand
		if rand > 0:
			message = "Earned {} golds from {} {}".format(session['money'],'casino', now)
			session['activities'].append({'color': 'green', 'message': message})

		else:
			message = "Entered a casino and lost {} golds...Ouch".format(session['money'], now)
			# session['activities'].append({'color': 'red' 'message': '"Entered a {} and lost {} golds...ouch".format('casino',session['money'])'})
			session['activities'].append({'color': 'red','message': message})
		session['gold'] = session['gold'] + rand

	return redirect('/')

@app.route('/reset',methods = ['POST'])
def reset():
	session.pop('gold',None)
	return redirect('/')


#make sure always put debug mode for working 
app.run(debug=True)