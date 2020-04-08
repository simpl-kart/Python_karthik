class Constdestclass:
    def __init__(self):
        print("Constructor")
    # def __del__(self):      ###########Constructor and destructor are default and even if you didn't define it will activate when del obj is called
    #      print("Desctructor")

if __name__ =="__main__":
    obj = Constdestclass()
    # del obj   #######if del obj is activated, the obj"object" will directly deleted and th print statement will throw error
    print obj


#########Multiple constructors are required when you want to initialize the class in mutliple forms.. Example is copied in the notes "Python V2"

class Date:
    def __init__(self, year, month, day):
        self.year=year
        self.month=month
        self.day=day
        #print("init")

    @classmethod
    def dmy(cls,day,month,year):
        cls.year=year
        cls.month=month
        cls.day=day
        return cls(cls.year,cls.month,cls.day)
    @classmethod
    def mdy(cls,month,day,year):
        cls.year=year
        cls.month=month
        cls.day=day
        return cls(cls.year,cls.month,cls.day)
a=Date(1987,10,17)
print(a.year)
b=Date.dmy(17,10,1987)
print(b.month)
c=Date.mdy(10,17,1987)
print(c.day)
