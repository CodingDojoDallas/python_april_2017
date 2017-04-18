from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/dojosurvey', methods=["POST"])
def dojosurvey():
	name = request.form['name']
	dallasLocation = request.form['DL']
	favouriteLang = request.form['FL']
	comment = request.form['ta']

	return render_template("result.html",name=name, DL=dallasLocation, FL=favouriteLang, textarea=comment)

app.run(debug=True)



	