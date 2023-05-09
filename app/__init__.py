from flask import Flask

def Create_app():
    app = Flask(__name__)

    app.config['Secret Key'] = 'your-secret-key-here'

    from .routes.car import cars_bp
    app.register_blueprint(cars_bp)

    return app
