from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninjas')
def ninjas():
	return render_template('ninjas.html')

@app.route('/dojos')
def dojos():
	return render_template('dojos.html')

@app.route('/ninjausers', methods=['POST'])
def create_ninjauser():
	print "Got Post Info"
	name = request.form['name']
	pet = request.form['pet']
	#print request.form
	print request.form['name']
	print request.form['pet']
	# my_data = request.form 
	return redirect('/')





app.run(debug=True)