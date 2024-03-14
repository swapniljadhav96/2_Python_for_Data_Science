# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:30:47 2024

@author: suraj
"""


'''************shallow copy and Deep copy*****************
In Python, assignment statements (obj_b =obj_a) do not create real copies.
It only creates a new variable with the same reference.
So when you want to make actual copies of mutable objects (lists, dicts)
and want to modify the copy without affecting the original, you have to be careful.
For 'real' copies we can use the copy module. However, for compound/nested objects (e.g. nested lists or dicts)
and custom objects there is an important difference between shallow and deep copying:

    - shallow copies: Only one level deep. It creates a new collection object and custom objects there is an important 
difference between shallow and deep copying:
shallow copies: Only one level deep. It creates a new collection object and populates it with references to the nested objects.
This means modyfing a nested object in the copy deeper than one level affects the original.
- deep copies: A full independent clone. It creates a new collection object and then recursively populates it with copies of the nested objects found in the original.
'''
#Assigment opertion
#this will only create a new variable with  the same reference .modify
#one will affect the other
list_a= [1,2,3,4,5]
list_b = list_a             #it will assign the list a value to the list b value
                            #and then  we modify the list_a then thet modifiicatiion will be ahppen in the list-b also

list_a[0] = -10 
print(list_a)
print(list_b)

'''
print(list_a)
[-10, 2, 3, 4, 5]

print(list_b)
[-10, 2, 3, 4, 5]'''

#############################
#shallow copy
#one level deep modifying on level 1 does not affect  the othre list
#use copy.copy(),
#apply cable only for the single level of the list

import copy
list_a = [1,2,3,4,5]
list_b= copy.copy(list_a)

#not affects the other list
list_b[0] = -10
print(list_a)
print(list_b) 

'''print(list_a)
[1, 2, 3, 4, 5]

print(list_b) 
[-10, 2, 3, 4, 5]'''
####################################
#drawback of the sahllow copy
#but with the nested object modifying in level 2 or deeeper does affect the other!
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.copy(list_a)

#afffect the other!
list_a [0][0]=-10
print(list_a)
print(list_b)

'''[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]'''

########################################
#deep copy:- not affet the other list only modification will be happen in the main copy
#full independent clones. use copy.deepcopy()
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)

#not afffect the other!
list_a [0][0]=-10
print(list_a)
print(list_b)
'''print(list_a)
[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

print(list_b)
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]'''
######################################
#python
#advance python
#python for data science
#matplotlib
#seborn
#python for nlp







