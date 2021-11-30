from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from app import app

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# Song Class/Model
class Song(db.Model):
  __tablename__ = 'song'
  id = db.Column(db.Integer, primary_key=True)
  #path = db.Column(db.String(300), unique=True)
  path = db.Column(db.String(300))
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

# Initialize Song Schema 
Song_schema = SongSchema()
Songs_schema = SongSchema(many=True)

# Initialize User Schema 
User_schema = UserSchema()
Users_schema = UserSchema(many=True)

# Initialize UserSong Schema 
UserSong_schema = UserSongSchema()
UserSongs_schema = UserSongSchema(many=True)
