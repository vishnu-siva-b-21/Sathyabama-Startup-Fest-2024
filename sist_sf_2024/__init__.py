from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    # Importing all blueprints
    from sist_sf_2024.modules.admin import admin
    from sist_sf_2024.modules.user import user

    # Register all blueprints, setting their URL prefix
    app.register_blueprint(admin, url_prefix="/admin")
    app.register_blueprint(user, url_prefix="/")

    return app
