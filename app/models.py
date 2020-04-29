from datetime import datetime
from app import db


class User(db.Model):  # klasa User dziedziczy po klasie db.Model, klasie bazowej dla wszystkich modeli
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):  # Metoda __repr__ mówi Pythonowi, jak drukować obiekty tej klasy
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # po to by pobierać posty  chronologicznie
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # klucz obcy dla user.id - odwołuje się do id klasy User

    def __repr__(self):
        return '<Post {}>'.format(self.body)