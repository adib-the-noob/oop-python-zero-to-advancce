class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("Bark")
        
class Cat(Animal):
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()
    
    