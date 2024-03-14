# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:13:19 2024

@author: suraj
"""


############################################
"""----------asssigment ------------------------"""
import pandas as pd
df = pd.read_csv('AutoInsurance.csv')
df
#########
df.shape
###########
df.size
#######
#Accesing one column content
df['Customer']
###################
#Accesing two column contents
df[['Customer','State']]
########################
#Select certain rows and assign it to another dataframe
df1 = df[3:16]
df1
###################
#Accessing certain cells from column
df['State'][4]
###########################
#Describe Dataframe
df.describe
#####################
#Rename
df1 = df.rename({'Customer':'Earnings'},axis='columns')
df1
######################
#Drop DataFrame Rows and Columns
df.drop(index=3,columns='Customer')
df
##################
#Drop Rows by Labels
df1 = df[:3]
df1
###################
#How to label the rows of a imported csv file"""

#Delete Rows by Position
df1 = df.drop([df.index[2]])
df1
#########################

#Deleting Rows by Index Range
df1 = df.drop(range(0,200))
df1
#####################
#Select Rows by Index
df2 = df[300:450]
df2