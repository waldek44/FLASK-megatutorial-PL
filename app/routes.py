from flask import render_template, flash
from werkzeug.utils import redirect

from app import app
from app.forms import LoginForm  # importuję klasę LoginForm z forms.py


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


# funkcja logowania użytkownika
@app.route('/login', methods=['GET', 'POST'])  # argument methods mówi, że funkcja widoku akceptuje żądania GET i POST
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
