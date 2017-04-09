from flask import*

app=Flask(__name__)

app.secret_key ="itsasecret"


@app.route('/')
def index():
	if 'gold' not in session:
		session['gold'] = 0
	if 'activities' not in session:
		session['acitivities'] = []
	return rendered_template('index.html')

# @app.route('/play', methods=['POST'])
# def play():
# 	if request.form['location'] == 'farm':
# 		gold = random.randint(10,20)
# 	elif : request.form['locaiton'] == 'cave':
# 		gold = random.randint(10,20)

# 	elif : request.form['locaiton'] == 'house':
# 		gold = random.randint(10,20)
# 	else:
# 		gold = random.randint(-50,50)

# 	session['gold'] += gold

# 	messageObj={}

# 	if gold > 0:
# 		action = "Earned"
# 		messageObj['color'] = 'green'

# 	else:
# 		acition = "Lost"
# 		messageObj['color'] = 'red'


# 	message = "{} {} gold from the {}".format(action, abs(gold), request.form['locaiton'])
# 	measageOb['message'] = message


	
# 	session['activities'].insert(0,message)


# 	return redirect('/')


app.run(debug=True)