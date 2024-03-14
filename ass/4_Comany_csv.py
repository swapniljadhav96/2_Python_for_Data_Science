# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:27:50 2024

@author: suraj
"""


"""-----------------------------assigmaent ------------------------"""
import pandas as pd
import numpy as np

df = pd.read_csv("C:/Data Science/1-python/Company_Data.csv")
df

#Get the number of Rows in the df 
rows_count = len(df.index) 
print(rows_count)

rows_count = len(df.axes[0])
print(rows_count)

rows_count = df.shape[0]
print(rows_count)

#Applying function on the columns of a DataFrame
def mod_100(x):
    return x%100
print(df['Sales'])

df1 = df['Income'].apply(mod_100)
print(df1)

df2 = df[['CompPrice','Population']].apply(mod_100)
df2
#using lambda function 
df3 = df['Education'].apply(lambda Age:Age+10)
df3
#Instead of apply we can also use transform
df0 = df['Age'].transform(mod_100)
df0
#using df.map() to single column
df['Age'] = df['Age'].map(lambda Age:Age+5)
print(df['Age'])

#using numpy function to a single column through pandas
df['Sales'] = df['Sales'].apply(np.square)
df['Sales']

df = np.square(df['Sales'])
df
#use groupby to complete the sum()
df = pd.read_csv("C:/Data Science/1-python/Company_Data.csv")
df
df4 = df.groupby(['ShelveLoc']).sum()
df4