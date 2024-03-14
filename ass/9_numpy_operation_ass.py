# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:18:59 2024

@author: suraj
"""



######################################################
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

                                        
                                        
                                        