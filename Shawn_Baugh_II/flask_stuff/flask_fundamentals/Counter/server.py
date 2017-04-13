from flask import *

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1

    return render_template('index.html')

@app.route('/button', methods=['POST'])
def button():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = -1
    return redirect('/')


app.run(debug=True)
