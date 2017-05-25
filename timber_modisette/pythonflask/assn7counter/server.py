from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "theendisnigh"

@app.route('/')
def index():
	
	if session.get('count') is None:
		session['count'] = 0
	print session.get('count')


	return render_template('index.html')


@app.route('/pushbutton', methods=["POST"])
def push_button():

	session['count'] += 2


	return redirect('/')


@app.route('/resetbutton', methods=["POST"])
def reset_button():

	#session['count'] = 1
	session.pop('count', None)

	return redirect('/')






app.run(debug=True)







