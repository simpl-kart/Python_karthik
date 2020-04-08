

######map actually maps each item in the list and what do you want the map to do

items = [1,2,3,4,5]
squared = map(lambda x:x**2, items)
cubed = map(lambda x:x**3, items)
print(squared)
print(cubed)

########map helps us avoid writing a function like below everytime for squaring a list

def square(items):
    r=[]
    for item in items:
        r.append(item**2)
    return r

###the function call should be below the definition, otherwise it's not working in python pls check later
print square([1,2,3,4])

##############Lambda filter ######filter will check each item in your list and apply a filter to it###########

number_list = range(-5,5)
less_than_zero = filter(lambda x:x<0, number_list)
print(less_than_zero)

from _functools import reduce


###########the calc
product_list = [1,2,3,4]
product = reduce(lambda x,y:(x**2)*y, product_list)
print product



