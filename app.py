from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATA_FILE = 'recipes.json'
IMAGES_DIR = 'images'

def load_recipes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_recipes(recipes):
    with open(DATA_FILE, 'w') as f:
        json.dump(recipes, f, indent=2)

@app.route('/')
def home():
    return jsonify({
        "message": "🔥 Recipe Vault API",
        "status": "running",
        "endpoints": {
            "GET /recipes": "Get all recipes",
            "POST /recipes": "Add new recipe",
            "DELETE /recipes/<id>": "Delete recipe",
            "GET /images/<filename>": "Get recipe image"
        }
    })

@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify(load_recipes())

@app.route('/recipes', methods=['POST'])
def add_recipe():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Recipe name required"}), 400
    
    recipe = {
        "id": str(int(datetime.now().timestamp() * 1000)),
        "name": data.get('name', ''),
        "calories": data.get('calories', 0),
        "ingredients": data.get('ingredients', []),
        "steps": data.get('steps', []),
        "category": data.get('category', ''),
        "cover_image": data.get('cover_image', ''),
        "facebook_link": data.get('facebook_link', ''),
        "date": datetime.now().isoformat()
    }
    
    recipes = load_recipes()
    recipes.insert(0, recipe)
    save_recipes(recipes)
    
    return jsonify(recipe), 201

@app.route('/recipes/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipes = load_recipes()
    recipes = [r for r in recipes if r.get('id') != recipe_id]
    save_recipes(recipes)
    return jsonify({"message": "Recipe deleted"})

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGES_DIR, filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
