
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
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

# Product Class/Model
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  path = db.Column(db.String(100), unique=True)
  steps = db.Column(db.Integer)

  def __init__(self, path, steps):
    self.path = path
    self.steps = steps

# Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'path', 'steps')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create a Product
@app.route('/product', methods=['POST'])
def add_product():
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
  new_product = Product(path, steps)
  db.session.add(new_product)
  db.session.commit()
  return product_schema.jsonify(new_product)

# Get All Products
@app.route('/product', methods=['GET'])
def get_products():
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  return jsonify(result)

# Get Single Products
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
  product = Product.query.get(id)
  return product_schema.jsonify(product)

# Update a Product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
  product = Product.query.get(id)
  path = request.json['path']
  steps = request.json['steps']
  product.path = path
  product.steps = steps
  db.session.commit()
  return product_schema.jsonify(product)

# Delete Product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  if os.path.exists(product.path):
    os.remove(product.path)
  db.session.delete(product)
  db.session.commit()
  return product_schema.jsonify(product)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)