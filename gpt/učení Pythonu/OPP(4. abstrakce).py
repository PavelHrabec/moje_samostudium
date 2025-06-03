

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

# shape = Shape()  ❌ nelze vytvořit
rect = Rectangle(5, 3)
print("Obsah obdélníku:", rect.area())

#Shape je abstraktní třída, kterou nemůžeš přímo vytvořit, jen rozšířit.

