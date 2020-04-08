import sys
randomlist=['a',0,2]

for entry in randomlist:
    try:
        print("The entry is", entry)
        r=1/(entry)
        break
    except:
        print("Oops", sys.exc_info()[0],"occured")
        print("Next Entry")
        print()
print("The final of the",entry,"is",r)

