# Import classes
from user_interface import UserInterface
from recipe_database import RecipeDatabase
from recipe import *
from data_validator import DataValidator

# Import other libraries

class DinnerCompainApp:
    
    def __init__(self):
        self.ui = UserInterface()
        self.database = RecipeDatabase()
        # Load the database from the file when initialize the app.
        try:
            self.database.load_from_file('database.txt')
            print("Database Loaded Successfully")
        except Exception as e:
            print(f"Unable to Load the Database: {e}")

        self.running = True

    def run(self):
        '''
        run() is the function that control the primary logic of the app.
        '''
        # The welcome message will print only once when run the program.
        print("===================================")
        print("*   Welcome to Dinner Companion   *")
        print("===================================")

        while self.running:
            try:
                choice = int(self.ui.display_mainMenu())
            except ValueError:
                print("\n******************************************")
                print("* Invalid input! Please enter a integer! *")
                print("******************************************\n")
            else:
                # Check whether the user input is numerical and in range (1, 6)
                if DataValidator.is_valid_int(choice, 1, 6):
                    match choice:
                        # View all recipes
                        case 1:
                            self.database.print_all_recipes()

                        # Add recipe
                        case 2:
                            self.add_rcp()
                        
                        # Search recipe
                        case 3:
                            self.search_recipe()
                        
                        # Update recipe
                        case 4:
                            pass
                        
                        # Delete recipe
                        case 5:
                            pass
                        
                        # Exit the app
                        case 6:
                            exit()
                else:
                    print("\n*****************************************")
                    print("* Please choose your option from 1 to 6!*")
                    print("*****************************************\n")


    def add_rcp(self):
        '''
        This is the primary function for adding recipe to the database and output them to the file
        '''
        is_add = False
        while not is_add:
            try:
                choice = int(self.ui.display_category())
            except ValueError:
                print("\n******************************************")
                print("* Invalid input! Please enter a integer! *")
                print("******************************************\n")
            else:
                if DataValidator.is_valid_int(choice, 1, 4):
                    match choice:
                        # Add main course
                        case 1:
                            title, ingredients, instruction, protein = self.ui.prompt_main_course()
                            # Create a main course object
                            recipe = MainCourse(title, ingredients, instruction, protein)
                            # Add it into the database
                            self.database.add_recipe(recipe)
                        
                        # Add side dish
                        case 2:
                            title, ingredients, instruction, calorie = self.ui.prompt_side_dish()
                            # Create a side dish object
                            recipe = SideDish(title, ingredients, instruction, calorie)
                            # Add it into the database
                            self.database.add_recipe(recipe)
               
                        # Add dessert
                        case 3:
                            title, ingredients, instruction, sweetness_level = self.ui.prompt_dessert()
                            # Create a dessert object
                            recipe = Dessert(title, ingredients, instruction, sweetness_level)
                            # Add it into the database
                            self.database.add_recipe(recipe)

                        case 4:
                            # Output all the recipes into the database before exit this menu
                            self.database.load_into_file('database.txt')
                            is_add = True
                else:
                    print("\n*****************************************")
                    print("* Please choose your option from 1 to 4!*")
                    print("*****************************************\n")
    
    def search_recipe(self):
        is_searched = False
        while not is_searched:
            try:
                choice = int(self.ui.display_searchMenu())
            except ValueError:
                print("\n******************************************")
                print("* Invalid input! Please enter a integer! *")
                print("******************************************\n")
            else:
                if DataValidator.is_valid_int(choice, 1, 4):
                    match choice:
                        # Search by Categories
                        case 1:
                            is_done = False
                            while not is_done:
                                try:
                                    cate = int(self.ui.prompt_search_by_category())
                                except ValueError:
                                    print("\n******************************************")
                                    print("* Invalid input! Please enter a integer! *")
                                    print("******************************************\n")
                                else:
                                    if DataValidator.is_valid_int(choice, 1, 4):
                                        match cate:
                                            # Main Course
                                            case 1:
                                                search_by_cate = self.database.search_by_category("MainCourse")
                                                for rcp in search_by_cate:
                                                    rcp.display()
                                            # Side Dish
                                            case 2:
                                                pass
                                            # Dessert
                                            case 3:
                                                pass
                                            case 4:
                                                is_done = True
                                    else:
                                        print("\n*****************************************")
                                        print("* Please choose your option from 1 to 4!*")
                                        print("*****************************************\n")
                            
                        case 2:
                            pass
                        case 3:
                            pass
                        # Back to the menu
                        case 4:
                            is_searched = True
                else:
                    print("\n*****************************************")
                    print("* Please choose your option from 1 to 4!*")
                    print("*****************************************\n")

# Entry point of the app
if __name__ == "__main__":
    app = DinnerCompainApp()
    app.run()
