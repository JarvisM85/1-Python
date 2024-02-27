#Date ==> 11/08/2023

###########     Matplotlib     ################
#            =================               #

import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.show()


#Multiline plots
import matplotlib.pyplot as plt
x =range(2,5)
plt.plot(x, [xi*1.5 for xi in x],color='g')

plt.plot(x, [xi*3.0 for xi in x],color='r')

plt.plot(x, [xi/3.0 for xi in x],color='b')

plt.show()

#############################################
#Grid,axes, and labels
#Adding a grid
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.grid(True)
plt.show()

#####################
#Handling axes :=>
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)

plt.axais()  #shows the current axis limits values

plt.axis([0,5,-1,13])  # set new axes limits
# [xmin , xmax , ymin , ymax ]
# [ 0 , 5 , -1 , 13]

plt.show()

############################
#Adding labels ::=>
import matplotlib.pyplot as plt
plt.xlabel("This is the X axis")
plt.ylabel("This is the Y axis")
plt.show()


###################################################
#Adding a title => 
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.title('Simple Plot')
plt.show()
#MatplotLib provides a simple function,plt.title(),to

################################################
#Adding legend 
import matplotlib.pyplot as plt
import numpy as np
x =np.arange(1,5)
plt.plot(x, x*1.5 ,label='Normal')
plt.plot(x, x*1.5 ,label='Fast')
plt.plot(x, x*1.5 ,label='Slow')
plt.legend()
plt.show()

####################################
#Control Colors
'''
   COLOR abbrevations ==>
   ----------------------
   COLOR       NAME
     b         blue
     c         cyan 
     g         green 
     k         black
     m        magenta
     r         red
     w        white
     y        yellow
 '''

import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y')
plt.plot(y+1,'m')
plt.plot(y+2,'c')
plt.show()

##################
#Specifying styles in multiline plots
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y',y+1,'m',y+2,'c');
plt.show()

##############################

#Control line styles
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'--',y+1,'-.',y+2,':');
plt.show()


'''
   Style abbrevation
    -     solid line
   --     double dash
   -.      dash dot 
   :      dotted line
      
   '''

###############################################

'''
Marker abbrevations
   
'''



import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3,0.2)
plt.plot(y,'x',y+0.5,'o',y+1,'D',y+1.5,'^',y+2,'s')
plt.show()

#######################################
# Histogram Charts
import matplotlib.pyplot as plt
import numpy as np
y = np.random.randn(1000)
plt.hist(y);
plt.grid()
plt.show()

####################
# Bar plots
import matplotlib.pyplot as plt
import numpy as np
plt.bar([1,2,3],[3,2,5]);
#plt.bar([1,2,3],[3,2,5],color='r');
plt.show()



#Scatter Plots (Also called as Bivarient analysis)
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x,y)
plt.show()

##
size = 50*np.random.randn(1000)
colors = np.random.rand(1000)
plt.scatter(x,y,s=size,c=colors);
plt.show()

###################3
#Adding text
import matplotlib.pyplot as plt
import numpy as np
X = np.linspace(-4,4,1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)
plt.text(-0.5,-0.25, 'Brackmard minimum')
plt.plot(X,Y,c='k')
plt.show()









