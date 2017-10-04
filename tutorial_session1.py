
# coding: utf-8

# In[225]:

import matplotlib.pyplot as plt
import numpy as np


#matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB. 
#Each pyplot function makes some change to a figure: e.g., creates a figure,
#creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc


# In[226]:

#check np.random at https://docs.scipy.org/doc/numpy/reference/routines.random.html


# In[293]:

#Draw random samples from a normal (Gaussian) distribution.

mu, sigma = 1, 1 # mean and standard deviation
sample = np.random.normal(mu, sigma, 1000)   #1000 is the size


# In[294]:

#sample


# In[295]:

#the histogram of the data https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.hist.html
#what is bin http://www.statisticshowto.com/what-is-a-bin-in-statistics/
count, bins, patches = plt.hist(sample, 30, normed= True, facecolor='blue')

#normed: If False, the result will contain the number of samples in each bin. 
#If True, the result is the value of the probability density function at the bin, 
#normalized such that the integral over the range is 1.

#patchesis the individual patches used to create the histogram, e.g a collection of rectangles
#bins: is the left hand edge of each bin


# In[296]:

# add a 'best fit' line 
#mlab.normpdf Return the normal probability density function evaluated at x; args provides mu, sigma
y = mlab.normpdf(bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)
## 'r--' red dashes, 'bs'blue squares and 'g^'green triangles
plt.xlabel('some random x lable')
plt.ylabel('some random y lable')
plt.grid(True)

plt.show()
#Display a figure. When running in ipython with its pylab mode, 
#display all figures and return to the ipython prompt.


# In[254]:

mu, sigma = 100, 15 # mean and standard deviation
x = mu + sigma*np.random.randn(10000) #Return a sample (or samples) from the “standard normal” distribution.

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)  #alpha = transparency 

# add a 'best fit' line
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.show()


# In[82]:

from pylab import *
from scipy.optimize import curve_fit


# In[268]:

c=normal(1,.2,5000)


# In[84]:

data=concatenate((normal(1,.2,5000),normal(2,.2,2500)))  #joining 
data


# In[91]:

y,x,_=hist(data,100,alpha=.3,label='data')

plt.xlabel('some random x lable')
plt.ylabel('some random y lable')
plt.title('some random bimodal')
#add the best fit line
plt.plot(x,bimodal(x,*params),color='red',lw=3)
plt.show()


# In[264]:

##another example

sample = np.random.normal(mu, sigma, 1000)


# In[265]:

sample2 = np.random.normal(mu, sigma, 1000)


# In[297]:

data=concatenate((sample,sample2))    


# In[298]:

y,x,_=hist(data,100,alpha=.3,label='data')

plt.xlabel('some random x lable')
plt.ylabel('some random y lable')
plt.title('some random bimodal')
#add the best fit line
plt.plot(x,bimodal(x,*params),color='red',lw=3)
plt.show()


# In[ ]:



