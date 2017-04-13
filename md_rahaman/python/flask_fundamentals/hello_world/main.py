
from flask import Flask, render_template #import flask to allow us to create our app

app = Flask(__name__) #Global varibale __name__ tells Flask whether or not we are running the file

@app.route('/') 
def hello_world():
	return render_template('index.html') #render the html and reutrn it


#run our application in debug mode
app.run(debug=True)