from flask import render_template, redirect, flash, request
from .forms import LoginForm
from .forms import CreateAccountForm
from .forms import NewFolderForm, NewNoteForm 
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

        user = Users.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            # Valid login
            login_user(user, remember=form.remember_me.data)
            print('True')
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
            u = Users(username=form.username.data, password=form.password.data, email=form.email.data)
            u.set_password(form.password.data)
            db.session.add(u)
            db.session.commit()
            return redirect('/home')
    else:
        if 'email' in form.errors:
            print('Invalid email format. Please enter a valid email address.')
        return render_template('create_account.html', form=form)

@myapp_obj.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home_blank.html')





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

#route for the split screen feature separately
    return render_template('create_note.html')  # Replace with the actual template name for creating a new note

@myapp_obj.route("/logout")
@login_required  # This decorator ensures that the user is logged in before logging out
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect('/')





@myapp_obj.route("/my-notes", methods=['GET', 'POST'])
def my_notes():
    form = NewFolderForm()

    #user_id = current_user.id if current_user.is_authenticated else None
    user_id = 1
    user_notes = Notes.query.filter_by(user_id=user_id).order_by(desc(Notes.modified_at)).all()
    user_folders = Folders.query.filter_by(user_id=user_id).order_by(asc(Folders.folder_name)).all()

    if form.validate_on_submit():
        folder_name = form.new_folder_name.data

        new_folder = Folders(folder_name=folder_name, user_id=user_id)
        db.session.add(new_folder)
        db.session.commit()

    return render_template('notes_directory.html', notes=user_notes, folders=user_folders, form=form)


@myapp_obj.route("/home-revamp", methods=['GET', 'POST'])
def homeRevamp():
    #user_id = current_user.id if current_user.is_authenticated else None
    user_id = 1
    user_notes = (
        db.session.query(
            #Notes.user_id,
            Notes.note_id,
            Notes.note_content,
            Notes.created_at,
            Notes.modified_at,
            Notes.folder_id
        )
        .filter_by(user_id=user_id)
        .order_by(desc(Notes.modified_at))
        .all()
    )   
    user_folders = (
        Folders.query.filter_by(user_id=user_id)
        .order_by(asc(Folders.folder_name))
        .all()
    )


    form1 = NewFolderForm()
    form2 = NewNoteForm()

    if form1.validate_on_submit():
        #user_id = current_user.id if current_user.is_authenticated else None ???
        folder_name = form1.new_folder_name.data
        new_folder = Folders(
            user_id=user_id,
            folder_name=folder_name)
        db.session.add(new_folder)
        db.session.commit()
        form1.processed = False
        return redirect(request.url)
        
    if form2.validate_on_submit():
        #user_id = current_user.id if current_user.is_authenticated else None
        #folder_id = ???
        new_note = Notes(
            user_id=user_id,
            note_content=form2.note_content.data,
            folder_id=form2.folder_id.data,
            created_at=form2.created_at.data,
            modified_at=form2.modified_at.data,
        )
        db.session.add(new_note)
        db.session.commit()
        #flash('Note created successfully', 'success')
        return redirect(request.url)

    return render_template('homepage.html', notes=user_notes, folders=user_folders, form1=form1, form2=form2)