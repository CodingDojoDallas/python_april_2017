from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
	return render_template('result.html', form_data = request.form)

app.run(debug=True)