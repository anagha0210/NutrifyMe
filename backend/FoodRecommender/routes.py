from re import I
from flask import jsonify
from flask import request
from FoodRecommender import app 
from FoodRecommender.models import Product,product_schema,products_schema
from FoodRecommender.models import User,user_schema, users_schema
from FoodRecommender.models import Ingredient
from FoodRecommender import db
from sqlalchemy.orm import joinedload
@app.route('/', methods=['GET'])
def check_api():
  return "api is running"


# ///////////////////////////////////////////////////////////////// User Routes
# Register a User
@app.route('/register', methods=['POST'])
def register_user():
  name = request.json['name']
  email_address = request.json['emailAddress']
  password = request.json['password']
  attempted_user = User.query.filter_by(email_address=email_address ).first()
  if(attempted_user):
    return jsonify("Failed! Email is already in use!"),404

  new_user = User(name, email_address, password)
  db.session.add(new_user)
  db.session.commit()
  return user_schema.jsonify(new_user)

# Sign in
@app.route('/signIn', methods=['POST'])
def signIn_user():
 email_address = request.json['emailAddress']
 password = request.json['password']
 attempted_user = User.query.filter_by(email_address=email_address ).first()
 if attempted_user and attempted_user.check_password_correction(attempted_password=password ):
    return user_schema.jsonify(attempted_user)
 else:
    return jsonify("Log in failed!"),404


# Get All users
@app.route('/users', methods=['GET'])
def get_users():
  all_users = User.query.all()
  result = users_schema.dump(all_users)
  return jsonify(result)

#//////////////////////////////////////////////////////////////////// Ingredient routes
@app.route('/addProfile', methods=['POST'])
def add_profile():
 userId = request.json['userId']
 Ingredients = request.json['ingredients']
 currentUser = User.query.filter_by(id=userId ).first()
 print("ingredients are", Ingredients, "and user is ", currentUser)
 try:
    for ingredient in Ingredients:
        # Post(title='Hello Python!', body='Python is pretty cool', category=py)    
        p=Ingredient(name=ingredient,user=currentUser)    
        currentUser.ingredients.append(p)
        db.session.add(currentUser)
    db.session.commit()

    return jsonify(Ingredients),200
 except:
    return jsonify("failed"),4004

# Get Profile
@app.route('/profile/<id>', methods=['GET'])
def get_profile(id):
    query = User.query.options(joinedload('ingredients'))
    for user in query:
        print (user, user.ingredients)
    return jsonify('profile extracted')
#   product = User.query.get(id)
#   return product_schema.jsonify(product)

#//////////////////////////////////////////////////////////////////// Product Routes



















# Create a Product
@app.route('/product', methods=['POST'])
def add_product():
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  new_product = Product(name, description, price, qty)

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

  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  product.name = name
  product.description = description
  product.price = price
  product.qty = qty

  db.session.commit()

  return product_schema.jsonify(product)

# Delete Product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)
