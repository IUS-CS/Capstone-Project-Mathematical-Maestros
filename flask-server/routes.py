import os
from flask import jsonify, request, send_file, session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import and_
from sqlalchemy.sql import func
from midi2audio import FluidSynth
from app import app, limiter
from models import *
from generate import generate

# Get Current User From Session
@app.route("/users/session", methods=['GET'])
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401
    
    user = User.query.filter_by(id=user_id).first()
    return jsonify({
        "id": user.id,
        "user_name": user.user_name,
        "email": user.email
    }), 200

# Register User
@app.route('/users', methods=['POST'])
def register():
  user_name = request.json['user_name']
  email = request.json['email']
  password = request.json['password']

  user_name_exists = db.session.query(User.id).filter_by(user_name=user_name).first() is not None
  email_exists = db.session.query(User.id).filter_by(email=email).first() is not None

  if user_name_exists:
    return jsonify({"error": "User already exists"}), 401
  if email_exists:
    return jsonify({"error": "Email already exists"}), 401

  hash_password = generate_password_hash(password)
  new_user = User(user_name, hash_password, email)
  db.session.add(new_user)
  db.session.commit()

  return jsonify({
    "id": new_user.id,
    "user_name": new_user.user_name,
    "email": new_user.email
  }), 200

# Sign In
@app.route('/users/session', methods=['POST'])
def sign_in():
  user_name_entered = request.json['user_name']
  password_entered = request.json['password']

  user = db.session.query(User).filter(User.user_name==user_name_entered).first()

  if user is None:
    return jsonify({"error": "Unauthorized"}), 401
  
  if not check_password_hash(user.hash_password, password_entered):
    return jsonify({"error": "Unauthorized"}), 401
  
  session["user_id"] = user.id

  return jsonify({
    "id": user.id,
    "user_name": user.user_name,
    "email": user.email
  }), 200

# Delete Users Session (Logout)
@app.route('/users/session', methods=["DELETE"])
def logout_user():
  session.pop("user_id")
  return "200", 200

# Play a Song
@app.route('/play/<id>', methods=['GET'])
def play_Song(id):
  song = Song.query.get(id)
  return send_file(song.wav_path, mimetype="audio/wav")

# Create a Song
@app.route('/song', methods=['POST'])
@limiter.limit("100/day;10/hour;2/minute")
def add_Song():
  genre = request.json['genre']
  rating = request.json['rating']
  midi_path = generate(genre)
  
  base, _ = os.path.splitext(midi_path)
  wav_path = f'{base}.wav'  

  FluidSynth(f'datasets/{genre}/sound_font.sf2').midi_to_audio(midi_path, wav_path)
  
  new_Song = Song(midi_path, wav_path, genre, rating)
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
  midi_path = request.json['midi_path']
  wav_path = request.json['wav_path']
  genre = request.json['genre']
  rating = request.json['rating']
  song.midi_path = midi_path
  song.wav_path = wav_path
  song.genre = genre
  song.rating = rating
  db.session.commit()
  return Song_schema.jsonify(song)

# Delete Song
@app.route('/song/<id>', methods=['DELETE'])
def delete_Song(id):
  song = Song.query.get(id)
  if os.path.exists(song.midi_path) and os.path.exists(song.wav_path):
    os.remove(song.midi_path)
    os.remove(song.wav_path)
  db.session.delete(song)
  db.session.commit()
  return Song_schema.jsonify(song)

# Rate Song 
@app.route('/song/rating', methods=['POST'])
def rate_song():
  song_id = request.json['song_id']
  user_id = request.json['user_id']
  stars = request.json['stars']

  record_exists = db.session.query(SongRating).\
    filter(and_(SongRating.user_id==user_id, SongRating.song_id==song_id)).\
    first() is not None

  if record_exists:
    # Update Record
    db.session.query(SongRating).\
      filter(and_(SongRating.user_id==user_id, SongRating.song_id==song_id)).\
      update({'stars': stars})
  else:
    # Create new Record
    song_rating = SongRating(song_id, user_id, stars)
    db.session.add(song_rating)

  # Calculate new rating
  new_rating = Song.query.with_entities(func.avg(SongRating.stars)).\
    filter(SongRating.song_id==song_id)
  # Update Song rating
  db.session.query(Song).filter(Song.id==song_id).update({'rating': new_rating})
  db.session.commit()
  return jsonify({
    "song_id": song_id,
    "user_id": user_id,
    "stars": stars
  }), 200

# Get All Ratings
@app.route('/song/rating', methods=['GET'])
def get_all_ratings():
  all_ratings = SongRating.query.all()
  result = SongRatings_schema.dump(all_ratings)
  return jsonify(result)

# Get Rating for Current Song 
@app.route('/song/rating/<id>', methods=['GET'])
def get_rating(id):
  song = Song.query.get(id)
  rating = song.rating
  return jsonify(rating)