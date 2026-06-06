from flask import Flask
from .config import Config
from .models import db
from .schemas import ma
from .routes import careers_bp, students_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    ma.init_app(app)
    app.register_blueprint(careers_bp)
    app.register_blueprint(students_bp)
    return app