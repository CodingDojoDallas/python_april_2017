from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ImASecret"

@app.route('/')
def index():
	if 'counter' not in session:
		session['counter'] = 0
	else:
		session['counter'] += 1
	print session['counter']

	return render_template("index.html")

@app.route('/two', methods=['POST'])
def two():
	if 'counter' not in session:
		session['counter'] = 0
	else:
		session['counter'] += 1
	print session['counter']

	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['counter'] = -1

	return redirect('/')

app.run(debug = True)