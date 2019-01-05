from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import Required
from flask_wtf import FlaskForm

class LoginForm(Form):
    username = TextField('login', validators = [Required()])
    submit = SubmitField('Sign In')

class AddPost(Form):
    posttext = TextField('text')
    posthead = TextField('Head')
    submit = SubmitField('send')
