# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:22:40 2024

@author: suraj
"""

#write the  the numpy program to get the minimum and maxmimum value accross the axix
import numpy as np
x = np.arange(4).reshape((2,2))
print("Original value/array:")
print(x)
print("\n maximum value along the second axis:")
print(np.amax(x,1))
print("Minimum value along the second axis:")
print(np.amin(x,1))

#np.array(x,1): here the np.amax(x,1) returns the maximum value along the 1st axis (rows) of the x
#
#
#
#
###############################################
#write a python  program to draw the a line with suitable label in the 
#x-axis and y axis and give the title to the graph
import matplotlib.pyplot as plt
x= range(1,50)
y= [value * 3 for value in x]
print("value of x:")
print(*range(1,50))         # astric(*) it give all the value between the 1 to 50 #and not write the astric (*) it give only the 1 and 50 range
print(" value of y (thrice of x):")
print(y)
#ploat line and /or markers to the axes
plt.plot(x,y)
# set the x axis label of the current axis
plt.xlabel('x - axis')
#set the y axis label of the current axis
plt.ylabel('y- axis')
#set the title
plt.title('Draw a line')
#dispaly the figure
plt.show()
#####################################################
#Write a Python program to draw a line with suitable label in the  give list between the x axis and y axis list the 
import matplotlib.pyplot as plt
#x axis value
x= [1,2,3]
#y axis value
y=[2,4,1]
#plot line  and /or makers to the axes
plt.plot(x,y)
#set the x axis label of the current axis
plt.xlabel('x-axis')
#set the y axis label of the current axis
plt.ylabel('y- axis')
#set the title
plt.title('Sample graph @ @')
#dispaly the figure
plt.show()

###############################################
#write the python program to draw line charts of the financial data of  fdata.csv file
##between the octomber 3,2016 to october 7,2016
import matplotlib.pyplot as plt
import pandas as pd
df= pd.read_csv('C:/Data Science/1-python/fdata.csv')
df.plot()
plt.show()