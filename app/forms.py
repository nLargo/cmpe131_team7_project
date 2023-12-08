from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.fields import DateTimeField
from datetime import datetime

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
    user_id = HiddenField('User ID', default=None)
    new_folder_name = StringField('New Folder Name', validators=[DataRequired()])
    submit = SubmitField('Create Folder')

class NewNoteForm(FlaskForm):
    user_id = HiddenField('User ID', default=None)
    default_note_content = 'New Note'
    note_id = HiddenField('Note ID', default=None)
    note_content = TextAreaField('Note Content', validators=[DataRequired()], default=default_note_content)
    folder_id = HiddenField('Folder ID', id='folder_id', default=None) 
    created_at = DateTimeField('Created At', default=datetime.utcnow)
    modified_at = DateTimeField('Modified At', default=datetime.utcnow)
