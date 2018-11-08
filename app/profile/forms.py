from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from .models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')


class LoginForm(Form):
    username = TextField('login', validators = [Required()])
    password = TextField('password', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
    submit = SubmitField('Sign In')
