from recipe import *
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

    # Save the recipe collection into the file
    def load_into_file(self, file_path):
        try:
            with open(file_path, 'w') as file:
                for recipe in self.recipes:
                    file.write(recipe.__str__())
                    file.write("\n")
        except FileNotFoundError:
            print("File Not Found!")
    
    # 
    def parse_line_to_recipe(line):
        portions = line.strip().split(' ')


    # Load the recipes from the file
    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if line[0] == "MainCourse":
                        title = line[1]
                        ingredients = line[2].strip().split(',')
                        instruction = line[3].strip().split(',')
                        protein = line[4]
                        self.recipes.append(MainCourse(title, ingredients, instruction, protein))

                    if line[0] == "SideDish":
                        title = line[1]
                        ingredients = line[2].strip().split(',')
                        instruction = line[3].strip().split(',')
                        calorie = line[4]
                        self.recipes.append(SideDish(title, ingredients, instruction, calorie))

                    if line[0] == "Dessert":
                        title = line[1]
                        ingredients = line[2].strip().split(',')
                        instruction = line[3].strip().split(',')
                        sweetness_level = line[4]
                        self.recipes.append(Dessert(title, ingredients, instruction, sweetness_level))

        except FileNotFoundError:
            print("File Not Found!")

