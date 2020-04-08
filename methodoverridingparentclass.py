
class Parent:

    def myMethod(self):
        print("this is parent class method")

class Child(Parent):
    def myMethod(self):
        print("this is child class method")

c=Child()
c.myMethod()
 #child class overridden method


######Another Example

class Rectangle():
    def __init__(self,length,breadth):   #The constructor is implemented using __init__(self) in this you can add parameters like how it's defined here
        self.length = length
        self.breadth = breadth
    def getArea(self):
        print(self.length*self.breadth, "is area of rectangle")

class Square(Rectangle):
    def __init__(self,side):
        self.side = side
    def getArea(self):
        print(self.side*self.side, "is the area of square")

s=Square(2)
r=Rectangle(2,2)
s.getArea()
r.getArea()



