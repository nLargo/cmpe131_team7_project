from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class CreateAccountForm(FlaskForm):
    name = StringField('Full name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm  = PasswordField('Repeat Password',validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Create Account')

class NewFolderForm(FlaskForm):
    new_folder_name = StringField('New Folder Name', validators=[DataRequired()])
    submit = SubmitField('Create Folder')