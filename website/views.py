from flask import current_app, Blueprint, render_template, abort, request, redirect, jsonify
from flask_login import login_required, current_user
from .models import User, Trip, Flight, Activity, Hotel, Booking, Favorites
import sqlite3
from datetime import datetime
from flask import flash, url_for
from . import db
from dotenv import load_dotenv
import os
import requests

load_dotenv()

# views.py are end points for the url to navigate around the webpage

views = Blueprint('views', __name__)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

@views.route('/')
def landing():
    # print("API Key loaded:", os.getenv("OPENROUTER_API_KEY"))
    return render_template("landing.html")

@views.route('/home')
@login_required
def home():
    trips = Trip.query.filter_by(user_id=current_user.id).all()
    favorites = db.session.query(Trip).join(Favorites).filter(Favorites.user_id == current_user.id).all()
    return render_template("home.html", user=current_user, trips=trips, favorites=favorites)


@views.route('/plan/<int:trip_id>')
@login_required
def view_plan(trip_id):
    trip = Trip.query.get_or_404(trip_id)
    flight = Flight.query.filter_by(trip_id=trip_id).first() 
    hotel = Hotel.query.filter_by(trip_id=trip_id).first() 
    activities = Activity.query.filter_by(trip_id=trip_id).all()

    if trip.user_id != current_user.id:
        abort(403)

    return render_template("plan.html", user=current_user, trip=trip, flight=flight, hotel=hotel, activities=activities)

@views.route('/explore-plan/<int:trip_id>')
@login_required
def explore_plan(trip_id):
    trip = Trip.query.get_or_404(trip_id)
    flight = Flight.query.filter_by(trip_id=trip_id).first() 
    hotel = Hotel.query.filter_by(trip_id=trip_id).first() 
    activities = Activity.query.filter_by(trip_id=trip_id).all()

    if trip.user_id != current_user.id:
        abort(403)

    return render_template("explore-plan.html", user=current_user, trip=trip, flight=flight, hotel=hotel, activities=activities)

@views.route('/edit-plan/<int:trip_id>', methods=['GET'])
@login_required
def edit_plan(trip_id):
    trip = Trip.query.get_or_404(trip_id)
    flight = Flight.query.filter_by(trip_id=trip_id).first() 
    hotel = Hotel.query.filter_by(trip_id=trip_id).first() 
    activities = Activity.query.filter_by(trip_id=trip_id).all()

    if trip.user_id != current_user.id:
        abort(403)

    return render_template("edit-plan.html", user=current_user, trip=trip, flight=flight, hotel=hotel, activities=activities)


@views.route('/delete-plan/<int:trip_id>', methods=['POST'])
@login_required
def delete_plan(trip_id):
    trip = Trip.query.get_or_404(trip_id)

    if trip.user_id != current_user.id:
        abort(403)
        
    try:
        db.session.delete(trip)
        db.session.commit()
        flash('Your trip has deleted successfully!', 'success')
        return redirect(url_for('views.home'))
    except Exception as ex:
        flash('An occured while performing action,', 'danger')
        return redirect(url_for('views.home'))        
    
    
@views.route('/delete-activity/<int:activity_id>', methods=['POST'])
@login_required
def delete_activity(activity_id):
    activity = Activity.query.get(activity_id)
    
    try:
        if activity:
            trip_id= activity.trip_id
            db.session.delete(activity)
            db.session.commit()
            flash('Your activity has deleted successfully!', 'success')
            return redirect(url_for('views.edit_plan', trip_id=trip_id))

    except Exception as ex:
        flash('An occured while performing action,', 'danger')
        return redirect(url_for('views.edit_plan', trip_id=trip_id))
    
@views.route('/like-trip/<int:trip_id>', methods=['POST'])
@login_required
def like_trip(trip_id):
    trip = Trip.query.get_or_404(trip_id)
    if trip.user_id != current_user.id:
        abort(403)
    favorite = Favorites.query.filter_by(user_id=current_user.id, trip_id=trip_id).first()

    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        liked = False
    else:
        new_fav = Favorites(user_id=current_user.id, trip_id=trip_id)
        db.session.add(new_fav)
        db.session.commit()
        liked = True

    return jsonify({'liked': liked})
    
    
