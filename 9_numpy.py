# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:48:46 2024

@author: suraj
"""

#************************use of numpy*********************
#What is NumPy?
#The NumPy library is a popular open-source Python library used for scientific computing applications, and it stands for Numerical Python, which is consisting of multidimensional array objects and a collection of routines for processing those arrays.
'''1. it is used to working on the array i.e. is matrix  Column feature dimension
2. Dimensitonality reduction reduce the large column in small column or less number of column  matrix reduction and develop the model so we required numpy 

#Install Python NumPy Library
1)	goto base terminal and on prompt
2)	pip install numpy
3)	Install NumPy using Conda
4)	conda install numpy
'''
# While a Python list can contain different data types within a single list,all of the elements in a NumPy array should be homogeneous.

#Arrays In NumPy
# Create ndarray
import numpy as np
arr = np.array([10,20,30]) 
print (arr)
# Output : [10 20 30]

#######################################################
#Create a Multi-Dimensional Array
arr = np.array([[10,20,30],[40,50,60]]) 
print (arr)
'''# Output :
[[10 20 30]
 [40 50 60]]
'''
#######################################################
#Represent The Minimum Dimensions
#Use ndmin param to specify how many minimum dimensions you wanted to create an array withaccording to the [] square bracket we can define the dimension of the array dimension to create an array with an minimum dimension ndmin
# Minimum dimension
arr = np.array([10, 20, 30,40], ndmin = 2) 
print (arr) 
 # Output: 
#[[10 20 30 40]]-- 	2 dimension array accourindig to the square bracket

###########################################################
arr = np.array([10, 20, 30,40], ndmin = 3) 
print (arr)
 # Output: [[[10 20 30 40]]]

#########################################################
#Change The Data Type using the dtype parameter 
arr = np.array([10, 20, 30], dtype = complex) 
print(arr)
# Output :[10.+0.j 20.+0.j 30.+0.j]

#######################################################
#Get The Dimensions of Array
arr = np.array([[1, 2, 3, 4], [7, 8, 6, 7], [9, 10, 11, 12]])  
print(arr. ndim) 
print(arr)
'''#Outputs :2
[[ 1  2  3  4]
 [ 7  8  6  7]
 [ 9 10 11 12]]
'''
######################################################
# Finding the size of each item in the array  
arr = np.array([10,20,30])
print("Each item contain in bytes :",arr.itemsize)  
#Outputs:Each item contain in bytes: 4

#######################################################
#Get The Data Type of Each Array Item
# Finding the data type of each array item  
arr = np.array([10,20,30])  
print("Each item is of the type", arr.dtype)
# Output:Each item is of the type int32

#######################################################
#Get the Shape and Size of Array
arr = np.array([[10,20,30,40],[60,70,80,90]])  
print("Array Size:", arr.size)  
print("Shape:", arr.shape)
#o.p:-Array Size: 8
#Shape: (2, 4)

##################################################
#Create NumPy Array From List
# Creation of Arrays
arr = np.array([10, 20, 30])
print("Array:",arr)			#o.p:- Array: [10 20 30]
#################################################
# Creating array from list with type float
arr = np.array([[10, 20, 40], [30,40,50]], dtype = 'float')
print ("Array created by using list: \n", arr)
'''# Output: Array created by using list: 
 [[10. 20. 40.]
 [30. 40. 50.]]
'''
###################################################
#Create a Sequence of Integers using arange()
# Create a sequence of integers from 0 to 20 with steps of 3
arr= np.arange(0, 20, 3)
print ("A sequential array with steps of 3:\n", arr)
#Array Indexing in NumPy
# Output: A sequential array with steps of 3:[ 0  3  6  9 12 15 18]

################################################
# Access single element using index 
arr = np.arange(11)
print(arr)
#[ 0  1  2  3  4  5  6  7  8  9 10]
print(arr[2])
#2
print(arr[-2])
#9

###########################################################
#Multi-Dimenstional Array Indexing
# Access multi-dimensional array element using array indexing
arr =np.array([[10,20,30,40,50],[20,30,50,10,30]])
print(arr)
#o.p:-[[10 20 30 40 50]
# [20 30 50 10 30]]

print(arr.shape)
#o.p:-(2,5) # now x is 2-dimensional

print(arr[1,1])
#30
print(arr[0,4])
#50
print(arr[1,-1])#rows starts from 0,we need 1 st row and last column
#30

##################################################

# Access array elements using slicing
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x= arr[1:8:2]   #start:end:in step of 2
print(x)
# Output: [1 3 5 7]

#################################################
# Example
x=arr[-2:3:-1]#start last but one(-2) upto 3 but not 3 in step of -1
print(x)
# Output: [8 7 6 5 4]

################################################## 
# Example
x=arr[-2:10]#start last but one(-2) and upto 10 but not 10
print(x)
#[8 9]

######################################################
# indexing in numpy
multi_arr = np.array([[10, 20, 10, 40],
        [40, 50, 70, 90],
            [60, 10, 70, 80],
        [30, 90, 40, 30]])
Arr

#############################################
# Slicing array
#For multi-dimensional NumPy arrays, 
#you can access the elements as below

multi_arr [1, 2] #– To access the value at row 1 and column 2.
multi_arr [1,:] #– To get the value at row 1 and all columns.
multi_arr [:, 1] #– Access the value at all rows and columns 1.

###############################################
x= multi_arr[:3, ::2] #columns from 0 to 3,in all selected rows and column every alternate rows
print (x)
# Output : 
# [[10 10]
# [40 70]
# [60 70]]

###############################################


#Integer Array Indexing
#Integer array indexing allows the selection of arbitrary items in the array based on their N-dimensional index. Each integer array represents a number of indices into that dimension. In this method, lists are passed for indexing for each dimension. One to one mapping of corresponding elements is done to construct a new arbitrary array.

# Integer array indexing
arr = np.arange(35).reshape(5, 7)
print(arr)
''' [[ 0  1  2  3  4  5  6]
 [ 7  8  9 10 11 12 13]
 [14 15 16 17 18 19 20]
 [21 22 23 24 25 26 27]
 [28 29 30 31 32 33 34]]’’’
'''
###########################################################
# Boolean Array Indexing
#This advanced indexing occurs when an object is an array object of Boolean types, such as may be returned from comparison operators. Use this method when we want to pick elements from the array which satisfy some conditions.
# Boolean array indexing
arr = np.arange(12).reshape(3,4)
print(arr)
'''#o.p:-
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
###############################################
rows = np.array([False,True,True])#not 0th row only first and second row
wanted_rows= arr[rows, : ]#In selected rows all rows and columns
print(wanted_rows)
'''#o.p:-
[[ 4  5  6  7]
 [ 8  9 10 11]]
'''
####################################################
#Convert NumPy Array to Python List
#We can convert the Numpy array to the list by using tolist() method, We may have a list of data elements that have been converted from the array using this method.
# Convert One Dimensional Array To List
# create array
array = np.array([10, 20, 30, 40])  
print("Array:", array)
print(type(array))
#Array: [10 20 30 40]
#######################################################
# Convert list
lst = array.tolist()
print("list:", lst)
print(type(lst))
#list: [10, 20, 30, 40]

#######################################################3
# Convert Multi Dimensional Array to list
# create array
array = np.array([[10, 20, 30, 40],
                  [50, 60, 70, 80],
                  [60, 40 ,20 ,10]])  
print("Array:", array)
'''#Array: [[10 20 30 40]
 [50 60 70 80]
 [60 40 20 10]]
'''
#######################################################
# Convert list
lst = array.tolist()
print("list:", lst)
#o.p:-list: [[10, 20, 30, 40], [50, 60, 70, 80], [60, 40, 20, 10]]

###################################################
# Convert Python List to A NumPy Array
'''Lists can convert to arrays using the built-in functions in the Python NumPy library.
#How to convert a list to an array in Python
NumPy provides us with two functions to use when converting a list into an array:
1.	numpy.array()
2.	numpy.asarray()
#numpy.array() : Using numpy.array() This function of the numpy library allows a list as an argument and returns an array that contains all the elements of the list. See the example below: import numpy as np. …
'''
# Create list
list = [20,40,60,80]
# Convert array
array = np.array(list)
print ("Array:", array)
# Output: Array: [20 40 60 80]

########################################################
#numpy.asarray() : Using numpy.asarray() This function calls the numpy.array() function inside itself.
# Use asarray()
list = [20,40,60,80]
array = np.asarray(list)
print(" Array:", array)
print(type(array))
# Output : Array: [20 40 60 80]

#######################################################
# Numpy Array Properties 
'''1)	ndarray.shape
2)	ndarray.ndim
3)	ndarray.itemsize
4)	ndaray.size
5)	ndarray.dtype
'''
#ndarray.shape
#To get the shape of a Python NumPy array use numpy.ndarray.shape property. The array shape can be defined as the number of elements in each dimension and dimension is defined as a number of indices or subscripts, that can specify an individual element of an array.shape attribute returns a tuple consisting of array dimensions. It can also use to resize the array. For example,
#Shape
array = np.array([[1,2,3],[4,5,6]]) 
print(array.shape)
# Output :(2, 3)

#########################################################
# Resize the array
array = np.array([[10,20,30],[40,50,60]]) 
array.shape=(3,2)
print(array)

'''# Output:
[[10 20]
 [30 40]
 [50 60]]
'''
####################################################
#NumPy also provides a numpy.reshape() function to resize an array. For example:-
#reshape usage
array = np.array([[10,20,30],[40,50,60]]) 
new_array = array.reshape(3,2)
print(new_array)
'''
# Output : 
[[10 20]
 [30 40]
 [50 60]]
'''
#############################################
# ndarray.ndim
The ndim property is used to find the dimensions of the array.
# Usage of ndim
array = np.array([[1, 2, 3, 4], 
                  [7, 8, 6, 7], 
                  [9, 10, 11, 12]])  
print(array.ndim) 
#Outputs :2

##################################################
#ndarray.itemsize
#The itemsize property is used to get the size of each array item. It returns the number of bytes taken by each array element.
# Finding the size of each item in the array  
array = np.array([10,20,30])
print("Each item contain in bytes :",array.itemsize)  
#Outputs:Each item contain in bytes: 4

##################################################
# ndarray.dtype
#Use dtype function to check the data type of each array item.  
# Finding the data type of each array item  
array = np.array([10,20,30])  
print("Each item is of the type", array.dtype)
#Output:Each item is of the type int32

##################################################
# ndaray.size
#To get the shape and size of the array,the size and shape function associated with the numpy array is used. 
# Get shape and size of array
array = np.array([[10,20,30,40],[60,70,80,90]])  
print("Array Size:", array.size)  
print("Shape:", array.shape)

# Output:Array Size: 8
#Shape: (2, 4)

#####################################################
# Operations Using in NumPy 
#NumPy’s operations are divided into three main
# categories:
'''
1)	Fourier Transform and Shape Manipulation
2)	Mathematical and Logical Operations
3)	Linear Algebra and Random Number Generation.
# Arithmetic Operations
Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.
# Apply arithmetic operations on numpy arrays
'''
arr1 = np.arange(16).reshape(4,4)
arr2 = np.array([1, 3, 2, 4])

# add()
add_arr = np.add(arr1,arr2)
print(f"Adding two arrays:\n{add_arr}")
#Adding two arrays:
# [[ 1  4  4  7]
# [ 5  8  8 11]
# [ 9 12 12 15]
# [13 16 16 19]]

##################################################
# substract()
sub_arr=np.subtract(arr1,arr2)
print(f"Subtracting two arrays:\n{sub_arr}")
#Subtracting two arrays:
# [[-1 -2  0 -1]
# [ 3  2  4  3]
# [ 7  6  8  7]
# [11 10 12 11]]

##################################################
# multiply()
mul_arr = np.multiply(arr1, arr2)
print(f"multiplying two arrays:\n{mul_arr}")
#Multiplying the two arrays:
# [[ 0  3  4 12]
# [ 4 15 12 28]
# [ 8 27 20 44]
# [12 39 28 60]]

#################################################
# divide()
div_arr = np.divide(arr1, arr2)
print(f"Dividing two arrays:\n{div_arr}")
#Dividing the two arrays:
# [[ 0.          0.33333333  1.          0.75      ]
# [ 4.          1.66666667  3.          1.75      ]
# [ 8.          3.          5.          2.75      ]
# [12.          4.33333333  7.          3.75      ]]

##################################################
# numpy.reciprocol()
#This function returns the reciprocal of argumentelement-wise. For elements with absolute values larger than 1, the result is always 0 because of the way in which Python handles integer division. For integer 0, an overflow warning is issued.

# To perform Reciprocal operation
arr1 = np.array([50, 10.3, 5, 1, 200])
rep_arr1=np.reciprocal(arr1)
print(f"After applying reciprocal function to array:\n{rep_arr1}")
#o.p:-After applying reciprocal function:
# [0.02       0.09708738 0.2        1.         0.005     ]

###############################################
# numpy.power()
#This NumPy power() function treats elements in the first input array as the base and returns it raised to the power of the corresponding element in the second input array.

# To perform power operation
arr1 = np.array([3, 10, 5])
pow_arr1 = np.power(arr1, 3)
print(f"After applying power function to array:\n{pow_arr1}")
#o.p:-Applying power function:
# [  27 1000  125]

arr2 = np.array([3, 2, 1])
print("My second array:\n",arr2)
pow_arr2=np.power(arr1, arr2)
print(f"After applying power function to array:\n{pow_arr2}")
#o.p:-Applying power function again:
# [ 27 100   5]

#################################################
# numpy.mod()
#This function returns the remainder of the division of the corresponding elements in the input array. The function numpy.remainder() also produces the same result.
# To perform mod function
# on NumPy array
import numpy as np
arr1 = np.array([7, 20, 13])
arr2 = np.array([3, 5, 2])
arr1
arr1.dtype
# mod()
mod_arr = np.mod(arr1, arr2)
print(f"After applying mod function to array:\n{mod_arr}")
#o.p:- Applying mod() function: [1 0 1]
##########################################

# remainder()
rem_arr = np.remainder(arr1, arr2)
print(f"After applying remainder function to array:\n{rem_arr}")
#o.p:-Applying remainder() function: [1 0 1]

