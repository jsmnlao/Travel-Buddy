from flask import current_app, Blueprint, render_template, abort, request, redirect
from flask_login import login_required, current_user
from .models import User, Trip, Flight, Activity, Hotel, Itinerary, Booking
import sqlite3
from datetime import datetime
from flask import flash
from . import db

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
    conn = sqlite3.connect(current_app.config['DATABASE'])
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
        # Create and insert Trip
        new_trip = Trip(
            destination=destination,
            start_date=datetime.strptime(start_date, '%Y-%m-%d').date(),
            end_date=datetime.strptime(end_date, '%Y-%m-%d').date(),
            travelers=int(travelers),
            budget=int(budget),
            user_id=current_user.id  
        )
        db.session.add(new_trip)
        db.session.flush()  

        # Create and insert Flight
        new_flight = Flight(
            airline=airline,
            flight_number=int(flight_number),
            departure_date=datetime.strptime(depart_date, '%Y-%m-%d').date(),
            departure_time=datetime.strptime(depart_time, '%H:%M').time(),
            trip_id=new_trip.id
        )
        db.session.add(new_flight)
        db.session.flush()  

        # Create and insert Hotel
        new_hotel = Hotel(
            hotel_name=hotel_name,
            location=hotel_location,
            trip_id=new_trip.id
        )
        db.session.add(new_hotel)
        db.session.flush()

        # Create and insert Activities
        print("Activities:", activity_names, activity_locations, activity_dates, activity_descriptions)

        for name, location, date, description in zip(activity_names, activity_locations, activity_dates, activity_descriptions):
            new_activity = Activity(
                activity_name=name,
                location=location,
                date=datetime.strptime(date, '%Y-%m-%d').date(),
                description=description,
                trip_id=new_trip.id
            )
            db.session.add(new_activity)

        new_booking = Booking(
            user_id=current_user.id,
            trip_id=new_trip.id,
            flight_id=new_flight.id,
            hotel_id=new_hotel.id
        )
        db.session.add(new_booking)
    
        db.session.commit()

    except Exception as ex:
        print('in except')
        db.session.rollback()
        print('Error saving plan: ', ex)

    finally:
        print('in finally')

        
    print('about to flash message and return home')
    flash('Plan created successfully!', category='success')
    return redirect('/home')
