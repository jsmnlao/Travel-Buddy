from . import db
from flask_login import UserMixin

# Represents database tables in TravelBuddy

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))

    trips = db.relationship('Trip', backref='user')             # list of all trips
    itineraries = db.relationship('Itinerary', backref='user')  # list of all itineraries
    flights = db.relationship('Flight', backref='user')         # list of all flights
    hotels = db.relationship('Hotel', backref='user')           # list of all hotels

class Trip(db.Model):
    trip_id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))           # each trip belongs to a user
    
    itinerary = db.relationship('Itinerary', backref='trip', uselist=False)  # one-to-one relationship  

class Itinerary(db.Model):
    itinerary_id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))   # each trip belongs to a user
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.trip_id'))
    activities = db.relationship('Activity', backref='itinerary', cascade="all, delete-orphan")    # many activities in itinerary

class Activity(db.Model):
    activity_id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(500))

    itinerary_id = db.Column(db.Integer, db.ForeignKey('itinerary.itinerary_id'))

class Booking(db.Model):
    booking_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.trip_id'))
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.flight_id'))
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.hotel_id'))

class Flight(db.Model):
   flight_id = db.Column(db.Integer, primary_key=True)
   departure_date = db.Column(db.Date, nullable=False)
   departure_time = db.Column(db.Time, nullable=False)
   destination = db.Column(db.String(200), nullable=False)

class Hotel(db.Model):
    hotel_id = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)