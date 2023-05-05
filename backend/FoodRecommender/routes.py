from re import I
from flask import jsonify
from flask import request
from FoodRecommender import app 
from FoodRecommender.models import Product,product_schema,products_schema
from FoodRecommender.models import User,user_schema, users_schema
from FoodRecommender.models import Ingredient, ingredient_schema, ingredients_schema
from FoodRecommender import db
from sqlalchemy.orm import joinedload
import spacy 

def textSimilarity(text1,text2):
    # here check text similarity of a tweet and their retweet count
    nlp = spacy.load("en_core_web_sm")
    #nlp = spacy.load("en_core_web_md")

    doc1 = nlp(text1)
    doc2 = nlp(text2)
    # print('T1 and T2',doc1.similarity(doc2)) 
    return doc1.similarity(doc2)





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
 type = request.json['type']
 currentUser = User.query.filter_by(id=userId ).first()
 print("ingredients are", Ingredients, "and user is ", currentUser)
 try:
    for ingredient in Ingredients:
        # Post(title='Hello Python!', body='Python is pretty cool', category=py)    
        print(ingredient)
        p=Ingredient(name=ingredient, type=type ,user=currentUser)
        print("ok")    
        currentUser.ingredients.append(p)
        print("ok")    

        db.session.add(currentUser)
    db.session.commit()

    return jsonify(Ingredients),200
 except:
    return jsonify("failed"),4004

# Get Profile
@app.route('/profile/<id>', methods=['GET'])
def get_profile(id):
    attempted_user = User.query.filter_by(id=id ).first()
    print("** attempted user is ", attempted_user)
    return ingredients_schema.jsonify(attempted_user.ingredients)


# check the healthy or allergic menu
@app.route('/checkIngredients', methods=['POST'])
def check_ingredients():
  userId = request.json['userId']
  ingredients = request.json['ingredients']
  print('** ingredients are ', ingredients, " user Ingredients are ", userId)

  # user profile
  attempted_user = User.query.filter_by(id=userId ).first()
  print("OK")
  userIngredients=attempted_user.ingredients

  print('** ingredients are ', ingredients, " user Ingredients are ", userIngredients)
  # algorithm
  allergicCount=0
  if(userIngredients and ingredients):
    for i in range(0, len(ingredients)):
      for ingredient in userIngredients:
        # print( ingredient.name)
        # print( ingredient.type)

        if(textSimilarity(ingredients[i],ingredient.name)>=0.8):
          print("check true ", ingredients[i],ingredient.name, " and ingredient type is ",ingredient.type)
          if(ingredient.type=='allergic'):
            allergicCount=allergicCount+1

  print("** allergic count is ", allergicCount)
  if (allergicCount/len(ingredients)*100>50):
    return jsonify("ingredients are allergic"),200
  return jsonify("ingredients are healthy"),200
















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
