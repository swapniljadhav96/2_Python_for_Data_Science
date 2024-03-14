# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:57:42 2024

@author: suraj
"""

################################################
#matplotlib library:-  tell about the only graph
import  matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show()
#it can show the graph

#################################################
#mulitline plots
import matplotlib.pyplot as plt
x=range(1,5)
plt.plot(x,[xi*1.5 for xi in x])

plt.plot(x,[xi*3.0 for xi in x])

plt.plot(x,[xi/3.0 for xi in x])

plt.show()
#matplotlib take the coluor from itself
##############################
#grid,axes,label
#adding the grid
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,x*3.0,x/3.0)
plt.grid(True)
plt.show()
####2nd
 #of the grid
import matplotlib.pyplot as plt
x=range(1,5)
plt.plot(x,[xi*1.5 for xi in x])

plt.plot(x,[xi*3.0 for xi in x])

plt.plot(x,[xi/3.0 for xi in x])
plt.grid(True)
plt.show()

#################################
# how to handle access (axis)
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,x*3.0,x/3.0)
plt.axis()  #shows the current axis limit values
plt.axis([0,5,-1,13])   # set the new axis
#([0,5,-1,13])=[xmin,xmax,ymin ,ymax]
#[0,5,-1,13]
plt.show()
###################################
#adding the label :- it can give the label to the axis by using the label maethod
#.xlabel give the label to x axis and .ylabel give the label to y axis 
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.xlabel("this is X axis")
plt.ylabel('this is the y axis')
plt.show()
#
#################################
#adding the title
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.title('Simple plot')
plt.show()
# it can add the title to the graph
#################################
#adding legend:- means give the name to the plot
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5 ,label='Normal')

plt.plot(x,x*3.0,label='Fast')

plt.plot(x,x/3.0,label='Slow' )
plt.legend()
plt.show()

###################################
#control the color:-various are avaible
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y');

plt.plot(y+1,'m');

plt.plot(y+2,'c');
plt.show()
##################################
#specifing the  style in multiline plot
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y',y+1,'m',y+2,'c');
plt.show()

#############################
#abberi
#contol line style
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'--',y+1,'-.',y+2,':');
plt.show()
#####################################
#marker:-  adding the some symbol
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3,0.2)
plt.plot(y,'x', y+0.5,'o', y+1,'D', y+1.5,'^', y+2,'s');
plt.show()
########## #######################
#histogram charts:- it is important in the everey data science frame
#it is basically used to the distribution
import matplotlib.pyplot as plt
import numpy as np
y=np.random.randn(1000)
plt.hist(y);
plt.show()
##########################
#bar() Graph or function:- univaarient  anlysys
import matplotlib.pyplot as plt
plt.bar([1,2,3],[3,2,5]);
plt.show()
'''the bar() function is used to generate bar charts in matplotlib.pyplot
##[1,2,3]point at which your bar has started,[3,2,5] bar graph are ended
'''

#################################
#scatter plot is also call bivarient graph
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()

##########################
#change the colour of the scatter graph
size=50*np.random.randn(1000)
colors=np.random.randn(1000)
plt.scatter(x,y,s=size,c=colors);
plt.show()
##########################
#adding the text
import numpy as np
import matplotlib.pyplot as plt
X=np.linspace(-4,4,1024)
Y=.25*(X+4)*(X+1)*(X-2)
plt.text(-0.5,0.25,'Background minimize')
plt.plot(X,Y,c='k')
plt.show()

#############################33



