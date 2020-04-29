import os
basedir = os.path.abspath(os.path.dirname(__file__))


# Ustawienia konfiguracyjne są zdefiniowane jako zmienne klasy wewnątrz klasy Config.
# Jeśli okaże się, że muszę mieć więcej niż jeden zestaw konfiguracyjny, mogę utworzyć jej podklasy.
class Config(object):
    # Zmienna konfiguracyjna SECRET_KEY tworzy klucz kryptograficzny
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # ustalam lokalizację bazy danych aplikacji ze zmiennej konfiguracyjnej SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
