
from flask import Flask, render_template,request,redirect

app = Flask(__name__) 

@app.route('/') 
def index():
	return render_template('index.html')


@app.route('/ninja')
def ninja_defult():
	return render_template('ninja.html') 

@app.route('/ninja/<color>')
def ninja(color):
	color = color
	print color
	return render_template('ninja.html',color=color)

 
app.run(debug=True)