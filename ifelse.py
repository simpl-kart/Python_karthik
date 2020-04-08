X=20
Y=20
#indentation is very important in python... 4 lines from starting statement ... if it's ommitted it will not execute
if (X ==Y):
    X+=Y

    if (X >Y):
        print ("X and Y are equal")
        print(X)
    elif(X<Y):
        print("X is less than Y")
else:
    print("X and Y values are not correct")
