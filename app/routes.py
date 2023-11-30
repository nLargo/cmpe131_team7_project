from flask import render_template, redirect, flash, request
from .forms import LoginForm
from .forms import CreateAccountForm
from app import myapp_obj, db
from .models import Users, Notes, Folders    #Updated  
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import asc, desc

@myapp_obj.route("/", methods=['GET', 'POST'])
@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print("Form is valid and submitted")

        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            # Valid login
            login_user(user, remember=form.remember_me.data)
            print('True')
            flash(f'Login successful for user: {user.username}', 'success')
            return redirect('/home')  

        # Invalid login
        flash('Invalid username or password. Please try again.', 'error')

    return render_template('login.html', form=form)

@myapp_obj.route("/createaccount", methods=['GET', 'POST'])
def createaccount():
    form = CreateAccountForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
            print('do something')
            print(f'this is the username of the user {form.username.data}')
            print(f'this is the password of the user {form.password.data}')
            u = Users(username=form.username.data, password=form.password.data, email=form.email.data)
            db.session.add(u)
            db.session.commit()
            return redirect('/home')
    else:
        if 'email' in form.errors:
            print('Invalid email format. Please enter a valid email address.')
        return render_template('create_account.html', form=form)

@myapp_obj.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home_blank.html')


@myapp_obj.route('/create_note')
def create_note():
    return render_template('create_note.html')  # Replace with the actual template name for creating a new note

@myapp_obj.route("/logout")
@login_required  # This decorator ensures that the user is logged in before logging out
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect('/')


@myapp_obj.route("/my-notes", methods=['GET', 'POST'])
def my_notes():
    #user_id = current_user.id if current_user.is_authenticated else None
    user_id = 1
    user_notes = Notes.query.filter_by(user_id=user_id).order_by(desc(Notes.modified_at)).all()
    user_folders = Folders.query.filter_by(user_id=user_id).order_by(asc(Folders.folder_name)).all()

    return render_template('notes_directory.html', notes=user_notes, folders=user_folders)


