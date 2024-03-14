# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:58:51 2024

@author: suraj
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 13 08:12:39 2023

@author: suraj
"""
"""------------------------------seaborn library------------------------------------"""
#how to use the seaborn for datavisualization
#pip install seaborn
import seaborn as sns
import pandas
import matplotlib.pyplot as plt
#seaborn has 18 types of dataset
#titanic
#that can ne found by using the following command'
sns.get_dataset_names()
'''sns.get_dataset_names()
Out[127]: 
['anagrams', 'anscombe', 'attention', 'brain_networks','car_crashes',
 'diamonds', 'dots', 'dowjones',  'exercise', 'flights', 'fmri', 'geyser', 'glue', 'healthexp', 'iris', 'mpg', 'penguins', 'planets', 'seaice',
 'taxis', 'tips','titanic']'''

#create the dataset as like csv file
#here we no need to give the absulte path
df=sns.load_dataset('titanic')
df.head()
'''it can give the dataset 
df=sns.load_dataset('titanic')

df.head()
Out[8]: 
   survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0         0       3    male  22.0  ...   NaN  Southampton     no  False
1         1       1  female  38.0  ...     C    Cherbourg    yes  False
2         1       3  female  26.0  ...   NaN  Southampton    yes   True
3         1       1  female  35.0  ...     C  Southampton    yes  False
4         0       3    male  35.0  ...   NaN  Southampton     no   True

[5 rows x 15 columns]'''

######################################
#give the dataset graph
# we can make graph iof the dataset element
#data =dataframe
#x=name of the column
sns.countplot(x='sex',data=df)
#########
#hue is used to different categories
sns.countplot(x='sex',hue='survived',data=df,palette='Set1')
#palette:- it  can give the color combination to the graph or color to be used
#it can give the double graph
#color cobination of the graph
sns.countplot(x='sex',hue='survived',data=df,palette='Set2')
sns.countplot(x='sex',hue='survived',data=df,palette='Set3')
##################
#kde plot
#A kernal density estimated (kde) plot is used
# to plot the distributiom of continous data
sns.kdeplot(x='age',data=df,color='black')
#kdeplot give the condinous graph
#x= the name of the dataset column
#data=the name of the dataframe
#color= the color name
#######################3
#distribution plot
sns.displot(x='age',kde=True,bins=5,data=df)
#kde-it is set to false by default 
#bin:- it give the number  of bar 
# the lower the number of the bar wider the bar vice versa

#############################################
#add view to the graph
sns.displot(x='age',kde=True,bins=5,hue=df['survived'],palette='Set1',data=df)
#it can give distribution of the graph according to the data
###########################
'''========iris======='''
#sactter plot:- find the rekation between sepal name and petal name
#iris dataset:- species of Iris (Iris setosa, Iris virginica and Iris versicolor)
#iris dataset contain:- the dadta realated to gthe flower petal size
# 
df=sns.load_dataset('iris')
df.head()
################
#first,se will need to help understand co_relation between data
sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')
# explain the 
"""in the above plot we can observe that an iris flower with sepal 
length<6cm and petal  length<2cm
 is most likely of type setosa.
  in iris flower with sepal 
 length<7cm and petal  length<5cm are moslty like versicolr,
 iris flower with sepal 
 length<8cm and petal  length<7cm are moslty like viraginica
 although there is no distinct boundary present between  the versicolor dots and virgincal dat
 on iris  flower with petal length between 3cm and 5 cm
  is mostly likely to type  versicolor
  while iris flowers with petal length>5cm
  are mostly likely of type virginica"""
  
  
#########################################
#joint plot
# ajoint plot  is also used to plot the coreralton betnween  the various graph 
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg') 
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='hist') 
# it  give the kde plot only kind is change
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='kde')  

''' kind the kind of the plot to be ploted
it can be one of the following
scatter ,'hist','hex','kde','reg','resid','''
##################################
# pair plot are usend in the co
sns.pairplot(df)
# it plot the all the graph annaysy is fiven
###################
#A heat map /is used o visualtion  confusion
# how to find the heat map
#corr is corelation
#only map the heat map
corr=df.corr()
sns.heatmap(corr)
# in the graph 1 means it having the high visualitaion
#And black means it having the low visualtion

#########################
# boxplot:-tell about the distribution of the data min and max value
#tell about the outlayer means extremly value


"""------------------------------2.30---------------------------------------------------""" 
###assigment
from scipy.stats import skew
from scipy.stats import kurtosis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#rename the  file or access the file
# means go  in the file downloaded 
cars=pd.read_csv("C:/Data Science/1-python/Q1_a.csv") # it is the absult path of the file and it can read th econtain of the file
cars.columns # it can give the  dataframe column name it the dataset
"""cars.columns
Out[10]: Index(['Index', 'speed', 'dist'], dtype='object')"""
##########################

cars.describe()
# it can descibe the data set
"""
Out[11]: 
          Index      speed        dist
count  50.00000  50.000000   50.000000
mean   25.50000  15.400000   42.980000
std    14.57738   5.287644   25.769377
min     1.00000   4.000000    2.000000
25%    13.25000  12.000000   26.000000
50%    25.50000  15.000000   36.000000
75%    37.75000  19.000000   56.000000
max    50.00000  25.000000  120.000000"""


#############################
# it can  draw thw histogram graph of the file Q_a file 
plt.hist(cars.speed)
############
sns.displot(x='speed',kde=True,bins=6,data=cars)
# almost  the 14 cars are rum between in the 10-15 m/s 
#12 cars are travilling sith the speed of the 14 m/s
# and car are ttravelling with the7 with speed of the 7

##############################
#left skwed/negative skewed:- lowrer value are higher in the left side
#sysmetric skewed:- equal vallue are present on the sideof the graph
#right skewed /poostive skewed:- lower value are higher in the right side
##############
#distant
sns.displot(x='dist',kde=True,bins=6,data=cars)
# the distance covered 10 to 40 km are 17 cars
#right skewed:-the lower value are prsend in the right side

################
#box plot
cars.describe()
sns.boxplot(cars.speed)
# outlayer caclutaed the median
# box plot give the mean adn max amd min value and outkayer
"""cars.describe()
Out[16]: 
          Index      speed        dist
