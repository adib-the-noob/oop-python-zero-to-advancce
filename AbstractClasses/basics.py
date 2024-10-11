from abc import ABC, abstractmethod


class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    

class Car(Vehicle):
    def go(self):
        print("Car is moving")
        
    def stop(self):
        print("Car has stopped")
        
class Bike(Vehicle):
    def go(self):
        print("Bike is moving")
        
    # def stop(self):
    #     print("Bike has stopped")
        
bike = Bike()
bike.go()
# bike.stop()
