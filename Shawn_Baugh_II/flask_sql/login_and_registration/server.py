from flask import Flask, session, render_template, redirect, flash, request
from mysqlconnection import MySQLConnector
import md5, re, os, binascii

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "itsasecretdog"
mysql = MySQLConnector(app, 'users')
# ****************
# index route
@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_userss=users)
# ********************
# registration process
@app.route('/process', methods=['POST'])
def create_user():
    salt = binascii.b2a_hex(os.urandom(15))
    is_valid = True
    if len(request.form['first_name']) < 2 or           len(request.form['last_name']) < 2:
        is_valid == False
        flash('First and Last name must be longer then 2 characters')
        return redirect('/')
    elif not email_regex.match(request.form['email']):
        is_valid == False
        flash('please ender a valid email')
        return redirect('/')
    elif not len(request.form['password']) <= 8:
        is_valid == False
        flash('Please eneter a password longer then 8 characters')
        return redirect('/')
    elif request.form['password'] !=  request.form['password_confirmation']:
        is_valid == False
        return redirect('/')
        flash('Your passwords dont match. Match em dude.')
    if is_valid == False:
        return redirect('/')
        return redirect('/')
    else:
        flash('Success!')

        query = "insert into users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :salt, NOW(), NOW())"

        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': md5.new(request.form['password'] + salt).hexdigest(),
            'salt': salt
        }
        mysql.query_db(query, data)

        return render_template('success.html')
# **********************
# session settings
@app.route('/process')
def users():
    if 'user_id' not in session:
        return redirect('/')
    else:
        return render_template('success.html')
# *************
# login methods
@app.route('/login', methods=['POST'])
def login():
    query = 'select * from users where email = :email limit 1'
    data = {
        'email': request.form['email'],
    }
    user = mysql.query_db(query, data)

    if len(user) == 0:
        flash('Invalid email')
        return redirect('/')
    elif md5.new(request.form['password'] + user[0]['salt']).hexdigest() != user[0]['password']:
        flash('Wrong PW Bruh')
        return redirect('/')
    else:
        flash('Welcome!')
        session['user_id'] = user[0]['id']
        print session
        return render_template('success.html')
#  **********
# logout method
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
