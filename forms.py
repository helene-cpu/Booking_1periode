from flask_wtf import FlaskForm
from flask_wtf import StringField, PasswordField, Submitfield
from wtforms.validators import inputrequired

class RegisterForm(FlaskForm):
    name = StringField("Navn", validators=[InputRequired()])
    username = StringField("Brukernavn", validators=[Inputrequired()])
    classname = StringField("Klasse", validators=[Inputrequred()])
    password = PasswordField("Passord", validators=[InputRequired()])
    submit = SubmitField("Registrer")

class LoginForm(FlaskForm):
    username = StringField("Brukernavn", validators=[InputRequired()])
    password = StringField("Passord", validators=[InputRequired()])
    submit = SubmitField("Logg inn")