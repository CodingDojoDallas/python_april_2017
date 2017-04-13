from flask import Flask, session, request, redirect, render_template
app = Flask(__name__)
app.secret_key = "secretsSecretsAreNOfunUnlesstheyreFUN4everyone"
import random


@app.route('/', methods=['GET'])
def index():

	if 'gold' not in session:
		session['gold'] = 0

	return render_template('index.html')
	
app.run(debug = True)