count  50.00000  50.000000   50.000000
mean   25.50000  15.400000   42.980000
std    14.57738   5.287644   25.769377
min     1.00000   4.000000    2.000000
25%    13.25000  12.000000   26.000000
50%    25.50000  15.000000   36.000000
75%    37.75000  19.000000   56.000000
max    50.00000  25.000000  120.000000
boxplot give the information are listed above and 
in the form of the box plot"""
###########################
#outlier are shown by the dot ( it can perfoem the rdeue on the data)
# box plot on the dist
sns.boxplot(cars.dist)
# it can show the boxplot on the dist\
# the one outlier are present
#########################
# use the matplot packagge
# convert the dataset atom column in the list
speed_lst=cars['speed'].tolist()
speed_lst
'''Out[21]: 
[4, 4, 7, 7, 8, 9, 10, 10, 10, 11,11, 12, 12
 , 12, 12, 13, 13, 13, 13, 14, 14, 14, 1
 4, 15, 15, 15, 16, 16,17, 17, 17, 18, 18, 18, 
 18, 19, 19, 19,20, 20, 20, 20, 20,22,23,
 24,24, 24,24, 25]'''
###########################
#skew function accept the list value
#skewness
# for calclating the skewnee of the any datset column we need
#to convert the column into the list firt then apply the opertion
print("skewness of the speed",skew(speed_lst))
#skewness of the speed -0.11395477012828319
####################
# we can convert the distance column in the list form
dist_lst=cars['dist'].tolist()
dist_lst
print("skewness of the speed",skew(dist_lst))
# caluclate the skewnes for dist
##########################
# skew():-
print(skew(dist_lst))


#####
#bar graph,joint plot.hit ploat
#bargraph
################
#distribution plot
cars.describe()
sns.displot(x='speed',kde=True,bins=5,data=cars)

####################
# count plot
sns.countplot(x='speed',data=cars)
# add hue
sns.countplot(x='dist',hue='speed',data=cars,palette='Set1')
#*revisedd

#########
# kdeplot 
sns.kdeplot(x='speed',data=cars,color='black')
#################
#scatter plot
sns.scatterplot(x='speed',y='dist',data=cars)
# maxim dist is cover by the car is in speed 25
# in the dist 120
# most are the dist cover in the speed of the in 10 to 25
# in the distsnce 20m to the 40m
#################
#joint plot
sns.jointplot(x='speed',y='dist',data=cars,kind='reg') 
# write what you caaan udestand from the  above plot
###############
#pair plot
sns.pairplot(cars)
##################
#heatmap is used to visualitation of the data
corr=cars.corr()
sns.heatmap(corr)

# in the graph 1 means it having the high visualitaion
#And black means it having the low visualtion
# it can

#########################################
'''assigment for iris dataframe'''
#data dictonary df.columns
from scipy.stats import skew
from scipy.stats import kurtosis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#read the dataset
df=sns.load_dataset('iris')
df.head() 
df=pd.read_csv("C:/Data Science/1-python/iris.data.csv")
df.columns

df.describe()
#####################
# histgramp
plt.hist(df.sepal_length)
plt.hist(df.petal_length)
plt.hist(df.sepal_width)
plt.hist(df.petal_width)
#######################
#displot
sns.displot(x='sepal_length',kde=True,bins=6,data=df)
sns.displot(x='sepal_width',kde=True,bins=6,data=df)
sns.displot(x='petal_length',kde=True,bins=6,data=df)
sns.displot(x='petal_width',kde=True,bins=6,data=df)
######################
#boxplot
df.describe()
sns.boxplot(df.sepal_length)
plt.boxplot(df.sepal_length)
sns.boxplot(df.sepal_width)
sns.boxplot(df.petal_width)
sns.boxplot(df.petal_length)

###############################3
#skweness
sepaleng_lst=df['sepal_length'].tolist()
sepaleng_lst
print("skewness of the speed",skew(sepaleng_lst))

###
sepalwidth_lst=df['sepal_width'].tolist()
sepalwidth_lst
print("skewness of the speed",skew(sepalwidth_lst))

############
petaleng_lst=df['petal_length'].tolist()
petaleng_lst
print("skewness of the speed",skew(petaleng_lst))
##############
petalwidth_lst=df['petal_width'].tolist()
petalwidth_lst
print("skewness of the speed",skew(petalwidth_lst))

######################3
#distribution plot
sns.displot(x='sepal_length',kde=True,bins=5,data=df)
#
sns.displot(x='sepal_width',kde=True,bins=5,data=df)
#
sns.displot(x='petal_length',kde=True,bins=5,data=df)
#
sns.displot(x='petal_width',kde=True,bins=5,data=df)
#########################
# count plot
sns.countplot(x='sepal_length',data=df)
# add hue
sns.countplot(x='species',hue='sepal_length',data=df,palette='Set1')
##########################3
# kdeplot 
sns.kdeplot(x='sepal_length',data=df,color='black')

####################3
#scatter plot
sns.scatterplot(x='sepal_length',y='petal_length',data=df)
#######################
#joint plot
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg') 
############################3
#pair plot
sns.pairplot(df)
##################
#heatmap is used to visualitation of the data
corr=df.corr()
sns.heatmap(corr)
