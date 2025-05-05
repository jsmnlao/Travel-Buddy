from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager
from llama_cpp import Llama

db = SQLAlchemy()
DB_NAME = "travelbuddy.db"

llm = None

def create_app():
    global llm
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdfa asdfa'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['DATABASE'] = os.path.join(app.instance_path, DB_NAME)
    db.init_app(app)

    llm = Llama(model_path="./model.gguf", n_ctx=512)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    with app.app_context():
        if not path.exists(DB_NAME):
            db.create_all()
            print("Database created successfully")

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
