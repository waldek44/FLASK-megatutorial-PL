from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Zmienna __name__ przekazywana do klasy Flask jest predefiniowaną zmienną Python,
# która jest ustawiona na nazwę modułu, w którym jest używana.
app = Flask(__name__)

# odczytywanie pliku konfiguracyjnego - app.config.from_object(Config) to klasa Config z modułu config.py
app.config.from_object(Config)

# konfiguracja database
db = SQLAlchemy(app)  # obiekt reprezentujący bazę danych
migrate = Migrate(app, db)  # obiekt reprezentujący silnik migracji.

# flask_login zarządza stanem zalogowania użytkownika. Nazwa funkcji (lub punktu końcowego) dla widoku logowania.
# Innymi słowy, nazwa, której użyjesz w wywołaniu url_for(), aby uzyskać adres URL
login = LoginManager(app)

# określam jaka funkcja widoku obsługuje logowanie dla celów wymagania zalogowania Flask-Login
login.login_view = 'login'

# moduł routes jest importowany u dołu, a nie u góry skryptu, ponieważ zawsze jest wykonywany.
# Dolny import to obejście importu cyklicznego, który jest częstym problemem w aplikacjach Flask.
from app import routes, models
