from FoodRecommender import db,ma



# Product Class/Model
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer)

  def __init__(self, name, description, price, qty):
    self.name = name
    self.description = description
    self.price = price
    self.qty = qty

# Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'qty')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)





# User Class/Model
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email_address = db.Column(db.String(length=50), nullable=False, unique=True)
  password = db.Column(db.String(length=60), nullable=False)

  def __init__(self, name, email_address,password ):
    self.name = name
    self.email_address=email_address
    self.password=password

  def check_password_correction(self, attempted_password):
    return self.password== attempted_password

# User Schema
class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'email_address', 'password')

# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)



# Ingredient Class/Model
class Ingredient(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
    # foreign key
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
    nullable=False)
  user = db.relationship('User',
    backref=db.backref('ingredients', lazy=True))
#   def __init__(self, name, email_address,password ):
#     self.name = name
#     self.email_address=email_address
#     self.password=password


# Ingredient Schema
# class UserSchema(ma.Schema):
#   class Meta:
#     fields = ('id', 'name', 'email_address', 'password')

# # Init schema
# user_schema = UserSchema()
# users_schema = ProductSchema(many=True)







