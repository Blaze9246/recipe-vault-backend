#!/usr/bin/env python3
"""
Add recipe with cover image from screenshot
Usage: python3 add_recipe_with_image.py <recipe_name> <image_path>
"""

import json
import os
import sys
import shutil
from datetime import datetime

sys.path.insert(0, '/root/.openclaw/workspace/recipe-backend')
from smart_categorize import categorize_recipe

DATA_FILE = '/root/.openclaw/workspace/recipe-backend/recipes.json'
IMAGES_DIR = '/root/.openclaw/workspace/recipe-backend/images'

def add_recipe_with_cover(name, ingredients, image_path, calories=None, protein=None, 
                          source="", facebook_link="", steps=None, **kwargs):
    """Add a recipe with cover image from screenshot"""
    
    # Get smart category
    category, subcategory = categorize_recipe(name, ingredients)
    
    # Copy image to images folder with safe filename
    safe_name = name.lower().replace(' ', '_').replace('/', '_')[:30]
    cover_filename = f"{safe_name}_cover.jpg"
    cover_path = os.path.join(IMAGES_DIR, cover_filename)
    
    if os.path.exists(image_path):
        shutil.copy2(image_path, cover_path)
        print(f"📸 Cover image saved: {cover_filename}")
    else:
        print(f"⚠️ Image not found: {image_path}")
        cover_filename = None
    
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
    if cover_filename:
        recipe["image"] = f"images/{cover_filename}"
        recipe["cover_image"] = f"images/{cover_filename}"
        
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
    if cover_filename:
        print(f"   Cover: {cover_filename}")
    print(f"   Total recipes: {len(recipes)}")
    
    return recipe


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 add_recipe_with_image.py 'Recipe Name' /path/to/image.jpg")
        print("\nExample:")
        print("  python3 add_recipe_with_image.py 'Chicken Nuggets' /path/to/screenshot.jpg")
        sys.exit(1)
    
    name = sys.argv[1]
    image_path = sys.argv[2]
    
    # Example ingredients - in real use, these would be extracted
    ingredients = ["See recipe details"]
    
    add_recipe_with_cover(name, ingredients, image_path)
