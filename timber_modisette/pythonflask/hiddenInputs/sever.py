from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def hidden():
	return render_template('hidden.html', methods="POST")



app.run(debug=True)