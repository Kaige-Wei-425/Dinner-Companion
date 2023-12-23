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
        self.running = True

    def run(self):
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
                if DataValidator.is_valid_int(choice, 1, 6):
                    match choice:
                        case 1:
                            print("1")
                        case 6:
                            exit()
                else:
                    print("\n*****************************************")
                    print("* Please choose your option from 1 to 6!*")
                    print("*****************************************\n")
                




# Entry point of the app
if __name__ == "__main__":
    app = DinnerCompainApp()
    app.run()
