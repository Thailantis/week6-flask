from flask import Blueprint, render_template

cars_bp = Blueprint('cars', __name__, url_prefix='/car')


@cars_bp.route('/')
def index():
    cars = [
        {'make': 'Ford', 'model': 'Mustang', 'year': 2021},
        {'make': 'Toyota', 'model': 'Camry', 'year': 2022},
        {'make': 'Honda', 'model': 'Odyssey', 'year': 2020},
        {'make': 'BMW', 'model': 'M5', 'year': 2021},
        {'make': 'Nissan', 'model': 'Altima', 'year': 2022}
    ]
    return render_template('cars.html', cars=cars)
