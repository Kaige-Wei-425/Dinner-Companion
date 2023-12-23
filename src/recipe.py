# Import abstract class
from abc import ABC, abstractmethod

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