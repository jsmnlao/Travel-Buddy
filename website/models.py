from . import db
from flask_login import UserMixin

# Represents database tables in Travel Buddy

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))

class Trip(db.Model):
    __tablename__ = 'trip'
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    travelers = db.Column(db.Integer)
    budget = db.Column(db.Integer)
    public = db.Column(db.Boolean, default=False)  # for sharing on explore page (False = private, True = public)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))           # each trip belongs to a user
    flights = db.relationship('Flight', backref='trip', cascade="all, delete-orphan")
    hotels = db.relationship('Hotel', backref='trip', cascade="all, delete-orphan")
    activities = db.relationship('Activity', backref='trip', cascade="all, delete-orphan")
    bookings = db.relationship('Booking', backref='trip', cascade="all, delete-orphan")
    # itinerary = db.relationship('Itinerary', backref='trip', uselist=False)  # one-to-one relationship  

class Activity(db.Model):
    __tablename__ = 'activity'
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(500))
    
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id', ondelete="CASCADE"))
    # itinerary_id = db.Column(db.Integer, db.ForeignKey('itinerary.id', ondelete="CASCADE"))

class Flight(db.Model):
   __tablename__ = 'flight'
   id = db.Column(db.Integer, primary_key=True)
   airline = db.Column(db.String(200))
   flight_number = db.Column(db.Integer, nullable=False)
   departure_date = db.Column(db.Date, nullable=False)
   departure_time = db.Column(db.Time, nullable=False)

   trip_id = db.Column(db.Integer, db.ForeignKey('trip.id', ondelete="CASCADE"))

class Hotel(db.Model):
    __tablename__ = 'hotel'
    id = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)

    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id', ondelete="CASCADE"))

class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"))
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id', ondelete="CASCADE"))
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id', ondelete="CASCADE"))
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id', ondelete="CASCADE"))
    
# class Itinerary(db.Model):
#     __tablename__ = 'itinerary'
#     id = db.Column(db.Integer, primary_key=True)
    
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   # each trip belongs to a user
#     trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'))
#     activities = db.relationship('Activity', backref='itinerary', cascade="all, delete-orphan")    # many activities in itinerary