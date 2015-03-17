#P-value
import matplotlib.pyplot as plt 
from random import gauss 

#######
X_ran,Y_ran = [gauss(0,1) for i in range(500)],[gauss(0,1) for i in range(500)]
#######
#plt.plot(X_ran,Y_ran,'x')
#plt.show()

#######
X_col = [gauss(0,1) for i in range(500)]
Y_col = [gauss(0,1)+x for x in X_col]
#######
#plt.plot(X_col,Y_col,'x')
#plt.show()


import numpy as np
import matplotlib.mlab as mlab
import math

mean = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(-6,6,100)
plt.plot(x,mlab.normpdf(x,mean,sigma))

plt.show()