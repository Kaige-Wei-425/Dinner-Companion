# Import classes
from user_interface import UserInterface
from recipe_database import RecipeDatabase
from recipe import *

# Import other libraries
import sys
class DinnerCompainApp:
    
    def __init__(self):
        self.ui = UserInterface()
        self.database = RecipeDatabase()
        self.running = True

    def run(self):
        while self.running:
            choice = self.ui.display_mainMenu()
            match choice:
                # View all recipes
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    # Exit with status 0
                    sys.exit(0)



# Entry point of the app
if __name__ == "__main__":
    app = DinnerCompainApp()
    app.run()
