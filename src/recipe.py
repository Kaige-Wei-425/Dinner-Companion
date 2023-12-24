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
        print(f"|=====Ingredients=====|")
        for igd in self.ingredients:
            print(igd)
        print(f"|=====Instructions=====|")
        for ist in self.instruction:
            print(ist)

    @abstractmethod
    def __str__(self):
        # Handle the list variable ingredients and instructions
        ingredient_str = ','.join(self.ingredients)
        instruction_str = ','.join(self.instruction)
        return f"{self.title}=" + f"{ingredient_str}=" + f"{instruction_str}="

# Subclass for categroy: main course
class MainCourse(Recipe):
    def __init__(self, title, ingredients, instruction, protein):
        super().__init__(title, ingredients, instruction, "MainCourse")
        self.protein = protein

    def display(self):
        super().display()
        print(f"|=====Protein Source=====|\n{self.protein}\n")
    
    def __str__(self):
        basic_details = super().__str__()
        return (f"{self.category}=" + f"{basic_details}" + f"{self.protein}")
    


# Subclass for categroy: side dish
class SideDish(Recipe):
    def __init__(self, title, ingredients, instruction, calorie):
        super().__init__(title, ingredients, instruction, "SideDish")
        self.calorie = calorie

    def display(self):
        super().display()
        print(f"|=====Approx Calories=====|\n{self.calorie}\n")

    def __str__(self):
        basic_details = super().__str__()
        return (f"{self.category}=" + f"{basic_details}" + f"{self.calorie}")

# Subclass for categroy: dessert
class Dessert(Recipe):
    def __init__(self, title, ingredients, instruction, sweetness_level):
        super().__init__(title, ingredients, instruction, "Dessert")
        self.sweetness_level = sweetness_level

    def display(self):
        super().display()
        print(f"|=====Sweetness Level=====|\n{self.sweetness_level}\n")

    def __str__(self):
        basic_details = super().__str__()
        return (f"{self.category}=" + f"{basic_details}" + f"{self.sweetness_level}")


