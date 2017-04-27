
from flask import Flask, render_template 

app = Flask(__name__) 

@app.route('/') 
def index():
	return render_template('index.html') 

@app.route('/ninjas.html') 
def ninjas():
	return render_template('ninjas.html') 

@app.route('/dojo.html') 
def dojo():
	return render_template('dojo.html') 


#run our application in debug mode
app.run(debug=True)