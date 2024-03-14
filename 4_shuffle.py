# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:21:56 2024

@author: suraj
"""

#******************shuffle**********************
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


