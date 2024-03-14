# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:21:28 2024

@author: suraj
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 08:29:33 2023

@author: suraj
"""

"""--------------------Numpy opertion-------------------------"""
#numpy assigment
#Write the anumpy program  to get the numpy version and show the numpy  configuration
import numpy as np
print(np.__version__)
print(np.show_config())

################
#write the numpy program to get help with the add function
import numpy as np
print(np.info(np.add0))
print(np.transpose(np.add))
#write the a numpy to test whether none of the element of the given array is zero
import numpy as np
x=np.array([1,2,3,4])
print("original array")
print(x)
print("Test if none of the element of the said array is zero:")
print(np.all(x))
############
#print the zero element in the array :- it give the  the out put as the boolean value
x=[0,1,2,3,4]
print("original array")
print(x)
print("Test if none of the element of the said array is zero:")
print(np.all(x))
#######################
#write the numpy program to test if any of the elment of the given array is non _zero
import numpy as np
x=[0,1,0,0]
print("original array")
print(x)
print("Test if none of the element of the said array is non_zero:")
print(np.any(x))
#############
x=[0,0,0,0]
print("original array")
print(x)
print("Test if none of the element of the said array is non_zero:")
print(np.any(x))
##############################
#write the numpy programm to test a given array element_wise for finiten
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print("orignal array")
print(a)
print("test a given array element _wise for finiteness:")
print(np.isfinite(a))


##################################
#write the numpy program to test element -wise for complex numbers,real numberin a array
#also test if a given number is of a scaler type or not.
import numpy as np
a=np.array([1+1j,1+0j,4.5,3,2,2j])
print("original array:")
print(a)
print("checking for the complex number:")
print(np.iscomplex(a))
print("cheking for real number:")
print(np.isreal(a))                     #it give the output in the form of true or false if it is present the
                                        #it give as true or not then it give output as the false
print("cheking for scaler type:")
print(np.isscalar)       
np.isscalar(3.1)
np.isscalar([3.1])

a=[[11,12,12],[23,34,45],[23,34,54]]

# Show the dimenstion

A=np.array(a)
A

A.ndim

# Show shape
A.shape

# Row*Col
A.size

# Accesss rows and se
A[1,2]

A[1,2]

A[1,1]

A[0,0]

' OR '

A[0][0]

# 1st row and 1st and 2nd col

A[0][0:2]

A[:1,2]

# Basic operations 

x=np.array([[2,1],[2,4]])

y=np.array([[2,1],[2,4]])

# Add
Z=x+y
Z

# Sub
Z=x-y
Z

# Mul
Z=x*y
Z

"or "

Z=np.dot(x,y)
Z

# Calculate the sine of Z

np.sin(Z)
#####################################################
#write the numpy program to compute the "outer product" of the two given vector
#dot product of the two matrix/vector
import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("Orignal matrix:")
print(p)
print(q)
result1=np.dot(p,q)         #main body or brain
print("Result of the said matrix multiplication:")
print(result1)
#o.p:-
"""[[1 2]
 [3 4]]"""
#################################################
#write the program to compute the cross product of the two vector
import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("Orignal matrix:")
print(p)
print(q)
result1=np.cross(p,q)
result2=np.cross(q,p)         #main body or brain
print("Result of the said matrix multiplication:")
print(result1)
print(result2)
'''[ 2 -3]

print(result2)
[-2  3]'''

###################################################
#write the numpy program to compute the determinanat of the given square array/matrix "it is shown in the square brakect
from numpy import linalg as LA
import numpy as np
a=np.array([[1,0],[1,2]])
print("origanl 2-d array:")
print(a)
print("determinant of the said 2-d array:-")
print(np.linalg.det(a))
#o.p:-2.0




#################################################
#write the numpy program to compute the eigenvalue and right eigenvector
import numpy as np
m=np.mat("3 -2;1 0")        #complex number
print("origanl matrix:")
print("a\n",m)
w,v =np.linalg.eig(m)
print("Eigenvector of the said matrix",w)       #Eigenvalue of the said matrix [2. 1.]
print("Eigen value of the said matrix",v)
#Eigen value of the said matrix [[0.89442719 0.70710678][0.4472136  0.70710678]]
##############################################
#Write the numpy program to compute the inverses of  a given matroix
import numpy as np
m=np.array([[1,2],[3,4]])
print("original matrix:")
print(m)
result=np.linalg.inv(m)
print("Inverse of the said matrix:")
print(result)

#############################################
#write the numpy program to genrate five random number from the noram distribution
import numpy as np
x=np.random.normal(size=5)          #you can increase or decrese the size also
print(x)
###################################################
#write the numpy program to generteate six random integers between 10 and 30
import numpy as np
x=np.random.randint(low=10,high=30,size=6)
print(x)
##########################################
#write  a numpy program to create a 3*3*3 array with random value
import numpy as np
x=np.random.randint((3,3,3))
print(x)
#########################################
#write numpy program to create 5*5 array with random value
#and find the minimum and maximum vallue
import numpy as np
x=np.random.randint((5,5))
print("Original matrix:")
print(x)
xmin,xmax=x.min(),x.max()
print("minimum and maximum value:")
print(xmin,xmax)

###########################################
"""2/6/23"""
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
#write a python  program tom draw thw a line with sutiable label in the 
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
###################################################






