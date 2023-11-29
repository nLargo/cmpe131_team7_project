from flask import render_template, redirect, flash, request
from .forms import LoginForm
from .forms import CreateAccountForm
from app import myapp_obj, db
from app.models import User
from .models import User  # Assuming your models are in a file named models.py
from flask_login import login_user

@myapp_obj.route("/")

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user is not None and user.check_password(password):
            # Valid login
            login_user(user, remember=form.remember_me.data)
            flash(f'Login successful for user: {username}', 'success')
            return redirect('/home')  
        else:
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
            u = User(username=form.username.data, password=form.password.data, email=form.email.data)
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

@myapp_obj.route("/my-notes", methods=['GET', 'POST'])
def my_notes():
    return render_template('notes_directory.html')

@myapp_obj.route("/create_note", methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        if request.form.get('action') == 'split_screen':
            # Handle split-screen logic here if needed
            # You might want to pass any necessary data to the split_screen template
            return render_template('split_screen.html')

        elif request.form.get('action') == 'exit_split_screen':
            # Redirect to the create_note page
            return render_template('create_note.html')

    return render_template('create_note.html')#Replace with the actual template name for creating a new note

#route for the split screen feature separately
