from flask import Blueprint, render_template

brand_bp = Blueprint('brand', __name__, url_prefix='/brand')

@brand_bp.route('/')
def index():
  brands = ['Ford', 'Toyota', 'Honda', 'BMW', 'Nissan']
  return render_template('brand_index.html', brands=brands)
