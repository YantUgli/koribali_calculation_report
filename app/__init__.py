from flask import Flask
from flask_cors import CORS
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    # Register Blueprints

    # add the import here
    from app.calc_example.routes import calc_bp
    from app.opening_part.routes import opening_bp

    # add the blueprint here
    app.register_blueprint(calc_bp)
    app.register_blueprint(opening_bp)

    return app