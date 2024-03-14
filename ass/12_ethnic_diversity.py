# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:43:13 2024

@author: suraj
"""


import pandas as pd
#let us import the dataset
df=pd.read_csv("C:/Data Science/data_set/ethnic diversity.csv")
df
#check all the phase of EDA
#let check the shape of the dataset
df.shape
#(310, 13)
#check the column
df.columns

#check datatypes 
df.dtypes
'''Employee_Name        object
EmpID                 int64
Position             object
State                object
Zip                   int64
Sex                  object
MaritalDesc          object
CitizenDesc          object
EmploymentStatus     object
Department           object
Salaries            float64
age                   int64
Race                 object
dtype: object'''
#check is null
df.isnull
#######################
df.dtypes
#type casting of the salaries is in float make it as int
df.Salaries=df.Salaries.astype(int)
df.dtypes  #now it is in the int
'''Employee_Name       object
EmpID                int64
Position            object
State               object
Zip                  int64
Sex                 object
MaritalDesc         object
CitizenDesc         object
EmploymentStatus    object
Department          object
Salaries             int32
age                  int64
Race                object
dtype: object'''
#########
#type casting
#type casting of the age is in float make it in float
df.age=df.age.astype(float)
df.dtypes
'''Employee_Name        object
EmpID                 int64
Position             object
State                object
Zip                   int64
Sex                  object
MaritalDesc          object
CitizenDesc          object
EmploymentStatus     object
Department           object
Salaries              int32
age                 float64
Race                 object
dtype: object'''
##########################################################################




