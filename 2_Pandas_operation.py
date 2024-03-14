# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:03:08 2024

@author: suraj
"""

#*************************Pandas DataFrame – Basic Operations******************
# Create DataFrame with None/Null to work with examples
import pandas as pd
import numpy as np
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies, index=row_labels)
print(df)
'''#o.p:-
Courses       	Fee 		Duration  		Discount
r0    	Spark  		22000.0    	30day      		1000
r1  	PySpark  	25000.0   	50days     		 2300
r2   	Hadoop  	23000.0   	55days      		1000
r3  	 Python  	24000.0   	40days      		1200
r4   	Pandas      	NaN   		60days      		2500
r5     	None  		25000.	0    	35day      		1300
r6    	Spark  		25000.0           			1400
r7  	 Python  	22000.0   	50days      		1600
'''
##################################################
#DataFrame properties
#shape of the dataframe
df.shape
#o.p:-(8, 4)

###############################################
#size of the dataframe
df.size
#o.p:-32

###################################################
#dataframe column and row information
df.columns		#o.p:- Index(['Courses', 'Fee', 'Duration', 'Discount'], dtype='object')
df.columns.values	#o.p:- array(['Courses', 'Fee', 'Duration', 'Discount'], dtype=object)
df.index			#o.p:-Index(['r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7'], dtype='object')
df.dtypes		
'''#o.p:- Courses      object
Fee         float64
Duration     object
Discount      int64
dtype: object
'''
#################################################
#Accessing one column contents
df['Fee']
'''#o.p:-
 0    20000
1    25000
2    26000
Name: Fee, dtype: int64
'''
########################################################
##Accessing two columns contents
df[['Fee','Duration']]
#o.p:- it give the two column data value

#########################################################
#select certain rows and assign it to another dataframe
df2=df[6:]
df2
'''#o.p:- 
Empty DataFrame
Columns: [Unnamed: 0, Courses, Fee, Duration, Discount]
Index: []
'''
######################################################
#accessing certain cell from column 'Duration'
df['Duration'][3]
#o.p:- '40days'

######################################################
#subtracting specific value from a column
df['Fee'] = df['Fee'] - 500
df['Fee']
'''#o.p:-
 r0    21500.0
r1    24500.0
r2    22500.0
r3    23500.0
r4        NaN
r5    24500.0
r6    24500.0
r7    21500.0
Name: Fee, dtype: float64
'''
#######################################################
#Pandas to Manipulate DataFrame
#Describe DataFrame:- It will show 5 number summary 
# Describe DataFrame for all numberic columns
df.describe()
'''#o.p:- Fee     Discount
count      7.000000     8.000000
mean   23214.285714  1537.500000
std     1380.131119   570.557372
min    21500.000000  1000.000000
25%    22000.000000  1150.000000
50%    23500.000000  1350.000000
75%    24500.000000  1775.000000
max    24500.000000  2500.000000
'''
####################################################
#rename() – Renames pandas DataFrame columns
df = pd.DataFrame(technologies, index=row_labels)
'''#o.p:-
Courses      	Fee		 Duration 	 Discount
r0    	Spark  		22000.0    	30day      	1000
r1  	PySpark  	25000.0   	50days      	2300
r2   	Hadoop  	23000.0   	55days     	1000
r3   	Python  	24000.0   	40days      	1200
r4   	Pandas      	NaN   		60days      	2500
r5     	None 		 25000.0    	35day      	1300
r6    	Spark  		25000.0               		1400
r7   	Python  	22000.0   	50days      	1600
'''
####################################################
# Assign new header by setting new column names.
df.columns=['A','B','C','D']
df
'''#o.p:- 
A       	 	B      	 	C    		 D
r0    		Spark  		22000.0  	 30days	 1000
r1  		PySpark  	25000.0  	50days 	 2300
r2   		Hadoop  	23000.0  	55days  	1000
r3   		Python  	24000.0  	40days  	1200
r4   		Pandas     	 NaN  		60days  	2500
r5     		None  		25000.0   	35day  	1300
r6    		Spark 		 25000.0         			 1400
r7   		Python 	 22000.0  	50days  	1600
'''
###########################################################
# Rename Column Names using rename() method
df = pd.DataFrame(technologies, index=row_labels)
df.columns=['A','B','C','D']
df2 = df.rename({'A': 'c1', 'B': 'c2'}, axis=1)
df2
'''#o.p:-		 c1      		 c2      		 C   		  D
r0    		Spark  		22000.0   	30days  	1000
r1  		PySpark 	 25000.0  	50days 	 2300
r2   		Hadoop  	23000.0  	55days  	1000
r3   		Python  	24000.0  	40days  	1200
r4   		Pandas      	NaN  		60days 	 2500
r5     		None  		25000.0   	35days		1300
r6    		Spark 		 25000.0          		1400
r7   		Python  	22000.0  	50days  	1600
'''
#######################################
#renaming the column by using the axis keyword 
df2 = df.rename({'C': 'c3', 'D': 'c4'}, axis='columns')
df2
'''#o.p:- 
A       	 	B     		 c3   		 c4
r0    		Spark  		22000.0   	30day  	1000
r1  		PySpark  	25000.0  	50days  	2300
r2   		Hadoop  	23000.0  	55days  	1000
r3   		Python  	24000.0  	40days  	1200
r4   		Pandas      	NaN  		60days  	2500
r5     		None  		25000.0   	35day  	1300
r6    		Spark  		25000.0          			1400
r7   		Python  	22000.0  	50days  	1600
'''
####################################################
df2 = df.rename(columns={'A': 'c1', 'B': 'c2'})
df2
'''#o.p:-
c1       		c2       		C     		D
r0    	Spark  		22000.0   	30day  	1000
r1  	PySpark  	25000.0  	50days  	2300
r2   	Hadoop  	23000.0  	55days  	1000
r3   	Python  	24000.0  	40days  	1200
r4   	Pandas      	NaN  		60days  	2500
r5     	None  		25000.0   	35day  	1300
r6   	 Spark  	25000.0          			1400
r7   	Python  	22000.0  	50days  	1600
'''
####################################################
#Drop DataFrame Rows and Columns
df = pd.DataFrame(technologies, index=row_labels)

# Drop rows by labels
df1 = df.drop(['r1','r2'])
df1
'''#o.p:-   	Courses      	Fee 		Duration  	Discount
r0   		Spark  		22000.0    	30day      	1000
r3  		Python  	24000.0   	40days      	1200
r4  		Pandas      	NaN   		60days      	2500
r5    		None  		25000.0    	35day      	1300
r6  		 Spark  	25000.0               		1400
r7 		 Python  	22000.0   	50days      	1600
'''
####################################################
# Delete Rows by position/index
df1=df.drop(df.index[1])
df1
'''#o.p:- Courses      	Fee 		Duration  		Discount
r0   Spark  		22000.0    	30day      		1000
r2  Hadoop  		23000.0   	55days      		1000
r3  Python  		24000.0   	40days      		1200
r4  Pandas      		NaN   		60days      		2500
r5    None  		25000.0    	35day      		1300
r6   Spark  		25000.0               			1400
r7  Python  		22000.0   	50days      		1600
'''
######################################################
df1=df.drop(df.index[[1,3]])
df1
'''#o.p:- Courses      	Fee 		Duration  		Discount
r0   Spark  		22000.0    	30day      		1000
r2  Hadoop  		23000.0   	55days      		1000
r4  Pandas      		NaN   		60days      		2500
r5    None  		25000.0    	35day      		1300
r6   Spark  		25000.0               			1400
r7  Python  		22000.0   	50days      		1600
'''
#####################################################
# Delete Rows by Index Range
df1=df.drop(df.index[2:])
df1
'''#o.p:- Courses      	Fee 		Duration  		Discount
r0    Spark  		22000.0   	 30day      		1000
r1  PySpark  		25000.0   	50days      		2300
'''
#############################################
# When you have default indexs for rows
df = pd.DataFrame(technologies)
df1 = df.drop(0)
df1
'''#o.p:- Courses      		Fee 		Duration  		Discount
1  PySpark  			25000.0   	50days      		2300
2   Hadoop  			23000.0   	55days      		1000
3   Python  			24000.0   	40days      		1200
4   Pandas      			NaN   		60days      		2500
5     None  			25000.0    	35day      		1300
6    Spark  			25000.0               			1400
7   Python  			22000.0   	50days      		1600
'''
####################################################
df = pd.DataFrame(technologies)
df1 = df.drop([0, 3])#it will delete row0 n row3
df1
'''
#o.p:- Courses      		Fee 		Duration 	 	Discount
1  PySpark  			25000.0   	50days      		2300
2   Hadoop  			23000.0   	55days      		1000
4   Pandas      			NaN   		60days      		2500
5     None  			25000.0    	35day      		1300
6    Spark  			25000.0               			1400
7   Python  			22000.0   	50days      		1600
'''
#########################################################
df1 = df.drop(range(0,2))#it will delete 0 and 1
df1
'''#o.p:- Courses     		Fee 		Duration  		Discount
2  Hadoop  			23000.0   	55days      		1000
3  Python  			24000.0   	40days      		1200
4  Pandas     			 NaN   		60days      		2500
5    None 			 25000.0    	35day      		1300
6   Spark  			25000.0               			1400
7  Python  			22000.0   	50days      		1600
'''
##############################################################
import pandas as pd
technologies = ({
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']
              })
df = pd.DataFrame(technologies)
print(df)
#get the dataframe in the row and column

####################################################
#Drop Column by Name
df2=df.drop(["Fee"], axis = 1)			# Drops 'Fee' column
print(df2)
#the fees column are drop from the dataframe

###################################################
# Explicitly using parameter name 'labels'
df2=df.drop(labels=["Fee"], axis = 1)
#it can drop the fees column

# Alternatively you can also use columns instead of labels.
df2=df.drop(columns=["Fee"], axis = 1)
#it can drop the fees column

###################################################
# Drop column by index.
print(df.drop(df.columns[1], axis = 1))
df = pd.DataFrame(technologies)

# using inplace=True
df.drop(df.columns[[2]], axis = 1, inplace=True)
print(df)

#############################################################
df = pd.DataFrame(technologies)
#Drop Two or More Columns By Label Name
df2=df.drop(["Courses", "Fee"], axis = 1)
print(df2)

##############################################################
#Drop Two or More Columns by Index
df = pd.DataFrame(technologies)
df2=df.drop(df.columns[[0,1]], axis = 1)
print(df2)

###########################################################
#Drop Columns from List of Columns
df = pd.DataFrame(technologies)
lisCol = ["Courses","Fee"]
df2=df.drop(lisCol, axis = 1)
print(df2)

############################################################
#Remove columns From DataFrame inplace
df.drop(df.columns[1], axis = 1, inplace=True)
df
# using inplace=True
############################################################
##Pandas Select Rows by Index (Position/Label)
import pandas as pd
import numpy as np
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies, index=row_labels)
print(df)
#**************************************
#**ILOC
#imp for the interview
iloc[]:- for the index
Syntax
df.iloc[startrow:endrow, startcolumn:endcolumn]
#############
#**loc**
loc[]:- for the label 

df = pd.DataFrame(technologies, index=row_labels)
# Below are quick example
df2=df.iloc[:, 0:2]
df2
#This line uses the slicing operator to get DataFrame items by index.
# The first slice [:] indicates to return all rows. 
#The second slice specifies that only columns between 0 and 2 (excluding 2) should be returned.

#############################################################
df2=df.iloc[0:2, :]
df2
#In this case, the first slice [0:2] is requesting only rows 0 through 1of the DataFrame.
#The second slice [:] indicates that all columns are required.

#############################################################
#Slicing Specific Rows and Columns using iloc attribute
df3=df.iloc[1:2, 1:3]
df3

#############################################################
#Another example
df3=df.iloc[:, 1:3]
df3
#The second operator [1:3] yields columns 1 and 3 only.
# Select Rows by Integer Index
#############################################################
#df2 = df.iloc[2]     # Select Row by Index
df2

############################################################
df2 = df.iloc[[2,3,6]]    # Select Rows by Index List and it can select the 2 ,3,6 row from the dataframe
df2 = df.iloc[1:5]   # Select Rows by Integer Index Range
df2 = df.iloc[:1]    # Select First Row
df2 = df.iloc[:3]    # Select First 3 Rows
df2 = df.iloc[-1:]   # Select Last Row
df2 = df.iloc[-3:]   # Select Last 3 Row
df2 = df.iloc[::2]   # Selects alternate rows

#############################################################
# Select Rows by Index Labels
df2 = df.loc['r2']          # Select Row by  Label
df2 = df.loc[['r2','r3','r6']]    # Select Rows by Index Label List
df2 = df.loc['r1':'r5']     # Select Rows by Label Index Range
df2 = df.loc['r1':'r5']     # Select Rows by Label Index Range
df2 = df.loc['r1':'r5':2]   # Select Alternate Rows with in Index La

##########################################################
import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','40days','35days','40days',np.nan,None,'55days'],
    'Discount':[1000,2300,1500,1200,2500,2100,2000]
               }
index_labels=['r0','r1','r2','r3','r4','r5','r6']
df = pd.DataFrame(technologies,index=index_labels)
print(df)
#Select Rows by Index using Pandas iloc[]
#Select Row by Integer Index

print(df.iloc[2])
'''# Outputs
Courses     Hadoop
Fee          26000
Duration    35days
Discount      1500
Name: r3, dtype: object
'''
####################################################

#Get Multiple Rows by Index List
# Select Rows by Index List
print(df.iloc[[2,3,6]])
'''# Outputs
  Courses    	Fee 		Duration  	Discount
r2  Hadoop  	26000  	 35days      	1500
r3  Python  	22000   	40days      	1200
r6    Java  	22000   	55days   	2000
'''
#####################################################
#Get DataFrame Rows by Index Range
# Select Rows by Integer Index Range
print(df.iloc[1:5])
'''# Output
Courses   	 Fee	 Duration  	Discount
r1  PySpark  		25000   40days      2300
r2   Hadoop  		26000   35days      1500
r3   Python  		22000   40days      1200
r4   pandas  		24000      NaN      2500
'''
################################################
# Select First Row by Index
print(df.iloc[:1])
'''# Outputs
   Courses    	Fee 	Duration 	 Discount
r0   Spark  	20000   30days      	1000
'''
#################################################
# Select First 3 Rows
print(df.iloc[:3])
'''# Outputs
    Courses    		Fee 		Duration  		Discount
r0    Spark  		20000   	30days      		1000
r1  PySpark  		25000   	40days      		2300
r2   Hadoop  		26000   	35days      		1500
'''
###################################################
# Select Last Row by Index
print(df.iloc[-1:])
'''# Outputs
 	Courses    	Fee 	Duration  	Discount
r6    	Java  		22000   55days      2000
'''
#######################################################
# Select Last 3 Row
print(df.iloc[-3:])
'''# Outputs
   Courses    	Fee 	Duration  	Discount
r4  pandas  	24000      NaN      2500
r5  Oracle  	21000     None      2100
r6    Java  	22000   55days      2000
'''
####################################################
# Selects alternate rows
print(df.iloc[::2])
'''# Output
   Courses    	Fee 	Duration  	Discount
r0   Spark  	20000   30days      1000
r2  Hadoop  	26000   35days      1500
r4  pandas  	24000      NaN      2500
r6    Java  	22000   55days  
'''
####################################################
#summary of all the code
# Select Rows by Integer Index Range
print(df.iloc[1:5])
'''# Output
   Courses    	Fee 	Duration  	Discount
r1  PySpark  	25000   40days      2300
r2   Hadoop  	26000   35days      1500
r3   Python 	 22000   40days      1200
r4   pandas  	24000      NaN      2500
'''
######################################################

# Select First Row by Index
print(df.iloc[:1])
'''# Outputs
   Courses    Fee 	Duration	  Discount
r0   Spark  	20000   30days      1000
'''
#######################################################
# Select First 3 Rows
print(df.iloc[:3])
'''# Outputs
    Courses    		Fee 	Duration  	Discount
r0    Spark  		20000   30days      1000
r1  PySpark  		25000   40days      2300
r2   Hadoop  		26000   35days      1500
'''
#######################################################
# Select Last Row by Index
print(df.iloc[-1:])
'''# Outputs
Courses    	Fee 	Duration  	Discount
r6    Java  	22000   55days      2000
'''
#####################################################
# Select Last 3 Row
print(df.iloc[-3:])
'''# Outputs
  Courses    		Fee 	Duration  	Discount
r4  pandas  		24000      NaN      2500
r5  Oracle  		21000     None      2100
r6    Java  		22000   55days      2000
'''
#########################################################
# Selects alternate rows
print(df.iloc[::2])
'''# Output
   Courses    	Fee 	Duration  	Discount
r0   Spark  	20000   30days      1000
r2  Hadoop  	26000   35days      1500
r4  pandas  	  24000      NaN      2500
r6    Java 	 22000   55days      2000
'''
#******************************************************************
#**loc[]**
# Using loc[] to take column slices
#loc[] syntax to slice columns  :-df.loc[:,start:stop:step]
## Selecte multiple columns

#Select Rows by Index Labels using Pandas loc[]
#Get Row by Label
# Select Row by Index Label
print(df.loc['r2'])
'''# Outputs
Courses     Hadoop
Fee          26000
Duration    35days
Discount      1500
Name: r2, dtype: object
'''
##################################################
#Get Multiple Rows by Label List
# Select multiple Rows by Index Label List
print(df.loc[['r2','r3','r6']])
'''# Outputs
    Courses    	Fee 	Duration  	Discount
r2  PySpark  	25000   40days      2300
r3   Hadoop  	26000   35days      1500
r6   Oracle  	21000     None      2100
'''
###################################################
#Get Rows Between Two Labels
# Select Rows by Label Index Range
print(df.loc['r1':'r5'])
'''# Outputs
Courses    	Fee 	Duration 	 Discount
r1  PySpark 	 25000   40days      2300
r2   Hadoop  	26000   35days      1500
r3   Python  	22000   40days      1200
r4   pandas  	24000      NaN      2500
r5   Oracle  	21000     None      2100
'''
##############################################
# Select Alternate Rows with in Index Labels
print(df.loc['r1':'r5':2])
'''# Outputs
Courses    	Fee 	Duration  	Discount
r1  PySpark  	25000   40days      2300
r3   Python  	22000   40days      1200
r5   Oracle  	21000     None      2100
'''
#####################################################
#Pandas Select Columns by Name or Index
# By using df[] Notation
df2=df['Courses']
## select multile columns
df2 = df[["Courses","Fee","Duration"]] 

###################################################
# Using loc[] to take column slices
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]
## Selecte multiple columns
df2 = df.loc[:, ["Courses","Fee","Duration"]]
# Select Random columns 
df2 = df.loc[:, ["Courses","Fee","Discount"]]
# Select columns between two columns 
df2 = df.loc[:,'Fee':'Discount'] 
## Select columns by range
df2 = df.loc[:,'Duration':] 
# Select columns by range 
#All the columns upto 'Duration'
df2 = df.loc[:,:'Duration']  
## Select every alternate column
df2 = df.loc[:,::2]          

#########################################################
#Pandas iloc[] to Select Column by Index or Position
#Select Multiple Columns by Index Position
# Selected by column position
df2 = df.iloc[:,[1,2,3]]
df2
'''Fee 	Duration  	Discount
r0  	20000   30days      1000
r1  	25000   40days      2300
r2  	26000   35days      1500
r3  	22000   40days      1200
r4  	24000      NaN      2500
r5  	21000     None      2100
r6  	22000   55days      2000
'''
######################################################
# Select between indexes 1 and 4 (2,3,4)
df2 = df.iloc[:,1:4]
df2
'''#Returns
     Fee 	Duration  	Discount
0  20000   30days      1000
1  25000   40days      2300
'''
####################################################
# Select From 3rd to end
df2 = df.iloc[:,2:]
df2
'''#Returns
  Duration  Discount   Tutor
0   30days      1000  Michel
1   40days      2300     Sam
'''
########################
 #Select First Two Columns
df2 = df.iloc[:,:2]
df2
'''#Returns
   Courses    Fee
0    Spark  20000
1  PySpark  25000
'''
########################################################
#Pandas.DataFrame.query() by Examples
# Query all rows with Courses equals 'Spark'
df2=df.query("Courses == 'Spark'")
print(df2)

######################################################
# not equals condition
df2=df.query("Courses != 'Spark'")
df2

#####################################################
#Pandas Add Column to DataFrame
import pandas as pd
import numpy as np

technologies= {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee' :[22000,25000,23000,24000,26000],
    'Discount':[1000,2300,1000,1200,2500]
          }

df = pd.DataFrame(technologies)
print(df)

########################################################
#Pandas Add Column to DataFrame
# Add new column to the DataFrame
tutors = ['Ram', 'sham', 'Ghansham', 'Ganesh', 'Ramesh']
df2 = df.assign(TutorsAssigned=tutors)
print(df2)

####################################################
# Add multiple columns to the DataFrame
MNCCompanies = ['TATA','HCL','Infosys','Google','Amazon']
df2 = df.assign(MNCComp = MNCCompanies,TutorsAssigned=tutors )
df2

#################################################
# Derive New Column from Existing Column
df = pd.DataFrame(technologies)
df2 = df.assign(Discount_Percent=lambda x: x.Fee * x.Discount / 100)
print(df2)

################################################


#Append Column to Existing Pandas DataFrame
# Add New column to the existing DataFrame
df = pd.DataFrame(technologies)
df["MNCCompanies"] = MNCCompanies
print(df)

################################################
# Add new column at the specific position
df = pd.DataFrame(technologies)
df.insert(0,'Tutors', tutors )
print(df)

#############################################
#Pandas Rename Column with Examples
import pandas as pd
technologies = ({
  'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
  'Fee' :[20000,25000,26000,22000,24000,21000,22000],
  'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']
              })
df = pd.DataFrame(technologies)
print(df.columns)

###########################################
#Pandas Rename Column Name Rename a Single Column 
df2=df.rename(columns = {'Courses':'Courses_List'})
print(df2.columns)

############################################
#Alternatively, you can also write the above statement by using axis=1 or axis='columns' Alternatively you can write above using axis, 
df2=df.rename({'Courses':'Courses_List'}, axis=1)
df2=df.rename({'Courses':'Courses_List'}, axis='columns')

################################################
#In order to change columns on the existing DataFrame without copying to the new DataFrame, you have to use inplace=True. Replace existing DataFrame (inplace). This returns None.
df.rename({'Courses':'Courses_List'}, axis='columns', inplace=True)
print(df.columns)

################################################
#Rename Multiple Columns
df.rename(columns = {'Courses':'Courses_List','Fee':'Courses_Fee', 
   'Duration':'Courses_Duration'}, inplace = True)
print(df.columns)
df.columns
##############################################
#Rename Columns with a List
column_names = ['Courses','Fee','Duration']
df.columns = column_names
print(df.columns)

#############################################
#Rename multiple columns with inplace
df.rename(columns = {'Courses':'Courses_List','Fee':'Courses_Fee', 
   'Duration':'Courses_Duration'}, inplace = True)
print(df.columns)

#################################################
#Quick Examples of Get the Number of Rows in DataFrame
rows_count = len(df.index)
rows_count
rows_count = len(df.axes[0])
rows_count

##############################################
df = pd.DataFrame(technologies)
row_count = df.shape[0		  # Returns number of rows
col_count = df.shape[1] 		 # Returns number of columns
print(row_count)
#Outputs - 4

#######################################
#Pandas Drop Rows From DataFrame
import pandas as pd
import numpy as np

technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python"],
    'Fee' :[20000,25000,26000,22000],
    'Duration':['30day','40days',np.nan, None],
    'Discount':[1000,2300,1500,1200]
               }

indexes=['r1','r2','r3','r4']
df = pd.DataFrame(technologies,index=indexes)
print(df)

########################################################



#pandas Drop Rows From DataFrame Examples
# Drop rows by Index Label
df = pd.DataFrame(technologies,index=indexes)
df1 = df.drop(['r1','r2'])
print(df1)

######################################################
# Delete Rows by Index Labels
df1 = df.drop(index=['r1','r2'])
df1

######################################################
# Delete Rows by Index Labels & axis
df1 = df.drop(labels=['r1','r2'])
df1 = df.drop(labels=['r1','r2'],axis=0)

########################################################
# Delete Rows by Index numbers
df = pd.DataFrame(technologies,index=indexes)
df1=df.drop(df.index[[1,3]])
print(df1)

#####################################################
# Delete Rows by Index Range
df = pd.DataFrame(technologies,index=indexes)
df1=df.drop(df.index[2:])
print(df1)

####################################################
#Delete Rows when you have Default Indexes
# Remove rows when you have default index.
df = pd.DataFrame(technologies)
df1 = df.drop(0)
df3 = df.drop([0, 3])
df4 = df.drop(range(0,2))

################################################
#Remove DataFrame Rows inplace
# Delete Rows inplace
df = pd.DataFrame(technologies,index=indexes)
df.drop(['r1','r2'],inplace=True)
print(df)

#################################################


#Drop Rows that has NaN/None/Null Values
# Delete rows with Nan, None & Null Values
df = pd.DataFrame(technologies,index=indexes)
df2=df.dropna()
print(df2)

###############################################
#Remove Rows by Slicing DataFrame
df2=df[4:]     # Returns rows from 4th row
df2=df[1:-1]   # Removes first and last row
df2=df[2:4]    # Return rows between 2 and 4

##############################################
#Change All Columns to Same type in Pandas
#df.astype(str) converts all columns of Pandas DataFrame to string type.

df = df.astype(str)
print(df.dtypes)

##############################################
#Change Type For One or Multiple Columns in Pandas
# Change Type For One or Multiple Columns
df = df.astype({"Fee": int, "Discount": float})
print(df.dtypes)

#########################################
#Convert Data Type for All Columns in a List 
df = pd.DataFrame(technologies)
cols = ['Fee', 'Discount']
df[cols] = df[cols].astype('float')

##################################################
# By using a loop
for col in ['Fee', 'Discount']:
    df[col] = df[col].astype('float')

###################################################
#Raise or Ignore Error when Convert Column type Fails
df = df.astype({"Courses": int},errors='ignore')
# Generates error
df = df.astype({"Courses": int},errors='raise')

##################################################
#Using DataFrame.to_numeric() to Convert Numeric Types
# Converts feed column to numeric type
df['Fee'] = pd.to_numeric(df['Fee'])
###############################################
#Convert multiple Numeric Types using apply() Method
# Convert Fee and Discount to numeric types
df = pd.DataFrame(technologies)
df[['Fee', 'Discount']] =df [['Fee', 'Discount']].apply(pd.to_numeric)
print(df.dtypes)

##############################################
#Quick Examples of Get the Number of Rows in DataFrame
rows_count = len(df.index)
rows_count
rows_count = len(df.axes[0])
rows_count

###############################################
df = pd.DataFrame(technologies)
row_count = df.shape[0]  # Returns number of rows
col_count = df.shape[1]  # Returns number of columns
print(row_count)
#Outputs - 4

###############################################
#pandas Apply Function to a Column
# Below are quick examples
# Using Dataframe.apply() to apply function add column
import pandas as pd
import numpy as np
data = [(3,5,7), (2,4,6),(5,8,9)]
df = pd.DataFrame(data, columns = ['A','B','C'])
print(df)
def add_3(x):
   return x+3
df2 = df.apply(add_3)
df2

############################################################
# Using apply function single column
def add_4(x):
   return x+4
df["B"] = df["B"].apply(add_4)
df["B"]
#########################################################
# Apply to multiple columns
df[['A','B']] = df[['A','B']].apply(add_3)
df
########################################################
# apply a lambda function to each column
df2 = df.apply(lambda x : x + 10)

########################################################
# apply() function on selected list of multiple columns
df = pd.DataFrame(data, columns = ['A','B','C'])
df[['A','B']] = df[['A','B']].apply(add_3)
print(df)

#######################################################
#Apply Lambda Function to Each Column
df2 = df.apply(lambda x : x + 10)
print(df2)

########################################################
#Apply Lambda Function to Single Column Using Dataframe.apply() and lambda function
df["A"] = df["A"].apply(lambda x: x-2)
print(df)

###########################################################
#Using pandas.DataFrame.transform() to Apply Function Column Using DataFrame.transform() 
def add_2(x):
    return x+2
df = df.transform(add_2)
print(df)

#########################################################
#Using pandas.DataFrame.map() to Single Column
df['A'] = df['A'].map(lambda A: A/2.)
print(df)

#########################################################
#Using Numpy function on single Column Using Dataframe.apply() & [] operator
df['A'] = df['A'].apply(np.square)
print(df)

##########################################################
#Using NumPy.square() Method Using numpy.square() and [] operator
df['A'] = np.square(df['A'])
print(df)

#############################################################


