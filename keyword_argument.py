#
# ##################below is the example for keyword argument where we need to give the keyword which calling the function and this is the recommended approach
# def keywordarg(a,b,c,d):
#     result = a*b + c*d
#     return result
#
# print keywordarg(a=1,b=2,c=3,d=4)
#
# ################default arguements
# def defaultarg(a,b,c,d=10):
#     result = a+b+c+d
#     return result
#
# print defaultarg(a=1,b=2,c=3)  #if d's value is passed the default value will be overridden
#
# #############variable length arguements
#
# def varlenarg(user, *users):
#     print ('first user argument:', user)
#     for x in users:
#         print 'user received from variable length arguments', x
#     return()
#
# varlenarg('karthik','rejith', 'lekshmi', 'sreeparu', 'sreedevi')

##########keyworded agrement example ......here we use **args

def myFunction(arg1, arg2, *arg3, **kwargs):
    print('First Normal Argument:', arg1)
    print ('Second Normal Argument:', arg2)
    print ('Non-keyworded Arguments:',  arg3)
    print ('keyworded argument' + str(kwargs))
    return
myFunction(1,2,3,4,5,6,7,name='karthik',age=32)