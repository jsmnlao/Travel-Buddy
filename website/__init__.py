from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY")

db = SQLAlchemy()
DB_NAME = "travelbuddy.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdfa asdfa'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    with app.app_context():
        if not path.exists('website/' + DB_NAME):
            db.create_all()
            print("Database created successfully")

    login_manager = LoginManager()
    login_manager.longin_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
