# app.py
from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# Replace 'mongodb://localhost:27017/recipe-database' with your actual MongoDB URL
app.config['MONGO_URI'] = 'mongodb://localhost:27017/recipe-database'

mongo = PyMongo(app)

# No need to insert sample recipes in this case

@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    recipes = list(mongo.db.recipe_table.find())
    recipe_list = [{"id": str(recipe["_id"]), "name": recipe["name"], "total_ingredients": recipe["total_ingredients"]} for recipe in recipes]
    return jsonify(recipe_list)

if __name__ == '__main__':
    app.run(debug=True)



# for api checking Url ==>   127.0.0.1:5000/api/recipes