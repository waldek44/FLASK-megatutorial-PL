from app import app, db
from app.models import User, Post


@app.shell_context_processor  # Dekorator rejestruje tę funkcję jako funkcję kontekstową powłoki
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
