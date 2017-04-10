from flask import *

app=Flask(__name__)

app.secret_key="whataday"

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/result', methods=['POST'])
def submit_info():
	print request.form
	session['name']=request.form['name']
	session['location']=request.form['location']
	session['language']=request.form['language']
	session['comment']=request.form['comment']
	#validations
	is_valid = True
	if session['name'] == '' :
		flash("Name cannot be empty!")
		is_valid = False
	if session['comment'] == '':
		is_valid = False
		flash("Comment cannot be empty!")


	if is_valid == True:
		return render_template('result.html')
	#only go to result page if we pass all validations	
	else:
		return redirect('/')
	print session['name']

	

@app.route('/reset')
def reset():
	return redirect('/')


app.run(debug=True)