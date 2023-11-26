from flask import render_template
from flask import redirect
from flask import flash
from .forms import LoginForm
from .forms import CreateAccountForm
from app import myapp_obj
from app.models import User
from app import db

@myapp_obj.route("/")
@myapp_obj.route("/hello", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f'Here we print to terminal the input {form.username.data} and {form.password.data}')
        flash(f'Here we use flash to HTML with the input {form.username.data} and {form.password.data}')
        found_user = User.query.filter_by(username=form.username.data).first()
        print(found_user)

        return redirect('/')
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
            return redirect('/')
    return render_template('create_account.html', form=form)




@myapp_obj.route("/home", methods=['GET', 'POST'])
def index():
    return render_template('home_blank.html')

@myapp_obj.route("/my-notes", methods=['GET', 'POST'])
def index():
    return render_template('notes_directory.html')