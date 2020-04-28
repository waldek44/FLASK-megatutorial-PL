from flask import Flask


# Zmienna __name__ przekazywana do klasy Flask jest predefiniowaną zmienną Python,
# która jest ustawiona na nazwę modułu, w którym jest używana.
app = Flask(__name__)

# moduł routes jest importowany u dołu, a nie u góry skryptu, ponieważ zawsze jest wykonywany.
# Dolny import to obejście importu cyklicznego, który jest częstym problemem w aplikacjach Flask.
from app import routes
