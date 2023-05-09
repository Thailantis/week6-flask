from flask import Blueprint, render_template

cars_bp = Blueprint('cars', __name__)

@cars_bp.route('/')
def index():
    return render_template('cars/cars.html')

@cars_bp.route('/list')
def list_cars():
    cars = ['Nissan', 'Toyota', 'Honda', 'Ford']
    return render_template('cars/list.html', cars=cars)

@cars_bp.route('/<string:car_name>')
def car_details(car_name):
    return f"This is the details page for {car_name}"
