# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:15:51 2024

@author: suraj
"""

"""----------------------assigment ----------------------------"""
import pandas as pd
import numpy as np
df=pd.read_csv('boston_data.csv')
df
#access the file
############
#data type
df.dtypes
#########
#Convert the all in best data type
df2=df.convert_dtypes()
print(df2.dtypes)
##########
#change column in same data type
df2=df.astype(str)
print(df2.dtypes)
#########
df=pd.read_csv('boston_data.csv')
df.dtypes
#convert  the data types of column
colum=['crim','zn','indus']
df[colum]=df[colum].astype(int)
df.dtypes

########
#error ignore and generate
df=pd.read_csv('boston_data.csv')
df
###error ignore and generate
df=df.astype({'chas':float},errors='ignore')
df.dtypes
####genarate
df=df.astype({'chas':float},errors='raise')
df.dtypes
###############
#droping the row by label
df1=df.drop([1,2])
df1
##########
#droping the row by index
df1=df.drop(df.index[[2,3]])
df1

############
#delete by range
df1=df.drop(df.index[1:])
df1
###########
df=pd.read_csv('boston_data.csv')
df
#drop the particular row
df1=df.drop(3)
df1

#########
df=pd.read_csv('boston_data.csv')
df

#shape
df.shape
#size
df.size
#describe
df.describe
#access the one column
df['crim']
###################
#Accesing two column contents
df[['crim','zn']]
########################
#Select certain rows and assign it to another dataframe
df1 = df[3:16]
df1
###################
#Accessing certain cells from column
df['crim'][4]

#####################
#Rename
df1 = df.rename({'crim':'prise'},axis='columns')
df1
######################
#Drop DataFrame Rows and Columns
df.drop(index=3,columns='crim')
df

###################

#Deleting Rows by Index Range
df1 = df.drop(range(0,200))
df1
#####################
#Select Rows by Index
df2 = df[300:350]
df2
#####
#rename the column
df2=df.rename({'crim':'c','zn':'z','indus':'i'},axis='columns')
df2
###########
#drop the dataframe by using the row and column
df.drop(index=3,columns='crim')
#################
#select the all rows and only two column
df2=df.iloc[:,0:2]
df2
##############
#select the all column and only 2 rows
df2=df.iloc[0:2,:]
df2
#################
#select the row and column
df2=df.iloc[1:2,1:3]
df2
################
##select the alternative row
df2=df.iloc[::3]
df2
###############
#df[] notation
df2=df["crim"]
df2
###############
#select the column between two column
df2=df.loc[:,"crim":"indus"]
df2

##############
#query()
df2=df.query("crim == 2.73397")
df2
################
#not equal
df2=df.query("crim != 2.73397")
df2
