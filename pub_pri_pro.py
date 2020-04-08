class Sreedevi():
    def __init__(self):
        self.__pri=("I'm private")
        self.pub=("I'm public")
        self._pro=("I'm protected")

    def __privatemethod(self):
        print 'In private'

obj=Sreedevi()

print(obj.pub)

#####################Even though the convention
##############is to access protected method only within the class or a subclass. But python is flexible and allow developers to access it. But it's againsst
##########the standards

print(obj._pro)

#####################Even though the convention
##############is to access private method only within the class or a subclass. But python is flexible and allow developers to access it. But it's againsst
##########the standards

print obj._Sreedevi__pri
print obj._Sreedevi__privatemethod()
