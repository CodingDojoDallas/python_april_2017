from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	print request.method
	return render_template('index.html')

@app.route('/football')
def football():
	return redirect('/')

app.run(debug=True)
