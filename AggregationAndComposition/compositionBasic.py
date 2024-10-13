class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power 

class Wheel:
   def __init__(self, size):
       self.size = size
   
class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheel = [Wheel(wheel_size) for wheel in range(4)]
        
    def display_car(self):
        data = {
            'make': self.make,
            'model': self.model,
            'horse_power': self.engine.horse_power,
            'wheel_size': self.wheel[0].size
        }
        print(data)
    
car1 = Car(
    make='Toyota',
    model='Corolla',
    horse_power=100,
    wheel_size=15
)
car1.display_car()