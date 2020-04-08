
########################Classic Example of a single level inheritance
class baseclass:
    def fun(self):
        print("this is base class")
class subbaseclass(baseclass):
    pass
    # def fun(self):
    #     print("this is subbaseclass")
ob=subbaseclass()
ob.fun()

###################Multiple Inheritance##################################

class firstClass(object):
    def __init__(self):
        print("this is first class")

class secondClass(object):
    def __init__(self):
        super(secondClass, self).__init__()
        print("this is second class")

class thirdClass(secondClass,firstClass):
    def __init__(self):
        super(thirdClass, self).__init__()
        print("this is third class")
thirdClass()

##################Multilevel Inheritance####################################

class Animal:
    def eat(self):
        print("Eating....")

class Dog(Animal):
    def bark(self):
        print("Barking....")

class Babydog(Dog):
    def weep(self):
        print("Weeping")

d=Babydog()
d.eat()
d.bark()
d.weep()

###############################################################################



