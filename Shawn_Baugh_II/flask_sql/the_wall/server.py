from flask import Flask, session, render_template, redirect, flash, request
from mysqlconnection import MySQLConnector
import md5, re, os, binascii

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "ihaveasecret"
mysql = MySQLConnector(app, 'the_wall')
# ************
# index route
@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create_user():
    salt = binascii.b2a_hex(os.urandom(15))
    is_valid = True
    if len(request.form['first_name']) or len(request.form['last_name']) <= 2:
        is_valid == False
        flash('First or Last name must be 2 or more characters.')
        return redirect('/')
    elif not email_regex.match(request.form['email']):
        is_valid == False
        flash('Please a valid email address.')
        return redirect('/')
    elif not len(request.form['password']) <=8:
        is_valid == False
        flash('Please enter an email 8 characters or longer.')
        return redirect('/')
    if is_valid == False:
        return redirect('/')
    else:
        flash("Welcome {}")
        query = "insert into users (first_name, last_name, email, password, salt, created_at, updated_at) values (:first_name, :last_name, :email, :password, :salt, NOW(), NOW())"

        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': md5.new(request.form['password'] + salt).hexdigest(),
            'salt': salt
        }
        mysql.query_db(query, data)

        return render_template('wall.html')

@app.route('/process')
def users():
    if 'user_id' not in session:
        return redirect('/')
    else:
        return render_template('wall.html')
# ***************************
# login methods
@app.route('/login', methods=['POST'])
def login():
    query = 'select * from users where email = :email limit 1'
    data = {
        'email': request.form['email']
    }
    if len(user) == 0 or md5.new(request.form['password'] + user[0]['salt']).hexdigest() != user[0]['password']:
        flash('Invalid Email or Password')
        return redirect('/')
    else:
        flash('Welcome {}!')
        session['user_id'] = user[0]['id']
        return render_template('success.html')
# ******************
# logout method
@app.route('/logout')
def logout():
    seesion.clear()
    return redirect('/')


app.run(debug=True)
