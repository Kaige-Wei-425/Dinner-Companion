# Import classes
from user_interface import UserInterface
from recipe_database import RecipeDatabase
from recipe import *

# Import other libraries

class DinnerCompainApp:
    
    def __init__(self):
        self.ui = UserInterface()
        self.database = RecipeDatabase()
        self.running = True

    def run(self):
        while self.running:
            choice = int(self.ui.display_mainMenu())
            match choice:
                case 1:
                    print("1")
                case 6:
                    exit()
                




# Entry point of the app
if __name__ == "__main__":
    app = DinnerCompainApp()
    app.run()
