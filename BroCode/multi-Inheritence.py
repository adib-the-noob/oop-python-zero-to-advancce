class Prey:
    def flee(self):
        print("This is the flee method of Prey class")

class Predator:
    def hunt(self):
        print("This is the hunt method of Predator class")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()

fish.flee()
fish.hunt()