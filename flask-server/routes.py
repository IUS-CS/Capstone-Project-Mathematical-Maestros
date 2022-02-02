import glob
import uuid

from flask import jsonify, request, send_file
from werkzeug.security import check_password_hash, generate_password_hash

from app import basedir, os, app, limiter
from models import *

from midi2audio import FluidSynth

# Register User
@app.route('/register', methods=['GET', 'POST'])
def register():
  user_name = request.json['user_name']
  email = request.json['email']
  password = request.json['password']
  user_name_exists = db.session.query(User.id).filter_by(user_name=user_name).first() is not None
  email_exists = db.session.query(User.id).filter_by(email=email).first() is not None
  if user_name_exists or email_exists:
    return jsonify({'user_added': False}), 403
  hash_password = generate_password_hash(password)
  new_user = User(user_name, hash_password, email)
  db.session.add(new_user)
  db.session.commit()
  return jsonify({'user_added': True}), 200

# Sign In
@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
  user_name_entered = request.json['user_name']
  password_entered = request.json['password']
  user = db.session.query(User).filter(User.user_name==user_name_entered).first()
  if user is not None and check_password_hash(user.hash_password, password_entered):
    return jsonify({'signed_in': True}), 200
  return jsonify({'signed_in': False}), 403

# Play a Song
@app.route('/play/<id>', methods=['GET'])
def play_Song(id):
  song = Song.query.get(id)
  return send_file(song.path, mimetype="audio/wav")

# Create a Song
@app.route('/song', methods=['POST'])
@limiter.limit("100/day;10/hour;2/minute")
def add_Song():
  steps = request.json['steps']
  os.system("melody_rnn_generate \
    --config=basic_rnn \
    --bundle_file="+basedir+"/magenta/basic_rnn.mag \
    --output_dir="+basedir+"/library \
    --num_outputs=1 \
    --num_steps="+str(steps)+" \
    --primer_melody=[60]")
 
  folder_path = basedir+"/library"
  file_type = '/*mid'
  files = glob.glob(folder_path + file_type)
  max_file = max(files, key=os.path.getctime)
  path = max_file

  new_path = basedir+'/library/'+uuid.uuid4().hex+'.wav'  

  fs = FluidSynth()
  fs.midi_to_audio(path, new_path)

  os.remove(path)

  new_Song = Song(new_path, steps)
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
