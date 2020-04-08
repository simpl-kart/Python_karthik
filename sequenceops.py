# karlist = ['Angular', 'python', 'java']
#
# rejlist = karlist + ['dotnet', 'unix'] ###example for concatenation
# print rejlist
# print karlist[0:2] ###example for slicing
# print (rejlist * 2) ###example for repetition
# print ('python' in karlist) #membership testing and this returns true
# karlist[1]='nodejs' # how to update the list
# del(karlist[2]) #to delete teh elements in the list
# print karlist
# list1=[1,2,3,4,'a','b','c']
# print (list1.pop(3)) #returns the element at the given element
# print (list1.remove('a')) # removes the element from the list
# print type(list1)
# print len(list1)
# list1.insert(0,'karthik') #insert anything into the list. at the current index value will be inserted along with other elements in the list
# print (list1.sort()) #sort the list in alphabatical order
# print (sorted(karlist))
# print (list1[::-1]) #to print the list in reverse order
# print(list1)
# #A TUPLE INSIDE A LIST
#
# tuplelist = [(91,2,300),'Karthik', [1,2,3]]
# print tuplelist[2][0:2]
# ####append
# #
# cubelist = [x**3 for x in [1,2,3,4,5]]
# print cubelist
#
# #
# list1  = []  #userdefined list object
# for x in [1,2,3,4,5]:
#    list1.append(x**2)
#    print list1
# print list1
######################################rough work#########################
x=1
listdel = []
while (x <= 5):
    listdel.append(x**2)
    x+= 1
print listdel

listdel1 = []
listdel2 = [1,2,3,4,5,6]
#listdellen = len(listdel1)
for x in listdel2:
    listdel1.append(x**3)
print listdel1

listdel3 = []
for x in range(1,7):
    listdel3.append(x**4)
print listdel3


# #####################################rough work###########################
#
# #how to modify a tuple containing lists
# tuphaslist1 = ([1,2,3], [4,5,6], [7,8,9])
# tuphaslist1[0][0] = 'updated'
# print tuphaslist1
#########how to convert a tuple into a list update it and convert it back to tuple

tup1 = ('a','b','c')
lst= list(tup1)
lst[0] = 'karthik'
print lst

tup2 = tuple(lst)
print tup2

###############################string  in python ##############################
########python can either concatinate two numbers or two strings. not a string and a number###########################



