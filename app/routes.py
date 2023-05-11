from flask import Blueprint, render_template, check_password_hash
from app import bs
from flask import form
import flash

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        
        flash('Invalid username/password combination')
        return redirect(url_for('login'))
    
    return render_template('login.html)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
