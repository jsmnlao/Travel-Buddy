from flask import Blueprint, render_template, abort, request, redirect
from flask_login import login_required, current_user
from .models import Trip
import sqlite3
from flask import flash

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

def get_db_connection():
    conn = sqlite3.connect('instance/travelbuddy.db')
    conn.row_factory = sqlite3.Row
    return conn

@views.route('/save-plan', methods=['POST'])
def save_plan():
    destination = request.form['destination']
    start_date = request.form['startDate']
    end_date = request.form['endDate']
    travelers = request.form['travelers']
    budget = request.form['budget']

    airline = request.form['airline']
    flight_number = request.form['flight_number']
    depart_date = request.form['depart_date']
    depart_time = request.form['depart_time']
    
    hotel_name = request.form['hotel_name']
    hotel_location = request.form['hotel_location']
    
    activity_names = request.form.getlist('activity_name[]')
    activity_locations = request.form.getlist('activity_location[]') 
    activity_dates = request.form.getlist('activity_date[]') 
    activity_descriptions = request.form.getlist('activity_description[]') 

    # insert to db
    conn = get_db_connection()
    cursor = conn.cursor()
    print('before try block')
    try:
        print('in try block to insert queries')
        insert_trip_query = """
            INSERT INTO trip (
            destination, start_date, end_date, travelers, budget)
            VALUES (?, ?, ?, ?, ?)"""
        conn.execute(insert_trip_query, (destination, start_date, end_date, travelers, budget))
        trip_id = cursor.lastrowid

        insert_flight_query = """
            INSERT INTO flight (airline, flight_number, departure_date, departure_time, trip_id)
            VALUES (?, ?, ?, ?, ?)"""
        conn.execute(insert_flight_query, (airline, flight_number, depart_date, depart_time, trip_id))

        insert_hotel_query = """
            INSERT INTO hotel (hotel_name, location, trip_id)
            VALUES (?, ?, ?)"""
        conn.execute(insert_hotel_query, (hotel_name, hotel_location, trip_id))

        insert_activities_query = """
            INSERT INTO activity (name, location, date, description, trip_id)
            VALUES (?, ?, ?, ?, ?)"""
        for name, location, date, description in zip(activity_names, activity_locations, activity_dates, activity_descriptions):
            conn.execute(insert_activities_query, (name, location, date, description, trip_id))

    except Exception as ex:
        print('in except')
        conn.rollback()
        print('Error saving plan: ', ex)

    finally:
        print('in finally')
        conn.commit()
        conn.close()
        
    print('about to flash message and return home')
    flash('Plan created successfully!', category='success')
    return redirect('/home')
