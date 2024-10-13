class Rectangle:
    def __init__(self, width, height):
        self._width = width # theser are meant to be private
        self._height = height 
        
    
    @property
    def width(self):
        return f"Width is {self._width}"
    
    
    @property
    def height(self):
        return f"Height is {self._height}"
    
rectanlge = Rectangle(10, 20)
print(rectanlge.width) # Width is 10 - printed by the property decorator