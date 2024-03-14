# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:24:06 2024

@author: suraj
"""


#write the python program to draw plot 2 or more  lines with legends ,differnt widhth and 
#and change te color of the graph
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,50]
#line 2 points
x2=[10,20,30]
y2=[40,10,30]
#set the x aixs lable to current axis
plt.xlabel('x- axis')
#set the y axis label to of the current axis
plt.ylabel('y-axis')
#set the title
plt.title("two or more line with the difffernt widths and colours with suitable legends")
#display the figure
plt.plot(x1,y1, color='blue',linewidth=3 , label = 'line1-width-3')
plt.plot(x2,y2, color='red', linewidth=5 , label = ' line2-width-5')
#show the legend on the plot
plt.legend()
plt.show()
#########################################################
#write the python program to plot two or more line and set the line markers 
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,50]
#line 2 points
x2=[10,20,30]
y2=[40,10,30]
#set the x aixs lable to current axis
plt.xlabel('x- axis')
#set the y axis label to of the current axis
plt.ylabel('y-axis')
#set the title
plt.title("plot with two or more line with the difffernt  styles")
#display the figure
plt.plot(x1,y1, color='blue',linewidth=3 , label = 'line1-dotted', linestyle = 'dotted')
plt.plot(x2,y2, color='red', linewidth=5 , label = ' line2-dashed' , linestyle ='dashed')
#show the legend on the plot
plt.legend()
plt.show()
###############################################################
#Write the python program to plot two or more lines and set the line markers(trigular star line marker cirule)
import matplotlib.pyplot as plt
#x axis values
x=[1,4,5,6,7]
#y axis values
y=[2,6,3,6,3]

#plotting the point
plt.plot(x,y, color='red',linestyle='dashdot',linewidth=3, marker='o'
         , markerfacecolor='blue',markersize=12)
#linestyle ,linewidth,marker,markerfacecolour,markersize
#set the y-limite of the current axis
plt.ylim(1,8)                   #y limit  give the using the ylim
#set the x limit of the current axis
plt.xlim(1,8)                   #x limit give  using the xlim
#naming the x axis
plt.xlabel('x-axis')
#namig the y axis
plt.ylabel('y-axis')
#giving the title to my graph
plt.title("display markers")
#function to show the plot
plt.show()
#############################################
#Write a python program to plot several lines with different format styles in one command array
import numpy as np
import matplotlib.pyplot as plt

#sampled time at 200ms intervals
t = np.arange(0.,5. ,0.2)

#green dashes ,blue squares and red triangles
plt.plot(t,t, 'g--',t,t**2,'bs',t , t**3,'r^')
#giving the title to my graph
plt.title("dispalying the  interval")
plt.show() 

#hrere the t ,t and t**2 ,t and t**3 , t are line equation
#################################################
#write the python pragram to dispaly a bar chart of the popularity of programming 
#language 
import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos= [i for i,_ in enumerate(x)]      #_ is variable means it take one by one letter from the x with its corresponding index
#enumerate is used to check or access the keys and values from the given list  
plt.bar(x_pos,popularity,color='blue')
plt.xlabel("langauge")      #x label
plt.ylabel("popularity")    #y label
plt.title("Populartiy of the proramming langaure\n"+"worldwide ,oct 2017 compared to a year")
plt.xticks(x_pos,x)     #graph in horizontal and vertical yoou can use the yticks
plt.show()
#xticks and yticks change only the x label and y label parameter of  the both the axis and all the 
#parmeter was on the x will goes on the y axis and all the label or parametr on the y  will be goes on the x axis

##################################################
#write  apython program to dispaly a horizonatl bar chart of the popularity of proramming language
import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos= [i for i,_ in enumerate(x)]      #_ is variable means it take one by one letter from the x with its corresponding index
#enumerate is used to check or access the keys and values from the given list  
plt.barh(x_pos,popularity,color='green')
plt.xlabel("popularity")      #x label
plt.ylabel("language")    #y label
plt.title("Populartiy of the proramming langaure\n"+"worldwide ,oct 2017 compared to a year")
plt.yticks(x_pos,x)     #graph in horizontal and vertical yoou can use the yticks
plt.show()
#######################################################
#write a pyhton program to create bar plot of score by group and gender
import numpy as np
import matplotlib.pyplot as plt
#data to plot
n_groups=5
men_means=(22,33,30,30,26)
women_means=(25,32,30,35,29)
#create the plot
fig,ax=plt.subplots()       #one plot so fig,ax #2 subplot then fig,ax,ax
index=np.arange(n_groups)
bar_width=0.35
opacity=0.8

rects1=plt.bar(index,men_means,bar_width,alpha=opacity,color='g',label='Men')
rects2=plt.bar(index+bar_width,women_means,bar_width,alpha=opacity,color='r',label='Women')

plt.xlabel('Person')
plt.ylabel("Scores")
plt.title('Scores by person')
plt.xticks(index + bar_width , ('G1','G2','G3','G4','G5')) 
plt.legend()
plt.tight_layout()
plt.show()









