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

        user = User.query.filter_by(email=email).first()
        
        if user:
            if check_password_hash(user.password, password):
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("landing.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name_signup')
        email = request.form.get('email_signup')
        password1 = request.form.get('password1_signup')
        password2 = request.form.get('password2_signup')

        user = User.query.filter_by(email=email).first()

        # quality checks
        if user:
            flash('Email already in use.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(name) < 1:
            flash('Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('views.home'))

    return render_template("signup.html")