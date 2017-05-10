from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
	# friends = mysql.query_db("SELECT * FROM friends")
	# print friends

	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)
	return render_template('index.html', all_friends=friends)
@app.route('/friends/<friend_id>')
def show():
    # add a friend to the database!
	query = "SELECT * FROM friends WHERE id = :specific_id"
	data = {'specific_id': friend_id}
	friends = mysql.query_db(query, data)
	return render_template('index.html', one_friend=friends[0])

@app.route('/friends', methods=['POST'])
def create():
	# print request.form['first_name']
	# print request.form['last_name']
	# print request.form['occupation']
	# add a friend to the database!
	query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
	data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    # Run query, with dictionary values injected into the query.
	mysql.query_db(query, data)

	return redirect('/')
app.run(debug=True)