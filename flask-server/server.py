from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import session 
from werkzeug.security import check_password_hash, generate_password_hash
import os
import glob

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Song Class/Model
class Song(db.Model):
  __tablename__ = 'song'
  id = db.Column(db.Integer, primary_key=True)
  path = db.Column(db.String(300), unique=True)
  steps = db.Column(db.Integer)

  def __init__(self, path, steps):
    self.path = path
    self.steps = steps

# Song Schema
class SongSchema(ma.SQLAlchemySchema):
  class Meta:
    fields = ('id', 'path', 'steps')

# User Class/Model
class User(db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key=True)
  user_name = db.Column(db.String(16), unique=True)
  hash_password = db.Column(db.Integer)
  email = db.Column(db.String(80), unique=True)

  def __init__(self, user_name, hash_password, email):
    self.user_name = user_name
    self.hash_password = hash_password
    self.email = email

# User Schema
class UserSchema(ma.SQLAlchemySchema):
  class Meta:
    fields = ('id', 'user_name', 'hash_password', 'email')

# UserSong Class/Model
class UserSong(db.Model):
  __tablename__ = 'usersong'
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
  song_id = db.Column(db.Integer, db.ForeignKey("song.id"))
  rating = db.Column(db.Integer)

  def __init__(self, user_id, song_id, rating):
    self.user_id = user_id
    self.song_id = song_id
    self.rating = rating

# UserSong Schema 
class UserSongSchema(ma.SQLAlchemySchema):
  class Meta:
    fields = ('id', 'user_id', 'song_id', 'rating')

# Init schema
Song_schema = SongSchema()
Songs_schema = SongSchema(many=True)

User_schema = UserSchema()
Users_schema = UserSchema(many=True)

UserSong_schema = UserSongSchema()
UserSongs_schema = UserSongSchema(many=True)

# Register User
@app.route('/register', methods=['GET', 'POST'])
def register():
  user_name = request.json['user_name']
  email = request.json['email']
  password = request.json['password']
  user_name_exists = db.session.query(User.id).filter_by(user_name=user_name).first() is not None
  email_exists = db.session.query(User.id).filter_by(email=email).first() is not None
  if user_name_exists or email_exists:
    return jsonify({'user_added': False})
  hash_password = generate_password_hash(password)
  new_user = User(user_name, hash_password, email)
  db.session.add(new_user)
  db.session.commit()
  return jsonify({'user_added': True})

# Sign In
@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
  user_name_entered = request.json['user_name']
  password_entered = request.json['password']
  user = db.session.query(User).filter(User.user_name==user_name_entered).first()
  if user is not None and check_password_hash(user.hash_password, password_entered):
    return jsonify({'signed_in': True})
  return jsonify({'signed_in': False})

# Create a Song
@app.route('/song', methods=['POST'])
def add_Song():
  steps = request.json['steps']
  os.system("melody_rnn_generate \
    --config=basic_rnn \
    --bundle_file="+basedir+"/basic_rnn.mag \
    --output_dir="+basedir+"/assets \
    --num_outputs=1 \
    --num_steps="+str(steps)+" \
    --primer_melody=[60]")
  folder_path = basedir+"/assets"
  file_type = '/*mid'
  files = glob.glob(folder_path + file_type)
  max_file = max(files, key=os.path.getctime)
  path = max_file
  new_Song = Song(path, steps)
  db.session.add(new_Song)
  db.session.commit()
  return Song_schema.jsonify(new_Song)

# Get All Songs
@app.route('/song', methods=['GET'])
def get_Songs():
  all_Songs = Song.query.all()
  result = Songs_schema.dump(all_Songs)
  return jsonify(result)

# Get Single Songs
@app.route('/song/<id>', methods=['GET'])
def get_Song(id):
  song = Song.query.get(id)
  return Song_schema.jsonify(song)

# Update a Song
@app.route('/song/<id>', methods=['PUT'])
def update_Song(id):
  song = Song.query.get(id)
  path = request.json['path']
  steps = request.json['steps']
  Song.path = path
  Song.steps = steps
  db.session.commit()
  return Song_schema.jsonify(song)

# Delete Song
@app.route('/song/<id>', methods=['DELETE'])
def delete_Song(id):
  song = Song.query.get(id)
  if os.path.exists(song.path):
    os.remove(song.path)
  db.session.delete(song)
  db.session.commit()
  return Song_schema.jsonify(song)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)