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
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            raise ValueError("Width must be greater than 0")
    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            raise ValueError("Height must be greater than 0")
    
    @width.deleter
    def width(self):
        del self._width
        print("Width is deleted")
    
    @height.deleter
    def height(self):
        del self._height
        print("Height is deleted")
    
rectanlge = Rectangle(10, 20)


print(rectanlge.width) # Width is 10 - printed by the property decorator
rectanlge.width = 20
del rectanlge.width