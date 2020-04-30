from datetime import datetime

from flask import render_template, flash, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import redirect

from app import app, db
from app.forms import LoginForm, EditProfileForm, RegistrationForm  # importuję klasy formularzy z forms.py
from app.models import User


# WIDOK STRONY GŁÓWNEJ
@app.route('/')
@app.route('/index')
@login_required
def index():

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

    return render_template('index.html', title='Strona domowa', posts=posts)


# funkcja logowania użytkownika
@app.route('/login', methods=['GET', 'POST'])  # argument methods mówi, że funkcja widoku akceptuje żądania GET i POST
def login():
    # Zmienna current_user pochodzi z Flask-Login i może być użyta w dowolnym momencie podczas obsługi do
    # uzyskania obiektu użytkownika, który reprezentuje żądania klienta.
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # ładuję użytkownika z bazy danych - zwróci obiekt użytkownika, jeśli istnieje, lub None, jeśli nie.
        user = User.query.filter_by(username=form.username.data).first()

        # Jeśli nazwa użytkownika i hasło są poprawne, wywołuję funkcję login_user( ), która pochodzi z Flask-Login.
        if user is None or not user.check_password(form.password.data):
            flash('Nieprawidłowa nazwa użytkownika lub hasło')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        # po poprawnym zalogowaniu user przejdzie do strony którą atakował zanim przekierowało go na /login
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


# funkcja wylogowywania użytkownika
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# funkcja rejestrowania nowego użytkownika
@app.route('/register', methods=['GET', 'POST'])
def register():
    # upewniam się, że użytkownik, który wywołuje tę trasę, nie jest zalogowany.
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # ładuję formularz rejestrowania
    form = RegistrationForm()

    # Logika if validate_on_submit( ) tworzy nowego użytkownika o nazwie użytkownika, podany adres e-mail i hasło,
    # zapisuje je w bazie danych, a następnie przekierowuje do monitu logowania, aby użytkownik mógł się zalogować.
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# widok profilu użytkownika
@app.route('/user/<username>')
@login_required
def user(username):

    # próbuję załadować użytkownika z bazy danych przy użyciu zapytania według nazwy użytkownika.

    # first_or_404 () działa dokładnie tak samo jak first (), gdy pojawiają się wyniki,
    # ale w przypadku braku wyników automatycznie wysyła błąd 404 z powrotem do klienta.

    user = User.query.filter_by(username=username).first_or_404()

    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)


# funkcja pomocnicza do określenia ostatniej wizyty użytkownika na stronie
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


# funkcja widoku edycji profilu użytkownika
@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    # Jeśli funkcja validate_on_submit () zwraca wartość True, kopiuję dane z formularza do obiektu użytkownika,
    # a następnie zapisuję obiekt w bazie danych.
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Supcio! Twoje zmiany zostały zapisane.')
        return redirect(url_for('user', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)