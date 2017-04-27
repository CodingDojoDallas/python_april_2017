
from flask import Flask, render_template,request,redirect

app = Flask(__name__) 

@app.route('/') 
def index():
	return render_template('index.html') 

@app.route('/result') 
def result():
	return render_template('result.html') 
 

@app.route('/result', methods=['POST']) 
def create_user():
	print "Got Post info"
	name = request.form['name'] #remember to put [] not () because it's tuple
	location = request.form['location']
	favorite_language = request.form['favorite_language']
	comment = request.form['comment']
	print name
	print location
	print favorite_language
	print comment

	data = {
		'name' : name,
		'location' : location,
		'favorite_language' : favorite_language,
		'comment' : comment,
	}
	return render_template('result.html', data=data)
	# return render_template('result.html', name=name, location=location,favorite_language=favorite_language,comment=comment)


#run our application in debug mode
app.run(debug=True)