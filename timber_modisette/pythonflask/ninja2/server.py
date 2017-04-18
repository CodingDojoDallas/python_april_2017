from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = 'theendisnigh'

@app.route('/')
def index():

	

	return render_template('index.html')


@app.route('/ninjas/<color>')
def getinput(color):


	session['color'] = color

	print session['color']

	return render_template('/ninjas.html')
	


app.run(debug= True)