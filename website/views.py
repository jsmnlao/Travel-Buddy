from flask import Blueprint, render_template

# views.py are end points for the url to navigate around the webpage

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

@views.route('/create-plan')
def create_plan():
    return render_template("create-plan.html")

