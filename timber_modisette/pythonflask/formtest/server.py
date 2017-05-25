from flask import Flask, render_template, request, redirect, session

app= Flask(__name__)

app.secret_key = "theendisnigh"
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
	print "Got Post Info"
	session['name'] = request.form['name']
	session['email'] = request.form['email']
	#print request.form
	#print request.form['email']
	#print request.form['name']
	#print request.form
	#my_data = request.form 
	return redirect('/show')
	#note that the typeof anything that comes in through request. form will be "STRING" no matter what
	#if you want that value to be indentified as an actual number you'll have to typpe cast it.

@app.route('/show')
def showUser():
	return render_template('user.html') #name=session['name'], email=session['email'])

app.run(debug=True)


