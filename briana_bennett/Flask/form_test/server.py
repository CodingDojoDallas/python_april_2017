from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ImASecret"

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
	print "got post info"
	print request.form

	session['name'] = request.form['name']
	session['email'] = request.form['email']
	# redirects back to the '/' route
	return redirect('/show')

@app.route('/show')
def show_user():
  return render_template('users.html')
	
app.run(debug=True) # run our server