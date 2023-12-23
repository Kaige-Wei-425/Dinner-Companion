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

        return input(">_: ")

    # Display the category of the recipe
    def display_category(self):
        print("Which type of recipe would you like to add?\n")
        print("> 1. Main Course")
        print("> 2. Side Dish")
        print("> 3. Dessert")
        print("> 4. Back to Main Menu --> ")

        return input(">_: ")
    
    # Prompt user enter the main course
    def prompt_main_course(self):
        print("Please enter the details of the recipe")
        title = input("> Title:\n")
        ingredients = input("> Ingredients:\n")
        instruction = input("> Instruction:\n")
        protein = input("> Protein:\n")

        return title, ingredients, instruction, protein
    
    # Prompt user enter the side dish
    def prompt_side_dish(self):
        print("Please enter the details of the recipe")
        title = input("> Title:\n")
        ingredients = input("> Ingredients:\n")
        instruction = input("> Instruction:\n")
        calorie = input("> Calorie:\n")

        return title, ingredients, instruction, calorie
    
    # Prompt user enter the dessert
    def prompt_dessert(self):
        print("Please enter the details of the recipe")
        title = input("> Title:\n")
        ingredients = input("> Ingredients:\n")
        instruction = input("> Instruction:\n")
        sweetness_level = input("> Sweetness Level:\n")

        return title, ingredients, instruction, sweetness_level