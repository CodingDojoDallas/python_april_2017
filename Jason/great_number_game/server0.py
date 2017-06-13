from flask import *
import random

app=Flask(__name__)

### Case 1: using a global variable for setting the random.randint number
# # seed_number=1
# great_num=random.randint(1,100)
# print great_num

# @app.route('/')
# def index():
# 	print great_num
# 	return render_template('index.html')

# @app.route('/submit')
# def submit():
# 	num = request.form[number]
# 	if num > great_num:
# 		session['status'] = "above"
# 	elif num < great_num:
# 		session['status'] = "below"
# 	else:
# 		session['status'] = "on the money"
# 		# seed_number+=1
# 		great_num=randint(1,100)

# 	return redirect('/',status=status)



### Case 2:using session for setting random number and assigning input numbers.

app.secret_key ='thisissecret'

@app.route('/')
def index():
	if 'randomint' not in session:
		session['randomint']=random.randint(1,100)
	print session['randomint']
	print type(session['randomint'])
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	session['number'] = request.form['number']
	print type(session['number'])
	print session['number']
	if session['number'] > session['randomint']:
		session['status'] = "above"
	elif session['number'] < session['randomint']:
		session['number'] = "below"
	else:
		session['status'] = "on the money"
	print session['status']
	return redirect('/')

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)