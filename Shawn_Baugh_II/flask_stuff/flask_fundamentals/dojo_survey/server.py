from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users' ,methods=['POST'])
def create_user():
    print 'Got some info'
    data = {
        'name' : request.form['name'],
        'location' : request.form['location'],
        'language' : request.form['language'],
        'comments' : request.form['comments']
    }

    return render_template('survey_info.html', data = data)



app.run(debug=True)
