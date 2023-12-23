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
        print(f"|=====Title=====|\n{self.title}\n")
        print(f"|=====Ingredients=====|\n{self.ingredients}\n")
        print(f"|=====Instructions=====|\n{self.instruction}\n")

    @abstractmethod
    def to_string(self):
        pass

# Subclass for categroy: main course
class MainCourse(Recipe):
    def __init__(self, title, ingredients, instruction, protein):
        super().__init__(title, ingredients, instruction, "MainCourse")
        self.protein = protein

    def display(self):
        super().display()
        print(f"|=====Protein Source=====|\n{self.protein}\n")
    
    def to_string(self):
        super().to_string()
        return f"{self.title}" + f"{self.ingredients} " + f"{self.instruction} " + f"{self.protein}"
    


# Subclass for categroy: side dish
class SideDish(Recipe):
    def __init__(self, title, ingredients, instruction, calorie):
        super().__init__(title, ingredients, instruction, "SideDish")
        self.calorie = calorie

    def display(self):
        super().display()
        print(f"|=====Approx Calories=====|\n{self.calorie}\n")

    def to_string(self):
        super().to_string()
        return f"{self.title}" + f"{self.ingredients} " + f"{self.instruction} " + f"{self.calorie}"

# Subclass for categroy: dessert
class Dessert(Recipe):
    def __init__(self, title, ingredients, instruction, sweetness_level):
        super().__init__(title, ingredients, instruction, "Dessert")
        self.sweetness_level = sweetness_level

    def display(self):
        super().display()
        print(f"|=====Sweetness Level=====|\n{self.sweetness_level}\n")

    def to_string(self):
        super().to_string()
        return f"{self.title}" + f"{self.ingredients} " + f"{self.instruction} " + f"{self.sweetness_level}"


