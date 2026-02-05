#!/usr/bin/env python3
"""
Smart Recipe Categorization System
Analyzes recipe name and ingredients to determine proper category
"""

def categorize_recipe(name, ingredients):
    """
    Categorize recipe based on name and ingredients
    Returns: (category, subcategory)
    """
    name_lower = name.lower()
    ingredients_lower = ' '.join(ingredients).lower() if ingredients else ''
    combined = f"{name_lower} {ingredients_lower}"
    
    # DESSERT indicators
    dessert_keywords = [
        'cookie', 'cake', 'brownie', 'pie', 'tart', 'muffin', 'cupcake',
        'pudding', 'mousse', 'cheesecake', 'doughnut', 'donut', 'pastry',
        'cinnamon bun', 'cinnamon roll', 'meringue', 'fudge', 'truffle',
        'macaron', 'eclair', 'tiramisu', 'panna cotta', 'creme brulee',
        'sorbet', 'ice cream', 'gelato', 'chocolate', 'candy', 'sweet',
        'dessert', 'treat', 'baked good', 'baking'
    ]
    
    # BREAKFAST indicators
    breakfast_keywords = [
        'pancake', 'waffle', 'french toast', 'oatmeal', 'porridge', 'granola',
        'smoothie bowl', 'breakfast', 'morning', 'eggs benedict', 'omelette',
        'scrambled eggs', 'breakfast burrito', 'breakfast sandwich', 'cereal',
        'parfait', 'bagel', 'croissant', 'breakfast'
    ]
    
    # SNACK indicators (light, finger foods, appetizers)
    snack_keywords = [
        'nugget', 'chip', 'cracker', 'popcorn', 'pretzel', 'trail mix',
        'energy ball', 'protein ball', 'bite', 'bar', 'snack', 'appetizer',
        'dip', 'hummus', 'salsa', 'guacamole', 'bruschetta', 'canape',
        'finger food', 'party food', 'roll-up', 'pinwheel', 'skewer'
    ]
    
    # LUNCH indicators
    lunch_keywords = [
        'sandwich', 'wrap', 'burger', 'slider', 'taco', 'burrito', 'quesadilla',
        'salad', 'bowl', 'soup', 'chili', 'stew', 'pasta salad', 'pizza',
        'flatbread', 'pita', 'lunch', 'meal prep'
    ]
    
    # DINNER indicators
    dinner_keywords = [
        'steak', 'roast', 'casserole', 'curry', 'stir fry', 'pasta', 'lasagna',
        'meatball', 'meatloaf', 'grilled chicken', 'salmon', 'fish', 'shrimp',
        'risotto', 'paella', 'tagine', 'dinner', 'main course', 'entree'
    ]
    
    # SIDE DISH indicators
    side_keywords = [
        'rice', 'quinoa', 'couscous', 'potato', 'mashed potato', 'fries',
        'roasted vegetables', 'green beans', 'asparagus', 'brussels sprouts',
        'coleslaw', 'side', 'accompaniment'
    ]
    
    # DRINK indicators
    drink_keywords = [
        'smoothie', 'shake', 'juice', 'latte', 'coffee', 'tea', 'cocktail',
        'mocktail', 'lemonade', 'milkshake', 'protein shake', 'drink', 'beverage'
    ]
    
    # Check for matches
    def has_keyword(keywords):
        for kw in keywords:
            if kw in combined:
                return True
        return False
    
    # Protein detection for subcategory
    protein_keywords = ['chicken', 'beef', 'pork', 'fish', 'salmon', 'tuna', 
                       'shrimp', 'turkey', 'protein', 'egg', 'tofu', 'tempeh']
    is_high_protein = has_keyword(protein_keywords)
    
    # Calorie detection
    is_low_calorie = 'low calorie' in combined or 'low-calorie' in combined or 'diet' in combined
    
    # Determine category (check in order of specificity)
    if has_keyword(dessert_keywords):
        category = 'dessert'
        if is_high_protein:
            subcategory = 'high-protein'
        elif is_low_calorie:
            subcategory = 'low-calorie'
        else:
            subcategory = 'sweet treat'
            
    elif has_keyword(breakfast_keywords):
        category = 'breakfast'
        if is_high_protein:
            subcategory = 'high-protein'
        else:
            subcategory = 'morning meal'
            
    elif has_keyword(snack_keywords):
        category = 'snack'
        if is_high_protein:
            subcategory = 'high-protein snack'
        elif is_low_calorie:
            subcategory = 'low-calorie snack'
        else:
            subcategory = 'finger food'
            
    elif has_keyword(dinner_keywords):
        category = 'dinner'
        if is_high_protein:
            subcategory = 'high-protein'
        else:
            subcategory = 'main course'
            
    elif has_keyword(lunch_keywords):
        category = 'lunch'
        if is_high_protein:
            subcategory = 'high-protein'
        else:
            subcategory = 'midday meal'
            
    elif has_keyword(side_keywords):
        category = 'side'
        subcategory = 'accompaniment'
        
    elif has_keyword(drink_keywords):
        category = 'beverage'
        subcategory = 'drink'
        
    else:
        # Default to lunch for savory, snack for undefined
        if 'sweet' in combined or 'sugar' in combined:
            category = 'dessert'
            subcategory = 'sweet treat'
        elif is_high_protein:
            category = 'lunch'
            subcategory = 'high-protein'
        else:
            category = 'lunch'
            subcategory = 'meal'
    
    return category, subcategory


if __name__ == '__main__':
    # Test cases
    test_recipes = [
        ("Homemade Chicken Nuggets", ["chicken breast", "cheese", "egg", "paprika"]),
        ("1 Calorie Meringue Cookies", ["egg whites", "sweetener", "vanilla"]),
        ("Protein Cinnamon Buns", ["greek yogurt", "flour", "cinnamon", "protein powder"]),
        ("Breakfast Smoothie Bowl", ["banana", "berries", "protein powder", "granola"]),
        ("Grilled Salmon with Asparagus", ["salmon", "asparagus", "lemon", "olive oil"]),
    ]
    
    print("🔥 SMART RECIPE CATEGORIZATION TEST\n")
    for name, ingredients in test_recipes:
        category, subcategory = categorize_recipe(name, ingredients)
        print(f"📋 {name}")
        print(f"   → Category: {category}")
        print(f"   → Subcategory: {subcategory}\n")
