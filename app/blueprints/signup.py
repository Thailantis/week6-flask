from flask import Blueprint, render_template, redirect, url_for

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
  return render_template('signup.html)
