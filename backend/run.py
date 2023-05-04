from FoodRecommender import app

#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True) 




# to create the database/table or update the schema run these commands
# from FoodRecommender import app,db 
# app.app_context().push()
# db.create_all()

# from app import app,db 
# app.app_context().push()
# db.create_all()