@views.route('/explore')
def explore():
    public_trips = Trip.query.filter_by(public=True).all()      # retrieve Public trips
    favorites = {fav.trip_id for fav in Favorites.query.filter_by(user_id=current_user.id).all()}
    return render_template("explore.html", user=current_user, trips=public_trips, favorites=favorites)

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
    public = True if request.form.get('public') else False

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
    
    values = [destination, start_date, end_date, travelers, budget, airline, flight_number, depart_date, depart_time, hotel_name, hotel_location]

    if any(value.strip() == '' for value in values):
        flash('Please fill in all required fields.')
        return redirect(request.referrer or url_for('create_plan'))
    
    activity_lists = [activity_names, activity_locations, activity_dates]
    for activity_list in activity_lists:
        if any(item.strip() == '' for item in activity_list):
            flash('Please fill in all required fields.')
            return redirect(request.referrer or url_for('create_plan'))

    # insert to db
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Create and insert Trip
        new_trip = Trip(
            destination=destination,
            start_date=datetime.strptime(start_date, '%Y-%m-%d').date(),
            end_date=datetime.strptime(end_date, '%Y-%m-%d').date(),
            travelers=int(travelers),
            budget=int(budget),
            public=public,
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
        db.session.rollback()
        print('Error saving plan: ', ex)
        
    print('about to flash message and return home')
    flash('Plan created successfully!', category='success')
    return redirect('/home')


@views.route('/update-plan', methods=['POST'])
def update_plan():    
    print('update plan is called')
    try:
        trip_id = request.form.get('trip_id')
        if not trip_id:
            print("trip_id not received in form!")
            raise Exception("Missing trip_id in form data")
        trip = Trip.query.get_or_404(trip_id)   
        
        if trip.user_id != current_user.id:
            abort(403)
        
        trip.destination = request.form['destination']
        trip.start_date = datetime.strptime(request.form['startDate'], '%Y-%m-%d').date()
        trip.end_date = datetime.strptime(request.form['endDate'], '%Y-%m-%d').date()
        trip.travelers = request.form['travelers']
        trip.budget = request.form['budget']
        trip.public = True if request.form.get('public') else False
  
        flight = Flight.query.filter_by(trip_id=trip_id).first() 
      
        if flight:
            flight.airline = request.form['airline']
            flight.flight_number = request.form['flight_number']
            flight.departure_date = datetime.strptime(request.form['depart_date'], '%Y-%m-%d').date()
            # flight.departure_time = datetime.strptime(request.form['depart_time'], '%H:%M').time()
            try:
                flight.departure_time = datetime.strptime(request.form['depart_time'], '%H:%M:%S').time()
            except ValueError:
                flight.departure_time = datetime.strptime(request.form['depart_time'], '%H:%M').time()

        
        hotel = Hotel.query.filter_by(trip_id=trip_id).first() 
        if hotel:
            hotel.hotel_name = request.form['hotel_name']
            hotel.location = request.form['hotel_location']
            
        activities = Activity.query.filter_by(trip_id=trip_id).all()
        activity_names = request.form.getlist('activity_name[]')
        activity_locations = request.form.getlist('activity_location[]') 
        activity_dates = activity_dates = [
            datetime.strptime(d, '%Y-%m-%d').date()
            for d in request.form.getlist('activity_date[]')]
        activity_descriptions = request.form.getlist('activity_description[]') 

        # update existing actvities
        if activities:
            for i in range(min(len(activities), len(activity_names))):
                activities[i].activity_name = activity_names[i]
                activities[i].location = activity_locations[i]
                activities[i].date = activity_dates[i]
                activities[i].description = activity_descriptions[i]
        
        # add any new activities
        for i in range(len(activities), len(activity_names)):
            new_activity = Activity(
                trip_id=trip_id,
                activity_name=activity_names[i],
                location=activity_locations[i],
                date=activity_dates[i],
                description=activity_descriptions[i]
            )
            db.session.add(new_activity)
            
        
        db.session.commit()
    
    except Exception as ex:
        db.session.rollback()
        print('Error saving plan: ', ex) 
    
    flash('Plan updated successfully!', category='success')
    return redirect('/home')


@views.route('/generate-itinerary', methods=['POST'])
def generate_itinerary():
    data = request.get_json()

    destination = data.get('destination')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    travelers = data.get('travelers')
    budget = data.get('budget')

    if not all([destination, start_date, end_date, travelers, budget]):
        return jsonify({ "error": "All fields are required." }), 400

    try:
        days = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days + 1
    except:
        return jsonify({ "error": "Invalid date format." }), 400

    prompt = f"""
        You are a professional travel planner and itinerary generator.

        Create a detailed {days}-day travel itinerary for a trip to {destination}.
        There will be {travelers} traveler(s), and the total budget for the trip is ${budget}. 
        The trip starts on {start_date} and ends on {end_date}. 
        Choose activities that match the weather and seasonal conditions during those dates.

        The response must be a **valid JSON array**. Do not include any commentary or formatting outside the array.

        Each item in the array should represent **one activity per day**, and contain the following fields:

        - "name": A short, engaging name for the activity  
        - "address": A specific location, neighborhood, or venue  
        - "date": A real date in YYYY-MM-DD format  
        - "description": A concise description (1–2 sentences) about the activity

        Keep each activity realistic and within the budget constraints. Vary activity types (e.g. sightseeing, dining, nature, culture, etc.).

        Example output format:
        [
            {{
            "name": "Visit Tokyo Tower",
            "address": "Minato City, Tokyo",
            "date": "2025-05-06",
            "description": "Enjoy panoramic views of the city from the iconic Tokyo Tower."
            }},
            ...
        ]
        """

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/llama-3-8b-instruct",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 800,
                "temperature": 0.7
            }
        )

        result = response.json()
        content = result["choices"][0]["message"]["content"]

        # Try to parse the returned string as JSON (the model outputs JSON-like text)
        import json
        activities = json.loads(content)

        return jsonify({ "activities": activities })

    except Exception as e:
        print("LLaMA API error:", e)
        return jsonify({ "error": "Failed to generate itinerary." }), 500
    

# Testing API endpoint
#@views.route('/test', methods=['POST'])
#def test():
#    print("Got a POST request!")
#    return jsonify({"message": "It works!"})
