# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 10:53:58 2024

@author: suraj
"""

#Python for Data Science
#What is Pandas DataFrame?
#pandas DataFrame is a Two-Dimensional data structure, an immutable, heterogeneous tabular data structure with labeled axes rows, and columns.
'''
#DataFrame Features
1)	DataFrames support named rows & columns.
2)	you can also provide names to rows.
3)	Supports heterogeneous collections of data.
4)	DataFrame labeled axes (rows and columns).
#Installing Pandas
1)	step-1 go to anaconda navigator
2)	step-2 select environment tab
3)	step-3 by default it will be base terminal
4)	step-4 on base terminal-pip install pandas
5)	Or conda install pandas
'''
######################################
#Upgrade Pandas to Latest or Specific Version on base terminal write :-conda install --upgrade pandas

#upgrade to specific version:-conda update pandas==1.5.3
#Note :- Do not install the spyder  on c Drive

#********************operation on DataFrame*************************
#To check the version of pandas
import pandas as pd
pd.__version__
#o.p:- 1.5.3

#########################################################
# Create pandas DataFrame Create using Construct. Create pandas DataFrame from List
import pandas as pd
technologies = [ ["Spark",20000, "30days"], 
                 ["pandas",20000, "40days"], 
               ]
df=pd.DataFrame(technologies		) #D and F in the DataFrame are in the capital letter always
print(df)
'''#o.p:-       	 0     	 1    	   	2		#by default the row and column index are given
0 	  Spark  	20000  	30days
1  	 pandas  	20000 		 40days
'''
####################################################
#check the size of the data frame
df.size 		#o.p:-6(it can give the number of element in the dataframe)
###################################################
#Note1:-Since we have not given labels to columns and indexes, DataFrame by default assigns incremental sequence numbers as labels to both rows and columns, these are called Index.

###################################################
# Add Column & Row Labels to the DataFrame
column_names=["Courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)

'''#o.p:-  		Courses    	Fee 		Duration
a  	 	Spark  		20000   	30days
b 	 	pandas  	20000   	40days
'''
####################################################
#Check the data type of the dataframe element 
df.dtypes 
'''#o.p:- Courses     object
Fee          int64
Duration    object
dtype: object
'''
##################################################
#You can also assign custom data types to columns. set custom types to DataFrame
types={'Courses': str,'Fee':float,'Duration':str}
df.dtypes	#o.p:- the data type will be change

####################################################
# Create DataFrame from Dictionary
technologies = {
    'Courses':["Spark","PySpark","Hadoop"],
    'Fee' :[20000,25000,26000],
    'Duration':['30day','40days','35days'],
    'Discount':[1000,2300,1500]
              }
df = pd.DataFrame(technologies)
df
# Quick Examples of Converting Data Types in Pandas
# Convert all types to best possible data types
df2=df.convert_dtypes()
print(df2.dtypes)
'''#o.p:- 
Courses       string
Fee            Int64
Duration      string
Discount     Float64
dtype: object
'''
#######################################################
# Change All Columns to Same data type
df = df.astype(str)
print(df.dtypes)
'''#o.p:- 
Courses      object
Fee          object
Duration     object
Discount     object
dtype: object
'''
#######################################################
# Change data Type For One or Multiple Columns
df = df.astype({"Fee": int, "Discount": float})
print(df.dtypes)
'''#o.p:-
Courses       object
Fee            int32
Duration      object
Discount     float64
dtype: object
'''
#####################################################
# Convert Data Type for All Columns in a List
df = pd.DataFrame(technologies)
df.dtypes
cols = ['Fee', 'Discount']
df[cols] = df[cols].astype('float')
df.dtypes
'''#o.p:- 
Courses       object
Fee          float64
Duration      object
Discount     float64
dtype: object
'''
#####################################################
#Ignores error
df = df.astype({"Courses": int},errors='ignore')
df.dtypes
'''#o.p:- 
Courses       object
Fee          float64
Duration      object
Discount     float64
dtype: object
'''
######################################################
# Generates error
df = df.astype({"Courses": int},errors='raise')
#o.p:- Error raise

#####################################################
# Converts feed column to numeric type
df = df.astype(str)
print(df.dtypes)
df['Discount'] = pd.to_numeric(df['Discount'])
df.dtypes
'''#o.p:- 
Courses      object
Fee          object
Duration     object
Discount     object
dtype: object
Out[18]: 
Courses       object
Fee           object
Duration      object
Discount     float64
dtype: object  
'''
######################################################
#convert dataframe to csv
df.to_csv('data_file.csv')

#######################################################
# Create DataFrame from Dictionary
technologies = {
    'Courses':["Spark","PySpark","Hadoop"],
    'Fee' :[20000,25000,26000],
    'Duration':['30day','40days','35days'],
    'Discount':[1000,2300,1500]
              }
df = pd.DataFrame(technologies)
df

##################################################


#Create DataFrame From CSV File
df = pd.read_csv('data_file.csv')
#o.p:- The csv  file is created and the dataframe are stored in it 
#################################################
#Create DataFrame From CSV File
df = pd.read_csv('data_file.csv')
df
'''#o.p:- 
0 	 	Courses    	Fee 		Duration  		Discount
0           0    	Spark  		20000    	30day      		1000
1           1  	PySpark 	 25000   	40days     		 2300
2           2  	 Hadoop  	26000   	35days      		1500

'''