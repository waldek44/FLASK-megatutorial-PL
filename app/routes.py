from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():

    # dodaję tymczasowego użytkownika, którego zamierzam zaimplementować jako słownik (dictionary)
    user = {'username': 'Waldemar'}

    # dodaję tymczasowe posty
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', title='Strona domowa', user=user, posts=posts)
