
# coding: utf-8

# In[323]:

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

#matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB. 
#Each pyplot function makes some change to a figure: e.g., creates a figure,
#creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc


# In[324]:

#check np.random at https://docs.scipy.org/doc/numpy/reference/routines.random.html


# In[348]:

#Draw random samples from a normal (Gaussian) distribution.

mu, sigma = 1, 1 # mean and standard deviation

sample = np.random.normal(mu, sigma, 1000)   #1000 is the size

#try 1000,100,30,15


# In[347]:

min(sample), max(sample)


# In[294]:

#sample


# In[321]:

#the histogram of the data https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.hist.html
#what is bin http://www.statisticshowto.com/what-is-a-bin-in-statistics/
count, bins, patches = plt.hist(sample, 30, normed= True, facecolor='blue')

#normed: If False, the result will contain the number of samples in each bin. 
#If True, the result is the value of the probability density function at the bin, 
#normalized such that the integral over the range is 1.

#patchesis the individual patches used to create the histogram, e.g a collection of rectangles
#bins: is the left hand edge of each bin


# In[322]:

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


# In[354]:

##define range of the distribution


# In[365]:

X1 = get_truncated_normal(mean=25, sd=1, low=10, upp=50)
X2 = get_truncated_normal(mean=25, sd=1, low=10, upp=50)
X3 = get_truncated_normal(mean=25, sd=1, low=10, upp=50)

import matplotlib.pyplot as plt
fig, ax = plt.subplots(3, sharex=True)
ax[0].hist(X1.rvs(1000), normed=True)
ax[1].hist(X2.rvs(100), normed=True)
ax[2].hist(X3.rvs(30), normed=True)
plt.show()


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
#pylab is a module that gets installed alongside matplotlib 
from scipy.optimize import curve_fit
#Use non-linear least squares to fit a function, f, to data.


# In[300]:

np.random.normal(1,.2,5000)


# In[301]:

data=concatenate((np.random.normal(1,.2,5000),np.random.normal(2,.2,2500)))  #joining 
data


# In[302]:

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



