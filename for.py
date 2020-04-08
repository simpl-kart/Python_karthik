fruits = ["banana", "apple", "orange"]

for fruit in fruits:
    print(fruit)


list1=[1,2,3,'python']

for i in list1:
    print(i)

#break example

for i in range(1,12):
    if i ==5:
        break #skips 5 and come out of for loop
    else:
        print i

#continue example

for i in range(1,12):
    if i ==5:
        continue # skips 5 and prints rest
    else:
        print i

#pass can be used when we have a piece of code and nothing has be to done with it
for i in [1,2,3,4]:
     pass



#