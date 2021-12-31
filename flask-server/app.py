import os

from flask import Flask
from flask_cors import CORS

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# CORS
cors = CORS(app)
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

# Run Server
if __name__ == '__main__':

  from routes import *

  app.run(debug=True)
