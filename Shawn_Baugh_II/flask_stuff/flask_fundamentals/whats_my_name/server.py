from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users',methods=['POST'])
def create_user():
    print 'Got Post Info'

    name = request.form['Name']

    return redirect('/')
app.run(debug=True)
