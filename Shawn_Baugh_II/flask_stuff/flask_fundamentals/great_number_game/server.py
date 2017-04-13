from flask import Flask, redirect, request, render_template, session
import random

app = Flask (__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():

    if 'head' not in session:
        session['head'] = random.randrange(0, 101)

    if 'red' not in session:
        session['red'] = 'red'

    print session['head']
    return render_template('index.html', red = session["red"])

@app.route('/guess', methods=['POST'])
def submit():

    num = int(request.form['guess'])
    head = session['head']
    print num
    if num < head:
        session["red"] = "That's low bruh"

    elif num > head:
        session["red"] = "That's high bruh"

    else:
        session["red"] = "Peeeerrrfect"



    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()

    return redirect('/')

app.run(debug=True)
