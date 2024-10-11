class Person:
    def __init__(self, name):
        self.name = name
        print("Hello, I am created!")

    def say_hi(self):
        print('Hello, my name is', self.name)


a = Person('Swaroop')
a.say_hi()
