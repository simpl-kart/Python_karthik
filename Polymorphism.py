class Animal:
    def __init__(self):
        pass
    def talk(self):
        pass
class Dog(Animal):
    def talk(self):
        print("dog bark")

class Cat(Animal):
    def talk(self):
        print("Meow")

d=Dog()
d.talk()
c=Cat()
c.talk()


