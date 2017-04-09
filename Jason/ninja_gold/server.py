from flask import*
import random

app=Flask(__name__)

app.secret_key ="itsasecret"


@app.route('/')
def index():
	if 'gold' not in session:
		session['gold'] = 0
	if 'activities' not in session:
		session['activities'] = []
	return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
	if request.form['location'] == 'farm':
		gold = random.randint(10,20)
	elif request.form['location'] == 'cave':
		gold = random.randint(10,20)
	elif request.form['location'] == 'house':
		gold = random.randint(10,20)
	else:
		gold = random.randint(-50,50)

	session['gold'] += gold

	messageObj={}

	if gold > 0:
		action = "Earned"
		messageObj['color'] = 'green'

	else:
		action = "Lost"
		messageObj['color'] = 'red'

	### message two attributes
	message = "{} {} gold from the {}".format(action, abs(gold), request.form['location'])
	messageObj['message'] = message
	session['activities'].insert(0,messageObj)


	return redirect('/')

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')


app.run(debug=True)