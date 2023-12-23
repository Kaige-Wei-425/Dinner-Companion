class UserInterface:

    # def __init__(self, recipeDB):
    #     self.recipeDB = recipeDB

    # Display the main menu
    def display_mainMenu(self):
        print("===================================")
        print("*   Welcome to Dinner Companion   *")
        print("===================================")
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

ui = UserInterface()
a = ui.display_mainMenu()
a
print(a)