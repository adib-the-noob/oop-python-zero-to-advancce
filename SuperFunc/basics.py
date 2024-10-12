class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"Color: {self.color}, Is Filled: {self.is_filled}, width: {self.width if hasattr(self, 'width') else None}, height: {self.height if hasattr(self, 'height') else None}, radius: {self.radius if hasattr(self, 'radius') else None}, area: {self.area if hasattr(self, 'area') else None}")        

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        # self.color = color
        # self.is_filled = is_filled - this is not needed as it is already in the parent class
        super().__init__(color, is_filled)
        
        # the difference is the radius is not in the parent class
        self.radius = radius
        
    def describe(self):
        super().describe()
        print(f"Circle, The area is {3.14 * self.radius ** 2}")
        
        
class Square(Shape):
    def __init__(self, color, is_filled, width):
        # self.color = color
        # self.is_filled = is_filled
        super().__init__(color, is_filled)
        
        # the difference is the width is not in the parent class
        self.width = width
        
    def describe(self):
        super().describe()
        print(f"Square, The area is {self.width ** 2}")
        
class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        # self.color = color
        # self.is_filled = is_filled
        super().__init__(color, is_filled)
        
        # the difference is the width and height is not in the parent class
        self.width = width
        self.height = height
        
    def describe(self):
        super().describe()
        print(f"Triangle, The area is {0.5 * self.width * self.height}")
        
circle1 = Circle(color='red', is_filled=True, radius=5)

print(circle1.color)
print(circle1.is_filled)

print("sq")
square1 = Square(color='blue', is_filled=False, width=10)
print(square1.color)
print(square1.is_filled)

square1.describe()
circle1.describe()