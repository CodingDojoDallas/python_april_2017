from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/yourname', methods=["POST"])
def yourname():
	name = request.form['name']

	print request.form
	print request.form['name']

	return redirect('/')

app.run(debug=True)