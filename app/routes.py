from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Eugen'}
    posts = [
        {
            'author':{'username': 'Hans'},
            'body': 'Schön hier in Müllekoven!'
        },
        {
            'author':{'username': 'Susanne'},
            'body': 'Kann ich noch en Glas Wein?'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


