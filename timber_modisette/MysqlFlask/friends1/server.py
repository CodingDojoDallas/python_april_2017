import md5
from flask import Flask, render_template, session, redirect, request, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'assn1friends')



#root
@app.route('/')
def index():
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)

	return render_template('index.html', all_friends=friends)

#when i push button this happens and redirects to root
@app.route('/friends', methods=['POST'])
def createFriends():
	query = "INSERT INTO friends (name, age, created_at, updated_at) VALUES(:name, :age, NOW(), NOW())"
	data = {'name': request.form['name'], 'age': request.form['age']}


	
	mysql.query_db(query, data)

	return redirect('/')







app.run(debug=True)


