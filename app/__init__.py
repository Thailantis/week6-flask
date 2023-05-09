from flask import Flask

def Create_app():
    app = Flask(__name__)

    app.config['Secret Key'] = 'your-secret-key-here'

    from app.cars.routes import cars_bp
    app.register_blueprint(cars_bp)

    from app.manufacturers.routes import manufacturers_bp
    app.register_blueprint(manufacturers_bp)

    return app
