#animal age

class animal:
    def __init__(self, age):
        self.__age = age
    def setage(self, age):
        self.__age = age
    def getage(self):
        return self.__age
    def __add__(self, predict):
        return animal( self.__age + predict.__age )
    def __gt__(self, predict):
        return self.__age > predict.__age
 
 
animal1 = animal(10)
print(animal1.getage())
animal2 = animal(15)
print(animal2.getage())
animal3 = animal1 + animal2
print(animal3.getage())
print( animal3 > animal2) 
  