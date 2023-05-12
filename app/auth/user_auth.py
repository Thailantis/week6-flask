from flask import jsonify
from app import check_password_hash

@app.route('/signup', methods=["POST"])
def signup():
  username = request.json['username']
  password = request.json['password]

  user = User(username=username, password=password)
  db.session.add(user)
  db.session.commit()
                          
  return jsonify({'message': 'User account created successfully'})
                          
@app.route('/login', methods=['POST'])
def login():
  username = request.json['username']
  password = request.json['password]
                          
  user = User.query.filter_by(username=username)
                          
  if user and check_password_hash(user.password, password):
      return jsonify({'message': 'User account logged in successfully'})     
  else:
      return jsonify({'message': 'Invalid username or password'})
                          
@app.route('logout', methods=['POST'])
def logout():
  return jsonify({'message': 'Logged out successfully'})                          