from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
# for password security
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

# auth.py handles the HTTP requests

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email_login')
        password = request.form.get('password_login')

        # validate email and password
        # if true, login user to account

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("initial_landing.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name_signup')
        email = request.form.get('email_signup')
        password1 = request.form.get('password1_signup')
        password2 = request.form.get('password2_signup')

        # quality checks
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        if len(name) < 1:
            flash('Name must be greater than 1 character.', category='error')
        if password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html")