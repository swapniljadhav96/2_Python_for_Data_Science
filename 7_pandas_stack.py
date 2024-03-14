# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:42:47 2024

@author: suraj
"""

#**DataFrame - stack() function
'''The stack() function is used to stack the prescribed level(s) from columns to index.
Return a reshaped DataFrame or Series having a multi-level index with one or more new inner-most levels compared to the current DataFrame. The new inner-most levels are created by pivoting 
 the columns of the current dataframe:    if the columns have a single level, the output is a Series;    if the columns have multiple levels, the new index level(s) is (are) taken from the  prescribed level(s) and the output is a DataFrame. 
'''
################################
#Write a Pandas program to sort a given Series. 
import pandas as pd
s = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s)
''' 0       100
1       200
2    python
3    300.12
4       400
dtype: object'''
new_s = pd.Series(s).sort_values()
print(new_s)
'''
‘’’ 0       100
1       200
3    300.12
4       400
2    python
dtype: object’’’’’’’
'''
###################################################
#Write a Pandas program to add some data 
#to an existing Series. 
import pandas as pd
s = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s)
''' 0       100
1       200
2    python
3    300.12
4       400
dtype: object’’’
'''
print("\nData Series after adding some data:")
new_s = pd.concat([s, pd.Series([500, "php"])], ignore_index=True)
print(new_s)
''' 0       100
1       200
2    python
3    300.12
4       400
5       500
6       php
dtype: object’’’
'''
####################################
#Write a Pandas program to change the order of index
# of a given series.
'''
Sample Output:
Original Data Series:
A    1
B    2
C    3
D    4
E    5
dtype: int64
Data Series after changing the order of index:
B    2
A    1
C    3
D    4
E    5
dtype: int64

'''
import pandas as pd
s = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C','D','E'])
print("Original Data Series:")
print(s)
s = s.reindex(index = ['B','A','C','D','E'])
print("Data Series after changing the order of index:")
print(s)
