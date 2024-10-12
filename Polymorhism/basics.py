from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Pizza(Circle):
    
    def __init__(self, radius, toppings):
        super().__init__(radius)
        self.toppings = toppings
        
    def area(self):
        return super().area() + 0.5 * len(self.toppings)

shapes = [Circle(5), Square(10), Triangle(10, 5)]

for shape in shapes:
    print(shape.area())

pizza = Pizza(5, ['cheese', 'pepperoni', 'mushrooms'])
print(pizza.area())