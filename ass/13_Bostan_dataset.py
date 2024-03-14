# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:10:08 2024

@author: suraj
"""

#Bostan dataset
'''inference of the Bostan dataset
problem statement:-The Boston Housing Dataset is a derived from information
Collected by the U.S. Census Service concerning housing in the area of Boston MA.
1. in this dataset there are 506 recods or case are there and 15 columns are present
2.Origin-The origin of the boston housing data is Natural.
3.Usage-This dataset may be used for Assessment.
#column description
a.CRIM - per capita crime rate by town
b.ZN - proportion of residential land zoned for lots over 25,000 sq.ft.
c.INDUS - proportion of non-retail business acres per town.
d.CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)
e.NOX - nitric oxides concentration (parts per 10 million)
f.RM - average number of rooms per dwelling
g.AGE - proportion of owner-occupied units built prior to 1940
h.DIS - weighted distances to five Boston employment centres
i.RAD - index of accessibility to radial highways
j.TAX - full-value property-tax rate per $10,000
k.PTRATIO - pupil-teacher ratio by town
j.B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
l.LSTAT - % lower status of the population
m.MEDV - Median value of owner-occupied homes in $1000's

businee udestanding
businee objective 
minimization:-nox, in which the nitrous oxide level is to be predicted; and 
price, in which the median value of a home is to be predicted
Miscellaneous Details

maximaization:-

business constranint:-

data dictionary:-
1.data is in this dataset is in the continuos form


'''
'''1.eda
2.data preprocessing'''
'''About Dataset
Domain: Real Estate

Difficulty: Easy to Medium

Challenges:

Missing value treatment
Outlier treatment
Understanding which variables drive the price of homes in Boston
Summary:
The Boston housing dataset contains 506 observations and 14 variables. The dataset contains missing values'''
import pandas as pd
import numpy as np
import seaborn as sns
df=pd.read_csv("C:/Data Science/data_set/Boston.csv")
df
##############################
#columns
df.columns
################################
#shape
df.shape
################################
#data type
df.dtypes
################################
# 5 number summary
df.describe()
##################################
#null value are present or not
df.isnull
df.isnull().sum()
##################################
#misssing value  is not present 
#if it is present then drop it
df.dropna(axis=0,how='any')
###############
df.dtypes
#make the crim columnn as the int
df.crim=df.crim.astype(int)
df.dtypes
#scatter plot
sns.boxplot(df.crim)
sns.boxplot(df.rad)
sns.boxplot(df.tax)
sns.boxplot(df.zn)
sns.boxplot(df.chas)
sns.boxplot(df)
#scattter plot
sns.scatterplot(data=df)
