# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:53:35 2024

@author: suraj
"""

#################opertion on array and matrix
# create array
from numpy import array
# create array
l = [1.0, 2.0, 3.0]
a = array(l)
# display array
print(a)        #o.p:-[1. 2. 3.]
# display array shape
print(a.shape)  #o.p:-(3,)
# display array data type
print(a.dtype)      #o.p:-float64

################################################
# create empty array
from numpy import empty
a = empty([3,3])
print(a)
'''
[[4.67296746e-307 1.69121096e-306 1.24610994e-306]
 [1.42413555e-306 1.78019082e-306 1.37959740e-306]
 [6.23057349e-307 1.42419530e-306 3.91786943e-317]]
'''
########################################
# create zero array
from numpy import zeros
a = zeros([3,5])
print(a)
'''
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
'''
###########################################
# create one array
from numpy import ones
a = ones([5])
print(a)        #o.p:-[1. 1. 1. 1. 1.]

#########################################
# create array with vstack
from numpy import array
from numpy import vstack
# create first array
a1 = array([1,2,3])
print(a1)               #o.p:-[1 2 3]
# create second array
a2 = array([4,5,6])
print(a2)               #o.p:-[4 5 6]
# vertical stack
a3 = vstack((a1, a2))
print(a3)               #o.p:-[[1 2 3] [4 5 6]]
print(a3.shape)         #o.p:-(2, 3)

#############################################
# create array with hstack
from numpy import array
from numpy import hstack
# create first array
a1 = array([1,2,3])
print(a1)               #o.p:-[1 2 3]
# create second array
a2 = array([4,5,6])
print(a2)               #o.p:-[4 5 6]
# create horizontal stack
a3 = hstack((a1, a2))
print(a3)               #o.p:-[1 2 3 4 5 6]
print(a3.shape)         #o.p:-(6,)

######################################################
#One-Dimensional List to Array
# create one-dimensional array
from numpy import array
# list of data
data = [11, 22, 33, 44, 55]
# array of data
data = array(data)
print(data)     #o.p:-[11 22 33 44 55]
print(type(data))       #o.p:-<class 'numpy.ndarray'>

######################################################
#Two-Dimensional List of Lists to Array
# create two-dimensional array
from numpy import array
# list of data
data = [[11, 22],
[33, 44],
[55, 66]]
# array of data
data = array(data)
print(data)
'''o.p:-[[11 22]
 [33 44]
 [55 66]]'''
print(type(data))           #o.p:-<class 'numpy.ndarray'>

###################################################
# index a one-dimensional array
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
# index data
print(data[0])          #o.p:-11
print(data[4])          #o.p:-55

################################################
# index array out of bounds
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
# index data
print(data[5])
#IndexError: index 5 is out of bounds for axis 0 with size 5

##################################################
# negative array indexing
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
# index data
print(data[-1])         #o.p:-55
print(data[-5])         #o.p:-11

##################################################
# index two-dimensional array
from numpy import array
# define array
data = array([
[11, 22],
[33, 44],
[55, 66]])
# index data
print(data[0,0])        #o.p:-11

###########################################



# index row of two-dimensional array
from numpy import array
# define array
data = array([
[11, 22],
[33, 44],
[55, 66]])
# index data
print(data[0,])#o th row and all columns
#[11 22]

##########################################
# slice a one-dimensional array
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
print(data[1:4])
#[22 33 44]

###################################################
# negative slicing of a one-dimensional array
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
print(data[-2:])            #o.p:-[44 55]

##################################################
# split input and output data
from numpy import array
# define array
data = array([
[11, 22, 33],
[44, 55, 66],
[77, 88, 99]])
# separate data
X, y = data[:, :-1], data[:, -1]
#data[:, :-1]-all rows and all columns
#except all rows and last column
#data[:, -1]-taking all rows (:) 
#but keeping the last column (-1)
print(X)
'''o.p:-[[11 22]
 [44 55]
 [77 88]]'''
print(y)        #o.p:-[33 66 99]
###########################################
# broadcast scalar to one-dimensional array
from numpy import array
# define array
a = array([1, 2, 3])
print(a)        #o.p:-[1 2 3]
# define scalar
b = 2           #o.p:-2
print(b)
# broadcast
c = a + b
print(c)        #o.p:-[3 4 5]

################################################
# vector addition
from numpy import array
# define first vector
a = array([1, 2, 3])
print(a)        #o.p:-[1 2 3]
# define second vector
b = array([1, 2, 3])
print(b)                #o.p:-[1 2 3]
# add vectors
c = a + b
print(c)                #o.p:-[2 4 6]

############################################
# vector subtraction
from numpy import array
# define first vector
a = array([1, 2, 3])
print(a)            #o.p:-[1 2 3]
# define second vector
b = array([0.5, 0.5, 0.5])
print(b)            #o.p:-[0.5 0.5 0.5]
# subtract vectors
c = a - b
print(c)            #o.p:-[0.5 1.5 2.5]

###########################################
# vector L1 norm
from numpy import array
from numpy.linalg import norm
# define vector
a = array([1, 2, 3])
print(a)            #o.p:-[1 2 3]
# calculate norm
l1 = norm(a, 1)
print(l1)       #o.p:-6.0

############################################
# vector L2 norm
from numpy import array
from numpy.linalg import norm
# define vector
a = array([1, 2, 3])
print(a)            #o.p:-[1 2 3]
# calculate norm
l2 = norm(a)
print(l2)           #o.p:-3.7416573867739413

################################################
# triangular matrices
from numpy import array
from numpy import tril
from numpy import triu
# define square matrix
M = array([
[1, 2, 3],
[1, 2, 3],
[1, 2, 3]])
print(M)
'''o.p:-[[1 2 3]
 [1 2 3]
 [1 2 3]]'''
# lower triangular matrix
lower = tril(M)
print(lower)
'''o.p:-[[1 0 0]
 [1 2 0]
 [1 2 3]]'''
# upper triangular matrix
upper = triu(M)
print(upper)
'''o.p:-[[1 2 3]
 [0 2 3]
 [0 0 3]]'''

##############################################
# diagonal matrix
from numpy import array
from numpy import diag
# define square matrix
M = array([
[1, 2, 3],
[1, 2, 3],
[1, 2, 3]])
print(M)
'''o.p:-[[1 2 3]
 [1 2 3]
 [1 2 3]]'''
# extract diagonal vector
d = diag(M)
print(d)
#o.p:-[1 2 3]
# create diagonal matrix from vector
D = diag(d)
print(D)
'''o.p:-[[1 0 0]
 [0 2 0]
 [0 0 3]]'''

#############################################
#identity matrix
from numpy import identity
I = identity(3)
print(I)
'''o.p:-[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]'''

##############################################
# orthogonal matrix
from numpy import array
from numpy.linalg import inv
# define orthogonal matrix
Q = array([
[1, 0],
[0, -1]])
print(Q)
'''o.p:-[[ 1  0]
 [ 0 -1]]'''
# inverse equivalence
V = inv(Q)
print(Q.T)
'''o.p:-
[[ 1  0]
 [ 0 -1]]'''
print(V)
'''o.p:-[[ 1.  0.]
 [-0. -1.]]'''

###################
# identity equivalence
I = Q.dot(Q.T)
print(I)
'''o.p:-[[1 0]
 [0 1]]'''

########################################
# transpose matrix
from numpy import array
# define matrix
A = array([
[1, 2],
[3, 4],
[5, 6]])
print(A)            #o.p:- it will print the array
# calculate transpose
C = A.T
print(C)
'''o.p:-[[1 3 5]
 [2 4 6]]'''

##########################################
# invert matrix
from numpy import array
from numpy.linalg import inv
# define matrix
A = array([
[1.0, 2.0],
[3.0, 4.0]])
print(A)            #o.p:- it gove the above matrix
# invert matrix
B = inv(A)
print(B)
'''o.p:-[[-2.   1. ]
 [ 1.5 -0.5]]'''
# multiply A and B
I = A.dot(B)
print(I)
'''o.p:-[[1.00000000e+00 1.11022302e-16]
 [0.00000000e+00 1.00000000e+00]]'''
###########################################

# sparse matrix
from numpy import array
from scipy.sparse import csr_matrix
# create dense matrix
A = array([
[1, 0, 0, 1, 0, 0],
[0, 0, 2, 0, 0, 1],
[0, 0, 0, 2, 0, 0]])
print(A)                #o.p:-it will give the above array
# convert to sparse matrix (CSR method)
S = csr_matrix(A)
print(S)
'''o.p:-  (0, 0)	1
  (0, 3)	1
  (1, 2)	2
  (1, 5)	1
  (2, 3)	2'''
# reconstruct dense matrix
B = S.todense()
print(B)
'''o.p:-[[1 0 0 1 0 0]
 [0 0 2 0 0 1]
 [0 0 0 2 0 0]]'''

##############################################
from numpy import array
T = array([
[[1,2,3], [4,5,6], [7,8,9]],
[[11,12,13], [14,15,16], [17,18,19]],
[[21,22,23], [24,25,26], [27,28,29]]])
print(T.shape)                  #o.p:-(3, 3, 3)
print(T)
'''o.p:-[[[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]]

 [[11 12 13]
  [14 15 16]
  ['17 18 19]]

 [[21 22 23]
  [24 '25 26]
  [27 28 29]]]'''


'''
Order of Operations
PEMDAS

You can remember by saying "Please Excuse My Dear Aunt Sally".

Or ...	Pudgy Elves May Demand A Snack
Popcorn Every Monday Donuts Always Sunday
Please Eat Mom's Delicious Apple Strudels
People Everywhere Made Decisions About Sums
You may prefer GEMS (Grouping, Exponents, Multiply or Divide, Add or Subtract).
In the UK they say BODMAS (Brackets, Orders, Divide, Multiply, Add, Subtract).
In Canada they say BEDMAS (Brackets, Exponents, Divide, Multiply, Add, Subtract).
It all means the same thing! It doesn't matter how you remember it, just so long as you get it right.

How Do I Remember It All ... ? PEMDAS !
P
Parentheses first
E
Exponents (ie Powers and Square Roots, etc.)
MD
Multiplication and Division (left-to-right)
AS
Addition and Subtraction (left-to-right)

Divide and Multiply rank equally (and go left to right).

Add and Subtract rank equally (and go left to right)
'''