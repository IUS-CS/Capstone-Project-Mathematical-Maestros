from app import db, ma

# Song Class/Model
class Song(db.Model):
  __tablename__ = 'song'
  id = db.Column(db.Integer, primary_key=True)
  midi_path = db.Column(db.String(300), unique=True)
  wav_path = db.Column(db.String(300), unique=True)
  genre = db.Column(db.String(30))
  rating = db.Column(db.Float)

  def __init__(self, midi_path, wav_path, genre, rating):
    self.midi_path = midi_path
    self.wav_path = wav_path
    self.genre = genre
    self.rating = rating

# Song Schema
class SongSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    fields = ('id', 'midi_path', 'wav_path', 'genre', 'rating')

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
class UserSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    fields = ('id', 'user_name', 'hash_password', 'email')

# SongRating Class/Model
class SongRating(db.Model):
  __tablename__ = 'songrating'
  id = db.Column(db.Integer, primary_key=True)
  song_id = db.Column(db.Integer, db.ForeignKey("song.id"), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
  stars =  db.Column(db.Integer)
  __table_args__ = (
    db.UniqueConstraint(song_id, user_id),
  )

  def __init__(self, song_id, user_id, stars):
    self.song_id = song_id
    self.user_id = user_id
    self.stars = stars

# SongRating Schema 
class SongRatingSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    fields = ('id', 'song_id', 'user_id', 'stars')

# Initialize Song Schema 
Song_schema = SongSchema()
Songs_schema = SongSchema(many=True)

# Initialize User Schema 
User_schema = UserSchema()
Users_schema = UserSchema(many=True)

# Initialize SongRating Schema 
SongRating_schema = SongRatingSchema()
SongRatings_schema = SongRatingSchema(many=True)
