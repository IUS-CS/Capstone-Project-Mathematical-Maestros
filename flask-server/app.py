import os

from flask import Flask
from flask_cors import CORS, cross_origin


# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Run Server
if __name__ == '__main__':

  from routes import *

  app.run(debug=True)
