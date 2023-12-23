# Import abstract class
from abc import ABC, abstractmethod

# Abstract class
class Recipe(ABC):
    def __init__(self, title, ingredients, instruction, category):
        self.title = title
        self.ingredients = ingredients
        self.instruction = instruction
        self.category = category

    # Abstract method must be denoted by non-abstract subclass
    @abstractmethod
    def display(self):
        pass

# Subclass for categroy: main course
class MainCourse(Recipe):
    def __init__(self, title, ingredients, instruction):
        super().__init__(title, ingredients, instruction, "MainCourse")

    def display(self):
        print(f"Title\n{self.title}\n")
        print(f"Ingredients\n{self.ingredients}\n")
        print(f"Instructions\n{self.instruction}\n")


mai = MainCourse("chicken", "chicken, oil", "This is fried chicken!")
mai.display()