from flask import Blueprint, render_template

cars_bp = Blueprint('cars', __name__)
manufacturers_bp = Blueprint('manufacturers', __name__)

@cars_bp.route('/')
def index():
    return render_template('cars/cars.html')

@manufacturers_bp.route('/')
def manu_index():
    return render_template('manufacturers'/'manufacturers.html')
