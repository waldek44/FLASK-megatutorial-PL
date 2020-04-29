from flask_wtf import FlaskForm  # klasa podstawowa FlaskForm pakietu Flask-WTF
from wtforms import StringField, PasswordField, BooleanField, SubmitField  # klasy reprezentujące typy pól
from wtforms.validators import DataRequired


#  formularz logowania użytkownika, który prosi użytkownika o podanie nazwy użytkownika i hasła
class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember_me = BooleanField('Pamiętaj mnie')
    submit = SubmitField('Zaloguj')
