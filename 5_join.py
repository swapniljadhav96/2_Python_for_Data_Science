# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:23:48 2024

@author: suraj
"""

#************************join***************************
'''1. it is important in ML
2.The various tables are join in the csv file 
4. database datapipeline .csv understand the data(EDA)Process modelEvalution model(also called RISP_ML(Q))
5. join for join the only one column is need to indentical
6. Pre requiste to the join there us comman column in the all the table or given table
7. There are various type of the join are present i.e. INNER ,LEFT , Right , Full 
INNER JOIN:-
1. Only common rows will display
2. in this table we can see that India and Nepal are comman entry
3. the join is made on country id of the both the tables
4.show the data only for matching records 
5. pandas inner join is mostly used join, It is used to join two DataFrames on indexes.When indexes don’t match the rows get dropped from both DataFrames.
LEFT Join 
1. In the left join all the data of left table will be display and only matching records /rows of right table will be display
Right join
1. all the records of right table will be display but only matching records of the left table will display
OUTER join
1. in the outer join all the records of left table and all the records af right table are display irrespective to it matching or not
Note :- By default the python will do the  left join.

Syntax:- variable name =DataFrame .join(Tablename1,tablename2,lsuffix =”_left”,rsuffix=”_right” ,how =”join name”)
	While joining the data frame is not mention column name on which column has to be done the join pandas inner join is mostly us ejon 
	It is used to join two dataframe on indexes
	If there is no explicity mentioning of the column
	Merge() = inner join by default left join not mention
	To_csv make the csv file
	Read_csv read the data of the csv file
serial of the right and left suffix will be change it can not harm on the dataframe
#lsuffix and rsuffix is important in the join
#'how=' it can show that which operation i.e. which join we want to perform on the dataframe
#syntax:-
#variblename=table1/dataframe1.join(table2/dataframe2 ,lsuffix="_left",rsuffix="_right",how=' name of join which join you want to perform on the dataframe')
#we can change the sequiece of the lsuffix and rsuffix
#from "how" statement we can specifies the which join is we can use in the excution
'''
##################################################
#Pandas Shuffle DataFrame Rows 
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30day','40days','35days','40days','60days','50days','55days'],
    'Discount':[1000,2300,1500,1200,2500,2100,2000]
               }
df = pd.DataFrame(technologies)
print(df)
#Pandas Shuffle DataFrame Rows shuffle the DataFrame rows & return all rows
df1 = df.sample(frac = 1)
print(df1)
#frac=1 it can do the shuffling of the data 

##############################################################
# Create a new Index starting from zero:- creating the new index starting from zero and it give the  older inde aswell  as  the newer index ie.shuffle index
df1 = df.sample(frac = 1).reset_index()
print(df1)

#############################################################
# Drop shuffle Index :- it can drop the shuffling the index value
df1 = df.sample(frac = 1).reset_index(drop=True)
print(df1)

###############################################################
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
              }
index_labels=['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)


# pandas join ,by default it will join the table left join
df3=df1.join(df2, lsuffix="_left", rsuffix="_right")
print(df3)
# In the left join all the data of left table will be display and only matching records /rows of right table will be display

########################################################
# pandas Inner join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='inner')
print(df3)
#. Only common rows will display
"""Out[26]: 
   courses_left  	discount	 courses_right   fee 	duration
r1        spark      	2134         spark  		2134   34days
r3      python       	4567       python   		4567   43days"""

############################################################
#pandas Left join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='left')
print(df3)
# In the left join all the data of left table will be display and only matching records /rows of right table will be display
"""Out[28]: 
   courses_left   	fee duration courses_right  discount
r1        spark  		2134   34days         spark    2134.0
r2      pyspark  	3456   54days           NaN       NaN
r3      python   	4567   43days       python     4567.0
r4       pandas   	768   36days           NaN       NaN"""
################################################################
 #pandas Right join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='right')
print(df3)
#. all the records of right table will be display but only matching records of the left table will display
"""df3
Out[30]: 
   courses_left     	fee duration courses_right  discount
