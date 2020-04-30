from flask_wtf import FlaskForm  # klasa podstawowa FlaskForm pakietu Flask-WTF
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField  # klasy reprezentujące typy pól
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User


#  formularz logowania użytkownika, który prosi użytkownika o podanie nazwy użytkownika i hasła
class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember_me = BooleanField('Pamiętaj mnie')
    submit = SubmitField('Zaloguj')


#  formularz rejestracyjny
#  walidator Email() należy do wtforms. Waliduje czy email jest poprawnie wpisany
#  walidator EqualTo() należy do wtforms. Waliduje czy wpisana wartość odpowiada tej z argumentu
class RegistrationForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    password2 = PasswordField(
        'Powtórz Hasło', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Zarejestruj użytkownika')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Ta nazwa użytkownika jest już zajęta.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Ten email należy do kogoś innego.')


#  formularz edycji profilu użytkownika
class EditProfileForm(FlaskForm):
    username = StringField('Użytkownik', validators=[DataRequired()])
    about_me = TextAreaField('O mnie', validators=[Length(min=0, max=140)])
    submit = SubmitField('Zatwierdź')
