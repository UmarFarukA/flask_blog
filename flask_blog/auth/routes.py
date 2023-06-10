import os
import utils
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.utils import secure_filename
from auth.forms import RegistratioinForm, LoginForm
from auth.models import User
from posts.forms import UpdateForm
from flask_bcrypt import Bcrypt

auth = Blueprint('auth', __name__)
bcrypt = Bcrypt()

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """Route for registering users"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistratioinForm(request.form)
    if request.method == 'POST' and form.validate():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode("utf-8")
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        user.insert()
        flash(f'Thank you for registerig', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title="Register", form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        flash("Username/password is invalid", "danger")
    return render_template('login.html', title="Login", form=form)


@auth.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    """A route that renders the dashboard"""
    form = UpdateForm(request.form)
    if request.method == 'POST' and form.validate():
        if 'file' not in request.files:
            flash('No file part', "info")
            return redirect(url_for('dashboard'))

        file = request.files['file']

        if file.filename == '':
            flash('No selected file', "info")
            return redirect(url_for('dashboard'))

        if file and utils.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.root_path, 'static/images', filename))
            user = User.query.filter_by(id=current_user.id).first()
            user.email = form.email.data
            user.username = form.username.data
            user.image_path = filename
            user.update()
            flash("Updated successfuly", "success")
            return redirect(url_for('dashboard'))

    return render_template('dashboard.html', title='Dashboard', form=form, image=current_user.image_path)


@auth.route('/logout')
@login_required
def logout():
    """A route that logout a user"""
    logout_user()
    return redirect(url_for('index'))
