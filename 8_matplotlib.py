# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:44:40 2024

@author: suraj
"""

#**********************graph draw***************************
#Matplotlip:- it is used to plot the graph,,,, first install the matplotlip i.e. as like a pandas 
#1. wite the command “pip install matplotlip”
#plaoting the two series
import pandas as pd
songs_69=pd.Series([7,56,34,1],
                   index=['aa','ss','dd','ff'],
                   name='Counts')

import matplotlib.pyplot as plt
flg=plt.figure()
songs_69.plot()
plt.legend()

###################################
#for studing the bar graph for plotings the series
import pandas as pd
songs_66=pd.Series([3,None,11,9],
                   index=['a','s','d','f'],
                   name='Counts')

flg=plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='k',alpha=.5)
plt.legend()
 

##########################################
#hextogram
import numpy as np
data=pd.Series(np.random.randn(500),
name='500 random')
flg=plt.figure()
ax=flg.add_subplot(111)
data.hist() 
