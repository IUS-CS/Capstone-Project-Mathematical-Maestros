import os
import redis 
from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Init CORS
cors = CORS(app, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_ORIGINS'] = ["http://localhost:3000"]

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Init limiter
limiter = Limiter(app, key_func=get_remote_address)

# Init Session
app.config['SECRET_KEY'] = 'super secret key'
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = redis.from_url("redis://127.0.0.1:6379")
server_session = Session(app)

# Run Server
if __name__ == '__main__':

  from routes import *

  app.run(debug=True, use_reloader=False)
