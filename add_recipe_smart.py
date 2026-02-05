import json
import os
import sys
from datetime import datetime

# Import smart categorization
sys.path.insert(0, '/root/.openclaw/workspace/recipe-backend')
from smart_categorize import categorize_recipe

DATA_FILE = '/root/.openclaw/workspace/recipe-backend/recipes.json'

def add_recipe(name, ingredients, calories=None, protein=None, source="", facebook_link="", steps=None, **kwargs):
    """Add a recipe with smart categorization"""
    
    # Get smart category
    category, subcategory = categorize_recipe(name, ingredients)
    
    recipe = {
        "id": str(int(datetime.now().timestamp() * 1000)),
        "name": name,
        "category": category,
        "subcategory": subcategory,
        "source": source,
        "facebook_link": facebook_link,
        "date": datetime.now().isoformat(),
        "ingredients": ingredients,
        "steps": steps or [],
    }
    
    if calories:
        recipe["calories"] = calories
    if protein:
        recipe["protein"] = protein
        
    # Add any additional fields
    recipe.update(kwargs)
    
    # Load existing recipes
    with open(DATA_FILE, 'r') as f:
        recipes = json.load(f)
    
    # Add new recipe at beginning
    recipes.insert(0, recipe)
    
    # Save
    with open(DATA_FILE, 'w') as f:
        json.dump(recipes, f, indent=2)
    
    print(f"✅ Added: {name}")
    print(f"   Category: {category}")
    print(f"   Subcategory: {subcategory}")
    print(f"   Total recipes: {len(recipes)}")
    
    return recipe


if __name__ == '__main__':
    # Example usage
    if len(sys.argv) > 1:
        # Manual add from command line
        name = sys.argv[1]
        print(f"Adding recipe: {name}")
        print("Smart categorization will be applied.")
    else:
        print("Usage: python3 add_recipe_smart.py 'Recipe Name'")
        print("\nSmart categorization system ready!")
        print("Categories: breakfast, lunch, dinner, snack, dessert, side, beverage")
