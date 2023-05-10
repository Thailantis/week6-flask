from flask import Flask
from flask_sqlaclehmy import SQLAlchemy
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    app.config['Secret Key'] = 'your-secret-key-here'

    from .routes.car import cars_bp
    from .routes.brand import brand_bp
    app.register_blueprint(cars_bp)
    app.register_blueprint(brand_bp)

    return app
