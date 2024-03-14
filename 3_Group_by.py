# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:20:29 2024

@author: suraj
"""

#Pandas groupby()  
'''groupby is used for grouping the data according to the categories and applying a function to the categories. It also helps to aggregate data efficiently. The Pandas groupby() is a very powerful function with a lot of variations. It makes the task of splitting the Dataframe over some criteria really easy and efficient.
 Pandas dataframe.groupby() function is used to split the data into groups based on some criteria
'''
#With Examples 

import pandas as pd
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
    'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
          })
df = pd.DataFrame(technologies)
print(df)
'''o.p:- Courses    Fee Duration  Discount
0    Spark  22000   30days    1000.0
1  PySpark  25000   50days    2300.0
2   Hadoop  23000   55days    1000.0
3   Python  24000   40days    1200.0
4   Pandas  26000   60days    2500.0
5   Hadoop  25000   35days       NaN
6    Spark  25000   30days    1400.0
7   Python  22000   50days    1600.0
8       NA   1500   40days       0.0'''

##################################################
# Use groupby() to compute the sum
df2 =df.groupby(['Courses']).sum()
print(df2)
'''o.p:-    
Courses                  Fee  Discount     
Hadoop   	48000    1000.0
NA        	1500       0.0
Pandas   	26000    2500.0
PySpark  	25000    2300.0
Python   	46000    2800.0
Spark    	47000    2400.0'''

######################################################


# Group by multiple columns
df2 =df.groupby(['Courses', 'Duration']).sum()
print(df2)
'''o.p:-                   
Courses	 Duration      Fee  Discount           
Hadoop  	35days    25000       0.0
       		 55days    23000    1000.0
NA  		    40days     1500       0.0
Pandas  	60days    26000    2500.0
PySpark 	50days    25000    2300.0
Python  	40days    24000    1200.0
        		50days    22000    1600.0
Spark   	30days    47000    2400.0'''

#####################################################
#Add Index to the grouped data
# Add Row Index to the group by result
df2 = df.groupby(['Courses','Duration']).sum().reset_index()
print(df2)
'''o.p:-
Courses 	Duration    Fee 	 Discount
0   Hadoop   		35days  25000       0.0
1   Hadoop   		55days  23000    1000.0
2       NA   		40days   1500       0.0
3   Pandas   		60days  26000    2500.0
4  PySpark   		50days  25000    2300.0
5   Python   		40days  24000    1200.0
6   Python   		50days  22000    1600.0
7    Spark   		30days  47000    2400.0'''

######################################################
# Group by on multiple columns
df2 =df.groupby(['Courses', 'Duration']).sum()
print(df2)
'''o.p:-                
Courses 	Duration	Fee  Discount         
Hadoop  	35days    25000       0.0
        		55days    23000    1000.0
NA      		40days     1500       0.0
Pandas  	60days    26000    2500.0
PySpark 	50days    25000    2300.0
Python  	40days    24000    1200.0
        		50days    22000    1600.0
Spark   	30days    47000    2400.0'''

#######################################################
#Pandas Get Column Names from DataFrame
import pandas as pd
import numpy as np

technologies= {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee' :[22000,25000,23000,24000,26000],
    'Duration':['30days','50days','30days', None,np.nan],
    'Discount':[1000,2300,1000,1200,2500]
          }
df = pd.DataFrame(technologies)
print(df)
'''o.p:-  Courses    Fee Duration  Discount
0    Spark  22000   30days      1000
1  PySpark  25000   50days      2300
2   Hadoop  23000   30days      1000
3   Python  24000     None      1200
4   Pandas  26000      NaN      2500'''

########################################################
# Get the list of all column names from headers
column_headers = list(df.columns.values)
print("The Column Header :", column_headers)
#o.p:-The Column Header : ['Courses', 'Fee', 'Duration', 'Discount']

#########################################################
#Using list(df) to get the column headers as a list
column_headers = list(df.columns)
column_headers          #o.p:-['Courses', 'Fee', 'Duration', 'Discount']
#Using list(df) to get the list of all Column Names
column_headers = list(df)
column_headers
#o.p:-Out[59]: ['Courses', 'Fee', 'Duration', 'Discount']

