# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:15:48 2024

@author: suraj
"""

#practice of the C:\Data Science\1-python
import pandas as pd
df=pd.read_csv("C:/Data Science/1-python/Diabetes.csv")
df

#check the data type
df.dtypes

#check the size
df.size

#########
#convert the dtype
df=df.convert_dtypes()
df.dtypes

##############
# Apply as type
df=df.astype(str)
df.dtypes
#################
#convert the particular column data type
df = df.astype({" Age (years)": float, " Number of times pregnant": float})
print(df.dtypes)

################
df = df.astype(str)
df.dtypes
#convert the all rows data type using the column name
'''cols=[ 'Number of times pregnant',' Plasma glucose concentration',
      ' Diastolic blood pressure', 'Triceps skin fold thickness',
         '2-Hour serum insulin',' Body mass index ',
         ' Diabetes pedigree functio',' Age (years)'] 
df[cols] = df[cols].astype('string')
df.dtypes'''
###################
#ignore error
df = df.astype({" Age (years)": int},errors='ignore')
df.dtypes
#####################
#raise error
df = df.astype({" Number of times pregnant": int},errors='raise')
df
############################
#DataFrame properties
df.shape

df.size

df.columns

df.columns.values

df.index
###############################
#Accessing one column contents
df[' Age (years)']
###############################
##Accessing two columns contents
df[[' Diabetes pedigree function',' Age (years)']]

#select certain rows and assign it to another dataframe
df2=df[6:]
df2

# Accessing certain cell from column
df[' Age (years)'][4]

# Substracting specific value from column
df = df.astype({" Age (years)": float})
print(df.dtypes)
df[" Age (years)"]=df[" Age (years)"] -10
df

###############################
# Describe DataFrame for all numberic columns
df.describe()
##########################
#  Rename column 

df2 = df.rename({' Age (years)': 'age', ' Number of times pregnant': 'number'}, axis='columns')
df2
df2 = df.rename(columns={' Number of times pregnant': 'Number', ' Age (years)': 'Age'})
df2
df=df.rename(columns={' Number of times pregnant': 'Number', ' Age (years)': 'Age'},inplace=True)
df

######################

# Drop DataFrame rows
df1=df.drop(df.index[1])

df1=df.drop(df.index[1])
df1

df1=df.drop(df.index[[1,3]])
df1

# Delete Rows by Index Range
df1=df.drop(df.index[23:])
df1

# Drop column by names
df1=df.drop([' Diabetes pedigree function'],axis=1)
df1

# Labels
df1=df.drop(labels=[' Diabetes pedigree function'],axis=1)
df1

# columns
df1=df.drop(columns=[' Diabetes pedigree function'],axis=1)
df1

# Drop Column by index
df.drop(df.columns[1],axis=1)
df

# Drop from Df 
# inplace used for main ope on df
df.drop(df.columns[[2]],axis=1,inplace=True)
df

# Drop two or more columns

lisCol = [" Diabetes pedigree function"," 2-Hour serum insulin"]
df2=df.drop(lisCol, axis = 1)
print(df2)

# Drop two or columns by index

df2=df.drop(df.columns[[0,1]],axis=1)

# Drop multiple column
lisCol = [" Diabetes pedigree function"," 2-Hour serum insulin"]
df2=df.drop(lisCol, axis = 1)
print(df2)

#Remove columns From DataFrame inplace
df.drop(df.columns[1], axis = 1, inplace=True)
df


df2=df.iloc[:, 0:2]
df2

df2=df.iloc[0:2, :]
df2

#The second slice [:] indicates that all columns are required.

#Slicing Specific Rows and Columns using iloc attribute
df3=df.iloc[1:2, 1:3]
df3
#Another example
df3=df.iloc[:, 1:3]
df3
#The second operator [1:3] yields columns 1 and 3 only.
# Select Rows by Integer Index
df2 = df.iloc[2]
df2


df2 = df.iloc[[2,3,6]]  
df2
df2 = df.iloc[1:5] 
df2
df2 = df.iloc[:1]
df2    
df2 = df.iloc[:3]    

df2 = df.iloc[-3:]
   
df2 = df.iloc[::2]   

# Select Rows by Index Labels
df2 = df.loc[1]   
df2     
df2 = df.loc[[2,3,6]]  
df2  

df2 = df.loc[1:5]    
df2

df2 = df.loc[1:5]
df2 = df.loc[1:5:2]   
df2
##########################################

#Select Rows by Index using Pandas iloc[]
#Select Row by Integer Index

print(df.iloc[2])

# Select Rows by Index List
print(df.iloc[[2,3,6]])


# Select Rows by Integer Index Range
print(df.iloc[1:5])

# Select First Row by Index
print(df.iloc[:1])


# Select First 3 Rows
print(df.iloc[:3])


# Select Last Row by Index
print(df.iloc[-1:])


print(df.iloc[-3:])


df2=df[" Diabetes pedigree function"]
df2

## select multiple columns
df2 = df[[" Diabetes pedigree function"," 2-Hour serum insulin"] ]
df2

# Using loc[] to take column slices
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]
## Selecte multiple columns

df2 = df.loc[:,[" Diabetes pedigree function"," 2-Hour serum insulin"]]
df2

# Select Random columns 

df2 = df.loc[:, [" Diabetes pedigree function"," 2-Hour serum insulin"]]
df2
