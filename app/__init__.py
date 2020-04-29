from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Zmienna __name__ przekazywana do klasy Flask jest predefiniowaną zmienną Python,
# która jest ustawiona na nazwę modułu, w którym jest używana.
app = Flask(__name__)

# odczytywanie pliku konfiguracyjnego - app.config.from_object(Config) to klasa Config z modułu config.py
app.config.from_object(Config)

# konfiguracja database
db = SQLAlchemy(app)  # obiekt reprezentujący bazę danych
migrate = Migrate(app, db)  # obiekt reprezentujący silnik migracji.


# moduł routes jest importowany u dołu, a nie u góry skryptu, ponieważ zawsze jest wykonywany.
# Dolny import to obejście importu cyklicznego, który jest częstym problemem w aplikacjach Flask.
from app import routes, models
