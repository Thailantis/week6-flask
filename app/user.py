from flask_sqlalchemy import SQLAlchemy
from app import db
import os
import psycopg2

DATABASE_URL =os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Colum(db.Integer, primary_key=True)
  first_name = db.Column(db.String(50))
  last_name = db.Column(db.String(50))
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(100))

 
