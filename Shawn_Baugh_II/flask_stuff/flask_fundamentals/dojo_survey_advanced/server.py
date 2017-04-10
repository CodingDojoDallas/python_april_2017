from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = 'SecretKeyBruh'

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
    is_valid = True
    if len(request.form['name']) < 1:
        is_valid = False
        flash("Name can't be empty bruh")

    if len(request.form['comments']) < 1 or len(request.form['comments']) > 120:
        flash("Please leave a comment or comment cant be more then 120 characters")
        is_valid = False
    if is_valid == False:
        return redirect('/')

    else:
        flash("Success! Welcome {}".format(request.form['name']))

        return render_template('survey_info.html', data = data)



app.run(debug=True)