r1        spark  		2134.0   34days         spark      2134
r6          NaN    	 NaN      NaN          java      3456
r3      python   	4567.0   43days       python       4567
r5          NaN     	NaN      NaN            go       565"""

###############################################################
# pandas join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'), how='inner')
print(df3)
##############################################################
# pandas join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'), how='left')
print(df3)

########################################################
# pandas join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'), how='right')
print(df3)

#########################################################
#we can join(use any join i.e. left ,right or inner) the more than one column by using the doble coat and [] bracket
df3=df1.set_index(["courses","discount"]).join(df2.set_index(["courses","discount"]),how='right')
df3

###########################################################
#inner join=Pandas Merge DataFrames
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
              }
index_labels=['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)

# Using pandas.merge()
df3= pd.merge(df1,df2)

# Using DataFrame.merge()
df3=df1.merge(df2)

########################################################
#Use pandas.concat() to Concat Two DataFrames
import pandas as pd
df = pd.DataFrame({'Courses': ["Spark","PySpark","Python","pandas"],
                    'Fee' : [20000,25000,22000,24000]})

df1 = pd.DataFrame({'Courses': ["Pandas","Hadoop","Hyperion","Java"],
                    'Fee': [25000,25200,24500,24900]})

# Using pandas.concat() to concat two DataFrames
data = [df, df1]
df2 = pd.concat(data)
df2

###########################################################
#Concatenate Multiple DataFrames Using pandas.concat()
import pandas as pd
df = pd.DataFrame({'Courses': ["Spark", "PySpark", "Python", "Pandas"],
                    'Fee' : ['20000', '25000', '22000', '24000']}) 
  
df1 = pd.DataFrame({'Courses': ["Unix", "Hadoop", "Hyperion", "Java"],
                    'Fee': ['25000', '25200', '24500', '24900']})
  
df2 = pd.DataFrame({'Duration':['30day','40days','35days','60days','55days'],
                    'Discount':[1000,2300,2500,2000,3000]})
  
# Appending multiple DataFrame
df3 = pd.concat([df, df1, df2])
print(df3)

##########################################################
#Use pandas.concat() to Concat Two DataFrames
import pandas as pd
df = pd.DataFrame({'Courses': ["Spark","PySpark","Python","pandas"],
                    'Fee' : [20000,25000,22000,24000]})

df1 = pd.DataFrame({'Courses': ["Pandas","Hadoop","Hyperion","Java"],
                    'Fee': [25000,25200,24500,24900]})

# Using pandas.concat() to concat two DataFrames
data = [df, df1]
df2 = pd.concat(data)
df2

###########################################################
#Concatenate Multiple DataFrames Using pandas.concat()
import pandas as pd
df = pd.DataFrame({'Courses': ["Spark", "PySpark", "Python", "Pandas"],
                    'Fee' : ['20000', '25000', '22000', '24000']}) 
  
df1 = pd.DataFrame({'Courses': ["Unix", "Hadoop", "Hyperion", "Java"],
                    'Fee': ['25000', '25200', '24500', '24900']})
  
df2 = pd.DataFrame({'Duration':['30day','40days','35days','60days','55days'],
                    'Discount':[1000,2300,2500,2000,3000]})
  
# Appending multiple DataFrame
df3 = pd.concat([df, df1, df2])
print(df3)

#########################################################
# Write DataFrame to CSV File with Default params.
df3.to_csv("c:/10-python/courses.csv")
#read CSV
# Import pandas
import pandas as pd

# Read CSV file into DataFrame
df = pd.read_csv('courses.csv')
print(df)

############################################################
# Write DataFrame to Excel file
df.to_excel('c:/10-python/Courses.xlsx')

########################################################
import pandas as pd
# Read Excel file
df = pd.read_excel('c:/10-python/Courses.xlsx')
print(df)

#####################################################
# Using Series.values.tolist()
col_list = df.Courses.values.tolist()
print(col_list)

####################################################
# Using Series.values.tolist()
col_list = df["Courses"].values.tolist()
print(col_list)

###################################################
# Using list() Function
col_list =  list(df["Courses"])
print(col_list)

####################################################

# Conver to numpy array
col_list = df['Courses'].to_numpy()
print(col_list)

#####################################################
# Get by Column Index
col_list = df[df.columns[0]].values.tolist()
print(col_list)

########################################################
# Convert Index Column to List
index_list = df.index.tolist()
print(index_list)
