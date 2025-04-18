from . import db
from flask_login import UserMixin

# Represents database tables in Travel Buddy

class User(db.Model, UserMixin):
<<<<<<< HEAD
=======
    __tablename__ = 'user'
>>>>>>> 4dd3c699e31a393eb172b0719d5ef072c700fa07
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))

    #trips = db.relationship('Trip', backref='user')             # list of all trips
    #itineraries = db.relationship('Itinerary', backref='user')  # list of all itineraries
    #flights = db.relationship('Flight', backref='user')         # list of all flights
    #hotels = db.relationship('Hotel', backref='user')           # list of all hotels

class Trip(db.Model):
    __tablename__ = 'trip'
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))           # each trip belongs to a user
<<<<<<< HEAD
    
=======
    public = db.Column(db.Boolean, default=False, nullable=False)  # for sharing on explore page (False = private, True = public)
>>>>>>> 4dd3c699e31a393eb172b0719d5ef072c700fa07
    itinerary = db.relationship('Itinerary', backref='trip', uselist=False)  # one-to-one relationship  


class Itinerary(db.Model):
<<<<<<< HEAD
    itinerary_id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   # each trip belongs to a user
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.trip_id'))
=======
    __tablename__ = 'itinerary'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   # each trip belongs to a user
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'))
>>>>>>> 4dd3c699e31a393eb172b0719d5ef072c700fa07
    activities = db.relationship('Activity', backref='itinerary', cascade="all, delete-orphan")    # many activities in itinerary

class Activity(db.Model):
    __tablename__ = 'activity'
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(500))
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itinerary.id'))

class Booking(db.Model):
<<<<<<< HEAD
    booking_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.trip_id'))
=======
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'))
>>>>>>> 4dd3c699e31a393eb172b0719d5ef072c700fa07
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.flight_id'))
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.hotel_id'))


class Flight(db.Model):
<<<<<<< HEAD
   flight_id = db.Column(db.Integer, primary_key=True)
=======
   __tablename__ = 'flight'
   id = db.Column(db.Integer, primary_key=True)
>>>>>>> 4dd3c699e31a393eb172b0719d5ef072c700fa07
   departure_date = db.Column(db.Date, nullable=False)
   departure_time = db.Column(db.Time, nullable=False)
   destination = db.Column(db.String(200), nullable=False)

class Hotel(db.Model):
    __tablename__ = 'hotel'
    id = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
