from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def landing():
    return render_template("landing.html")

@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/plan')
def plan():
    return render_template("plan.html")

@views.route('/explore')
def explore():
    return render_template("explore.html")

@views.route('/signup')
def signup():
    return render_template("signup.html")