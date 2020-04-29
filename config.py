import os


# Ustawienia konfiguracyjne są zdefiniowane jako zmienne klasy wewnątrz klasy Config.
# Jeśli okaże się, że muszę mieć więcej niż jeden zestaw konfiguracyjny, mogę utworzyć jej podklasy.
class Config(object):
    # Zmienna konfiguracyjna SECRET_KEY tworzy klucz kryptograficzny
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
