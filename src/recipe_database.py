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
        for rcp in self.recipes:
            # Return the recipe if the input title can be found in the database
            if rcp.title == title:
                return rcp
            # Otherwise, return None
            else:
                return None
    
    # 3. Search by ingredients
    def search_by_ingredients(self, ingredients):
        for rcp in self.recipes:
            # Return the recipe if the input ingredients can be found in the database
            if ingredients in rcp.ingredients:
                return rcp
            # Otherwise, return None
            else:
                return None
        
    # Update functions
    def update_recipe(self, title, new_recipe):
        for i, rcp in enumerate(self.recipes):
            # Find the recipe that the user want to update by title
            if rcp.title == title:
                # Update the original recipe with the new recipe
                self.recipes[i] = new_recipe
                # Indicate the update was successful by returning true
                return True
        return False
            

    # Delete recipe by title
    def delete_recipe(self, title):
        for rcp in self.recipes:
            if rcp.title == title:
                self.recipes.remove(rcp)

    # Output the recipe database to file
    def file_output(self, file_path):
        try:
            with open(file_path, 'w') as file:
                for recipe in self.recipes:
                    file.write(recipe)
        except FileNotFoundError:
            print("File Not Found!")

