class Animel:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f'{self.name} is eating')
        
    def sleep(self):
        print(f'{self.name} is sleeping')
        

class Dog(Animel):
    def speak(self):
        print(f'{self.name} is barking')

class Cat(Animel):
    def speak(self):
        print(f'{self.name} is meowing')

class Mouse(Animel):
    def speak(self):
        print(f'{self.name} is squeaking')

dog1 = Dog('Doggy')
cat1 = Cat('Catty')
mouse1 = Mouse('Mousy')


print(dog1.name,"-->", dog1.is_alive)
print(cat1.name,"-->", cat1.is_alive)
print(mouse1.name,"-->", mouse1.is_alive)

dog1.eat()
dog1.sleep()


cat1.sleep()
cat1.eat()


dog1.speak()
cat1.speak()
mouse1.speak()