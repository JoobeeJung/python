#13Class.py
"""
public class Car
{
    필드...
    생성자
    메소드..
}
"""

class Car:
    color = str()

    def printCar(self):  # 파라미터가 없으면 안된다.!!
        print("color = ", self.color)

taxi = Car()
print(type(taxi))
taxi.color = "red"
taxi.printCar()

print("-" * 80)

class MyCar:
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def printMyCar(self):
        # (name, color, speed) = ( bmw, red, 30 )
        print("(name, color, speed) = (",
              self.name,
              ",", self.color,
              ", ",
              self.speed, ")")

bmw = MyCar("bmw", "red", 100)
bmw.printMyCar()
print(bmw)

print("-" * 80)

class Bus :
    nation = "KOREA"                    # class 변수
    def __init__(self, name, color):    # 인스턴스 변수
        self.name = name
        self.color = color

    def printBus(self):
        print("(name, color, nation) = (",
              self.name, ", ",
              self.color ,", " ,
              self.nation, ")")

bus1 = Bus('bus1', 'red')
bus2 = Bus('bus2', 'blue')
bus1.printBus()
bus2.printBus()

bus1.nation = "Japan"
bus1.printBus()
bus2.printBus()

print("-" * 80)
print("Share Memory")
print("-" * 80)

class Dog:
    tricks = []                 # 클래스 변수 : 인스턴스간 공유
    def __init__(self, name):
        self.name = name

    def addTrick(self, trick):
        self.tricks.append(trick)

puppy = Dog('puppy')
doge = Dog('doge')

puppy.addTrick("roll")
puppy.addTrick("bark")
print(doge.tricks)
doge.addTrick("sleep")
doge.addTrick("eat")

print(puppy.tricks)
print("******************")
print( Dog.tricks )

class BullDog:
    def __init__(self, name):
        self.name = name
        self.tricks = []            # 인스턴스

    def addTrick(self, trick):
        self.tricks.append(trick)

puppy = BullDog('puppy')
doge = BullDog('doge')

puppy.addTrick("roll")
puppy.addTrick("bark")
print(doge.tricks)
doge.addTrick("sleep")
doge.addTrick("eat")

print(puppy.tricks)
print(doge.tricks)

print( dir(BullDog) )       # dir() : 클래스 내부에 있는 객체 확인

class Truck :
    __nation = "KOREA"                    # 변수 장식
    def __init__(self, name, color):    # 인스턴스 변수
        self.name = name
        self.color = color

    def printTruck(self):
        print("(name, color, nation) = (",
              self.name, ", ",
              self.color ,", " ,
              self.__nation, ")")

    def setNation(self, nation):
        self.__nation = nation

truck = Truck("truck", "green")
truck.printTruck()
print(truck.name)
#print(truck.__nation)
truck.setNation("USA")
truck.printTruck()
