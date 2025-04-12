from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# the home page should be /home after user authentication is implemented
# the initial_landing page route would be '/' instead
# this is temporary for now
@views.route('/')
def home():
    return render_template("home.html")

# @views.route('/home')
# def home():
#     return render_template("home.html")

@views.route('/plan')
def plan():
    return render_template("plan.html")

@views.route('/explore')
def explore():
    return render_template("explore.html")