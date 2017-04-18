from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')



@app.route('/unknown')
def unknown():
	displayall = True
	return render_template('unknown.html', displayall=displayall)


@app.route('/unknown/<color>')
def getcolor(color):
	displayall = False
	color = color
	return render_template('unknown.html', color=color, displayall=displayall)





	



app.run(debug=True)