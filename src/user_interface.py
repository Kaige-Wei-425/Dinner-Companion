class UserInterface:

    # def __init__(self, recipeDB):
    #     self.recipeDB = recipeDB

    # Display the main menu
    def display_mainMenu(self):
        print("\nPlease select from the following options:\n")
        print("> 1. View All Recipes")
        print("> 2. Add Recipe")
        print("> 3. Search Recipe")
        print("> 4. Update Recipe")
        print("> 5. Delete Recipe")
        print("> 6. Exit")

        return input(">_: ")

    # Display the sub menu of search
    def display_searchMenu(self):
        print("==============")
        print("*   Search   *")
        print("==============\n")
        print("> 1. Search by Category")
        print("> 2. Search by Title")
        print("> 3. Search by Ingredients")
        print("> 4. Back to Main Menu --> ")

        return input(">_: ")

    # Display the category of the recipe
    def display_category(self):
        print("Which type of recipe would you like to add?\n")
        print("> 1. Main Course")
        print("> 2. Side Dish")
        print("> 3. Dessert")
        print("> 4. Back to Main Menu --> ")

        return input(">_: ")
    
    # Prompt users enter several ingredients unitl they enter 'done' or press 'Enter'
    def prompt_for_ingredients(self):
        ingredients = []
        print("> Ingredients:\n")
        is_done = False
        while not is_done:
            ingredient = input("> Please enter an ingredient(enter 'done' or press 'Enter' to finish)\n")
            # Check whether the user enter 'done' or press 'Enter'
            if ingredient.lower() == 'done' or ingredient == '':
                is_done = True
            ingredients.append(ingredient)
        return ingredients

    # Prompt users enter step-by-step instructions unitl they enter 'done' or press 'Enter'
    def prompt_for_instructions(self):
        instructions = []
        print("> Instruction:\n")
        is_done = False
        while not is_done:
            step = input("> Please enter one step (enter 'done' or press 'Enter' to finish)\n")
            # Check whether the user enter 'done' or press 'Enter'
            if step.lower() == 'done' or step == '':
                is_done = True
            instructions.append(step)
        return instructions
    
    # Prompt user enter the main course
    def prompt_main_course(self):
        print("Please enter the details of the recipe")
        title = input("> Title:\n")
        ingredients = self.prompt_for_ingredients()
        instruction = self.prompt_for_instructions()
        protein = input("> Protein:\n")

        return title, ingredients, instruction, protein
    
    # Prompt user enter the side dish
    def prompt_side_dish(self):
        print("Please enter the details of the recipe")
        title = input("> Title:\n")
        ingredients = self.prompt_for_ingredients()
        instruction = self.prompt_for_instructions()
        calorie = input("> Calorie:\n")

        return title, ingredients, instruction, calorie
    
    # Prompt user enter the dessert
    def prompt_dessert(self):
        print("Please enter the details of the recipe")
        title = input("> Title:\n")
        ingredients = self.prompt_for_ingredients()
        instruction = self.prompt_for_instructions()
        sweetness_level = input("> Sweetness Level:\n")

        return title, ingredients, instruction, sweetness_level
    
    # Prompt user search from the existing categories
    def prompt_search_by_category(self):
        print("Please select which type of dinner your want to search?")
        print("> 1. Main Course")
        print("> 2. Side Dish")
        print("> 3. Dessert")
        print("> 4. Back --> ")

        return input(">_: ")
    
    # Prompt user enter the title of the recipe they want to search
    def prompt_search_by_title(self):
        print("Please enter the title of the recipe")

        return input(">_: ")

    # Prompt user check the available recipe by entering ingredient
    def prompt_search_by_ingredient(self):
        print("Please enter the ingrediet you have")
        
        return input(">_: ")
    
    # Prompt user enter the title of the recipe they want to update
    def prompt_update_recipe(self):
        print("Enter the title of the recipe you want to update")

        return input(">_: ")
    
    # Prompt user enter the title of the recipe they want to delete
    def prompt_delete_recipe(self):
        print("Enter the title of the recipe you want to delete")

        return input(">_: ")