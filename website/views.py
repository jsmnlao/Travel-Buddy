from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from .models import Trip

# views.py are end points for the url to navigate around the webpage

views = Blueprint('views', __name__)

@views.route('/')
def landing():
    return render_template("landing.html")

@views.route('/home')
@login_required
def home():
    trips = Trip.query.filter_by(user_id=current_user.id).all()
    return render_template("home.html", user=current_user, trips=trips)


@views.route('/plan/<int:trip_id>')
@login_required
def view_plan(trip_id):
    trip = Trip.query.get_or_404(trip_id)

    if trip.user_id != current_user.id:
        abort(403)

    return render_template("plan.html", user=current_user, trip=trip)


@views.route('/edit-plan/<int:trip_id>')
@login_required
def edit_plan(trip_id):
    trip = Trip.query.get_or_404(trip_id)

    if trip.user_id != current_user.id:
        abort(403)

    return render_template("plan.html", user=current_user, trip=trip)


@views.route('/explore')
def explore():
    return render_template("explore.html", user=current_user)

@views.route('/signup')
def signup():
    return render_template("signup.html")

@views.route('/create-plan')
@login_required
def create_plan():
    return render_template("create-plan.html", user=current_user)

# @views.route('save-plan', methods=['POST'])
# def save_plan():

