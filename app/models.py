from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    #def __init__(self, user_id):
    #    self.id = user_id

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<user {self.id}: {self.username}>'

    notes = db.relationship('Notes', backref='user', lazy=True)
    folders = db.relationship('Folders', backref='user', lazy=True)

    def get_id(self):
        return str(self.id)
    
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Notes(db.Model):
    note_id = db.Column(db.Integer, primary_key=True)
    note_content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    modified_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    folder_id = db.Column(db.Integer, db.ForeignKey('folders.folder_id', ondelete='CASCADE'), nullable=False)

class Folders(db.Model):
    folder_id = db.Column(db.Integer, primary_key=True)
    folder_name = db.Column(db.String(32), nullable=False, default='New Folder')

    parent_folder_id = db.Column(db.Integer, db.ForeignKey('folders.folder_id', ondelete='CASCADE'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    
