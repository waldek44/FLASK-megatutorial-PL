from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


# funkcja ładująca użytkownika do sesji dla flask-login
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):  # klasa User dziedziczy po klasie db.Model, klasie bazowej dla wszystkich modeli
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, password):  # Metoda hashowania hasła
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):  # Metoda hashowania hasła
        return check_password_hash(self.password_hash, password)

    def __repr__(self):  # Metoda __repr__ mówi Pythonowi, jak drukować obiekty tej klasy
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # po to by pobierać posty  chronologicznie
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # klucz obcy dla user.id - odwołuje się do id klasy User

    def __repr__(self):
        return '<Post {}>'.format(self.body)