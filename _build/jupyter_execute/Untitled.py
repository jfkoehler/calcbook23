#!/usr/bin/env python
# coding: utf-8

# ### Area and Approximation

# ![](wiggle.png)

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def f(x): 
    return -x**2 + 2


# In[3]:


x = np.linspace(-1.5, 1.5, 100)


# In[4]:


plt.xkcd()
plt.axhline(color = 'black')
plt.fill_between(x, f(x), color = 'turquoise')
plt.title('Approximate the area under $f(x) = -x^2 + 2$\nfrom $x = -1$ to $x = 1$', pad = 15)
plt.plot(x, f(x), color = 'black');
plt.savefig('wiggle.png', pad_inches = 13)


# In[ ]:





# In[ ]:





# #### Area and Patterns
# 
# 

# Area under $f(x) = \frac{1}{2}x$ from $x = 0$ to $x = 1$ with $n = 5$ rectangles.

# In[ ]:





# In[ ]:





# Area under $f(x) = \frac{1}{2}x$ from $x = 0$ to $x = 2$ with $n = 10$ rectangles.

# In[ ]:





# In[ ]:





# Area under $f(x) = \frac{1}{2}x$ from $x = 0$ to $x = 3$ with $n = 15$ rectangles.

# In[ ]:





# In[ ]:





# #### Problem 2

# Area under $f(x) = \frac{1}{3}x^2$ from $x = 0$ to $x = 1$ with $n = 5$ rectangles.

# In[5]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:





# In[ ]:





# In[ ]:





# Area under $f(x) = \frac{1}{3}x^2$ from $x = 0$ to $x = 2$ with $n = 10$ rectangles.

# In[ ]:





# In[ ]:





# In[ ]:





# Area under $f(x) = \frac{1}{3}x^2$ from $x = 0$ to $x = 3$ with $n = 15$ rectangles.

# In[ ]:





# In[ ]:





# In[ ]:





# Area under $f(x) = \frac{1}{3}x^2$ from $x = 0$ to $x = 4$ with $n = 20$ rectangles.

# In[ ]:





# In[ ]:





# In[ ]:





# #### Applications

# In[ ]:




