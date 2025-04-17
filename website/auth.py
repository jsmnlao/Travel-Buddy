from flask import Blueprint, render_template, request

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
        password = request.form.get('password_signup')

        # add user to database

    return render_template("signup.html")