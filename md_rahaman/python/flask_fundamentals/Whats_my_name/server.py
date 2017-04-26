
from flask import Flask, render_template,request,redirect

app = Flask(__name__) 

@app.route('/') 
def index():
	return render_template('index.html') 
 

@app.route('/process', methods=['POST']) 
def create_user():
	print "Got Post info"
	name = request.form['name'] #remember to put [] not () because it's tuple
	print name

	return redirect('/')


#run our application in debug mode
app.run(debug=True)