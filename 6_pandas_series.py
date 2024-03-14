# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:37:04 2024

@author: suraj
"""

#**pandas series**
'''Series
	Module pandas series
	Work on column use series
	Work on dataframe use dataframe
	It has no column name and it dose not have index it hash exclibility index value
	A series  is used to module one-dimension data(column)
	It is similar to the list In python but not a list
	The series object also has a few more bits of data including an index and rows it has no built in index but it has exclisitive index are available
	NULL value then drop or replace 
	Rows increases  model have the higher performance
	Rows decreases model have low performance
	NAN is dangerous
	NAN value stands for not a null number and is usually ignored in arithematic
	Operation are similar to NULL in sql
	If you load data from csv file an apply the value otherwise that value  you can replace otherwise drop that value
	Series has duplicate value
	The series data structure provides the support for basic CRUD operation  create, read, update, delete
	A series  is used to model one dimensional data similar to a list in python the series object also has a few more bits of the data including an #index and name
'''
import pandas as pd
songs2=pd.Series([334,355,54,76],name='counts')
songs2
#it is esay to inspect the index of a series (or data frame)
songs2.index
songs2
""" it give the  index value by default
Out[30]: 
0    334
1    355
2     54
3     76
Name: counts, dtype: int64"""

##########################################################
#assign index as the index can be string based as well in which case pandas indicates that the datatype for the index is object (not string):
songs3=pd.Series([334,355,54,76],name='counts',
                index=['paul','john','ingo','tipa'])
songs3.index				#intialise
#it give the index to counts column i.e. index
songs3
"""Out[28]: 
paul    334
john    355
ingo     54
tipa     76
Name: counts, dtype: int64"""

####################################################
#the nan valuestands for 
#numeric column will become  nan/null
import pandas as pd
f1=pd.read_csv("C:/Data Science/1-python/courses.csv")
f1
#finding the mean value
import pandas as pd
songs = pd.Series([145,25,36,78],name = 'count')
songs
#It is easy to inspect the index of a series(or a dataframe)
songs.index
#the index non be string bases as well,in which case pandas indicates  that the datatype for the index is object (not string):

songs3 = pd.Series([154,35,41,26,47],name='count',index=['Arijit','Honey','Atif','Shreya','Ajay'])
songs3

#NaN - it is generally ignored in arithmetic operation the series object behaves similarly to a numpy array
songs3.mean()
songs3

#################################################
##pandas series Data structure provides the support for the CRUD operation
#creation
george=pd.Series([23,45,54,7],
                 index=['3245','5665','5646','5465'],
                 name='George songs')
george

##############################################
#reading:-to read  or select the data frame a series
george['3245']
george['5665']
#it can show the index value which has the value assign to it and show that value
# we can iterate over in 
for item in george:
    print(item)
'''#o.p:-23
    45
    54
    7'''
    # it shows only value

############################################################
#updateing
#updating the value sin series little trickle as well as to update the value
george['3245']=68
george=['3245']
george['3245']

#########################################################
#deletion
# the del statement appers to have problem with duplicatae value index
s=pd.Series([2,3,4],index=[1,2,3])
del s[1]
s

#########################################################
# converrt types
#string use .astype(str)
#numeric use pd.numeric
#innteger use .astype(int)
# note a
#
import pandas as pd
songs_66=pd.Series([3,None,11,9],
                   index=['a','s','d','f'],
                   name='Counts')

pd.to_numeric(songs_66.apply(str))
#ther will be error
#that error can be solve by uing the errors='coerce'

pd.to_numeric(songs_66.apply(str),errors='coerce')
#it can remove the error occur in teh series 
#dealing with none

################################################



#dealing with none
songs_66.fillna[-1]
#drop the null data 
songs_66.dropna()

###############################################
#append combine and joining the tow series
import pandas as pd
songs_69=pd.Series([7,56,34,1],
                   index=['aa','ss','dd','ff'],
                   name='Counts')
#the concactnet  the tow series together we use simply append()
songs=songs_66.append(songs_69)

####pandas series opertion
#Write a Pandas program to create and display a one-dimensional array-like object 
#containing an array of data.
import pandas as pd
ds = pd.Series([2, 4, 6, 8, 10])
print(ds)

###################################################
#Write a Pandas program to convert a Panda module Series
# to Python list and it’s type.
import pandas as pd
ds = pd.Series([2, 4, 6, 8, 10])
print("Pandas Series and type")
print(ds)
print(type(ds))
print("Convert Pandas Series to Python list")
print(ds.tolist())
print(type(ds.tolist()))

#######################################################
#Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
#Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
print("Add two Series:")
print(ds)
'''0     3
1     7
2    11
3    15
4    19
dtype: int6'''
print("Subtract two Series:")
ds = ds1 - ds2
print(ds)
''' 0    1
1    1
2    1
3    1
4    1
dtype: int64'''
print("Multiply two Series:")
ds = ds1 * ds2
print(ds)
'''0     2
1    12
2    30
3    56
4    90
dtype: int64'''
print("Divide Series1 by Series2:")
ds = ds1 / ds2
print(ds)
''' 0    2.000000
1    1.333333
2    1.200000
3    1.142857
4    1.111111
dtype: float64’’’’
'''
####################################################################
#Write a Pandas program to compare the elements of the two Pandas Series.
#Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])
print("Series1:")
print(ds1)
''' 0     2
1     4
2     6
3     8
4    10
dtype: int64’’’’
'''
print("Series2:")
print(ds2)
''' 0     1
1     3
2     5
3     7
4    10
dtype: int64'''
print("Compare the elements of the said Series:")
print("Equals:")
print(ds1 == ds2)
''' 0    False
1    False
2    False
3    False
4     True
dtype: bool’’’’
'''
print("Greater than:")
print(ds1 > ds2)
''' 0     True
1     True
2     True
3     True
4    False
dtype: bool’’’’
'''
print("Less than:")
print(ds1 < ds2)
''' 0    False
1    False
2    False
3    False
4    False
dtype: bool’’’’’
'''
#######################################################
#Write a Pandas program to convert a dictionary to a Pandas series.
#Original dictionary:{'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
import pandas as pd
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
print("Original dictionary:")
print(d1)		#{'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
new_series = pd.Series(d1)
print("Converted series:")	
print(new_series)
''' a    100
b    200
c    300
d    400
e    800
dtype: int64’’’’’
'''
####################################
#Write a Pandas program to convert a NumPy array to a Pandas series. 
import numpy as np
import pandas as pd
n_a = np.array([10, 20, 30, 40, 50])
print("NumPy array:")
print(n_a)		# [10 20 30 40 50]
new_series = pd.Series(n_a)
print("Converted Pandas series:")
print(new_series)
''' 0    10
1    20
2    30
3    40
4    50
dtype: int32’’’’
'''
########################################
#Write a Pandas program to change the data type of given a column or a Series. 
'''
Sample Series:
Original Data Series:
0 100
1 200
2 python
3 300.12
4 400
dtype: object
Change the said data type to numeric:
0 100.00
1 200.00
2 NaN
3 300.12
4 400.00
dtype: float64
'''
import pandas as pd
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s1)
print("Change the said data type to numeric:")
s2 = pd.to_numeric(s1, errors='coerce')
print(s2)
#######################################3
#Write a Pandas program to convert 
#the first column of a DataFrame as a Series. 
import pandas as pd
d = {'col1': [1, 2, 3, 4, 7, 11],
     'col2': [4, 5, 6, 9, 5, 0], 
     'col3': [7, 5, 8, 12, 1,11]
     }
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
s1 = df.iloc[:,0]
print("\n1st column as a Series:")
print(s1)
print(type(s1))

###################################
import pandas as pd
s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
print("Original Series of list")
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True)
print("One Series")
print(s)
