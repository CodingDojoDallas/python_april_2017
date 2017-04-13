from flask import Flask, render_template, redirect, request 
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'mydb')



@app.route('/')
def index():
    query = "SELECT * FROM fullfriends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

@app.route('/process', methods=['POST'])
def process():

    query = "INSERT INTO fullfriends (name, age, friend_since, created_at, updated_at) VALUES (:name, :age, :friend_since, NOW(), NOW())"

    data = {
             'name': request.form['name'],
             'age':  request.form['age'],
             'friend_since': request.form['friend_since']
           }
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
