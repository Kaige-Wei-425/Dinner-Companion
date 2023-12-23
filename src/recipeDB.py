# This class manages the collections of the recipes
class RecipeDatabase:
    def __init__(self):
        self.recipes = []

    # Create new recipes
    def add_recipe(self, recipe):
        self.recipes.append(recipe)
    
    # Seach functions
    # 1. Search by categories
    def search_by_category(self, category):
        return [recipe for recipe in self.recipes if recipe.category == category]
    
    # 2. Search by title of the recipe
    def search_by_title(self, title):
        return [recipe for recipe in self.recipes if recipe.title == title]
    
    # 3. Search by ingredients
    def search_by_ingredients(self, ingredients):
        return [recipe for recipe in self.recipes if ingredients in self.ingredients]
    
    
    # Update

    # Delete
