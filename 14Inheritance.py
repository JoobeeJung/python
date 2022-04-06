# 14Inheritance.py
"""


"""

class Car:
    nation = "KOREA"
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print("Car created...")
    def printCar(self):
        print("(name, color, nation) = (",
              self.nation, ", ", self.name, ", ", self.nation, ")")

class SportsCar(Car):
    def __init__(self, name, color, turbo=True):
        super().__init__(name, color)
        self.turbo = turbo
        print("SportsCar Created")
    def printCar(self):
        print("(name, color, nation, turbo) = (",
              self.nation, ", ", self.name, ", ", self.nation,
              ", ", self.turbo, ")")

bmw = SportsCar("BMW", "RED", True)
bmw.printCar()