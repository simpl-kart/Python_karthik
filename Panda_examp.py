import pandas
import numpy
arr = numpy.array([9,8,8,6,5,3])
series = pandas.Series(arr)
print series
##getting the part of the array using slicing from the series

listx = [1,2,3,4,5,6,7]
tabl = pandas.DataFrame(listx) ###converting a sample list into Dataframe
print tabl
data_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5}
series = pandas.Series(data_dict)
print series[2:4] # starts from 2 and ends before 4 so 2 and 3 rows of dictionary will be selected

dictx = [{'a':1,'b':2},{'a':5,'b':10},{'a':50,'b':100,'c':200}]
table = pandas.DataFrame(dictx,index=['first','second','third']) #index will be automatically taken as 0,1,2
print table

### Converting a dictionary of series into a Dataframe
dataseries = {'Karthik':pandas.Series([1,2,3],index=['Maths','Physics','Chemistry']),'Rejith':pandas.Series([3,4,5,6],index=['Maths','Physics','Chemistry','Bio'])}
table1 = pandas.DataFrame(dataseries)
print table1
table1['Lekshmi']= pandas.Series([10,11],index=['Chemistry','Maths'])
print table1

del(table1['Lekshmi'])
print table1
print table1.loc['Maths']
print table1.pop('Karthik')
print table1
#####append a row
table1=table1.append(pandas.DataFrame([[30]], columns=['Rejith']))
print table1

#####deleting a row
print table1.drop(0)
####read from csv and write to csv file

tablexl = pandas.read_csv('panda_dataset.csv')
print tablexl
table1.to_csv('panda_dataset.csv')




