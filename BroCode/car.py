class Car:
    
    wheels = 4 # this is a class variable, it can be accessed outside the class
    
    def __init__(
        self,
        model, # these are called instance variables 
        year, # these cant be accessed outside the class
        color, 
        for_sale,
    ):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f'{self.model} is driving')
        
    def stop(self):
        print(f'{self.model} is stopping')
