#!/usr/bin/env python
# coding: utf-8

# ### Sequences and Summations
# 
# **Objectives**
# 
# - Generate terms of a binomial sequence
# - Form sequences of partial sums
# - Look for patterns in partial sums
# 
# 

# #### Problem: Sennett
# 
# An ancient egyptian game of sennet involves dropping two colored sticks and moving a board piece based on the resulting stick color combination.  Your goal is to complete the table below, and determine the number of ways for each outcome for 3, 4, and 5 sticks to occur.
# 
# | num sticks | 0 red | 1 red | 2 red | 3 red | 4 red | 5 red |
# | ---------- | ----- | ----- | ----- | ------ | ----- | ------ |
# | 1 | 1 | 1 | -- | -- | -- | -- |
# | 2 | 1 | 2 | 1 | -- | -- | -- |
# | 3 | $~$ | $~$ | $~$ | $~$ | $~$ | $~$ |
# | 4 | $~$ | $~$ | $~$ | $~$ | $~$ | $~$ |
# | 5 | $~$ | $~$ | $~$ | $~$ | $~$ | $~$ |

# #### Problem: Partial Sums
# 
# Given the sequence below, we aim to evaluate the sum of a sequence and form a sequence based on these sums.  For example, take the sequence:
# 
# $$a_n = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1$$
# 
# the sequence formed by the sum of the first $n$ terms would be:
# 
# $$s_n = 1, 2, 3, 4, ... $$
# 
# Your goal for each of the following sequences is to create a sequence of partial sums, and try to generate a recursive and closed form definition of that sequence of sums.

# 1. $a_n = 1, 2, 3, 4, 5, ...$
# 2. $a_n = 1^3, 2^3, 3^3,  4^3$
# 
# - [Sheet Link](https://docs.google.com/spreadsheets/d/1XsjVmyh_N6fI60VSu4_FL0dq68eAVTg_RhfbpjRE8Ms/edit?usp=sharing)

# ### The Big Idea and Notation
# 
# Create a sequence, and create a sequence from sums of the terms of the sequence.  Let's move to a slightly different expression of these ideas where we form sequences based on functions defined in closed form.  For each of the examples below use:
# 
# $$x = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10$$
# 
# to evaluate the given function $f$.  Create a spreadsheet and visualize $f(x)$.  Next, create a sequence of partial sums on the same sheet and plot the sequence of partial sums alongside the functions.  
# 
# 1. $f(x) = 1$
# 2. $f(x) = x$
# 3. $f(x) = x^2$
# 4. $f(x) = x^3$
# 5. $f(x) = x^4$

# ### Using Python and Notebooks

# While google sheets are nice, and there are many spaces that you may use a spreadsheet -- we want to move to some more powerful and flexible tools.  To begin, we aim to use Python to perform the operations we have used to this point.  These are:
# 
# - Define and use functions
# - Visualize functions
# - Form sequences of partial sums in Python

# #### Some Basics
# 
# - Addition: `+`
# - Subtraction: `-`
# - Multiplication: `*`
# - Division: `/`
# - Exponents: `**`

# In[1]:


#addition
3 + 4


# In[2]:


#subtraction
3 - 8


# In[3]:


#multiplication
2*10


# In[4]:


#division
10/3


# In[5]:


#exponents
2**4


# #### Defining functions
# 
# ```python
# def f(x):
#     return x**2
# ```
# 
# The above code defines a function that will take in a number and return its square.  After running a code cell with this definition you can use the function with `f(2)`.

# In[6]:


#define a function
def f(x):
    return x**2


# In[7]:


#use the function
f(2)


# Use the functions defined below to evaluate the following:
# 
# 1. $f(0)$
# 2. $g(0)$
# 3. $f(10)$
# 4. $g(.10)$
# 5. $g(0)$

# In[8]:


def f(x):
    return x - 4

def g(x):
    return 1/x


# In[9]:


#f(0)


# In[10]:


#g(0)


# In[11]:


#f(10)


# In[12]:


#g(.1)


# In[13]:


#g(0)


# #### Libraries and Plotting
# 
# To create domains for our functions, we will use a library called `numpy`.  To visualize the functions, we will use a library called `matplotlib`.  In order to make use of these we first import and alias them below.

# In[14]:


import matplotlib.pyplot as plt
import numpy as np


# First, we will use numpy to create a domain as we did earlier with
# 
# ```python
# x = np.arange(1, 11)
# ```

# In[15]:


np.arange(1, 11)


# In[16]:


np.arange(1, 11, .5)


# In[17]:


np.arange(0, 1, .1)


# In[18]:


#define the function
def f(x):
    return x**2
#define the domain
x = np.arange(1, 11)
#evaluate function on domain
f(x)


# #### Problems
# 
# For each of the following, use python and numpy to define and evaluate the functions on the given domain.
# 
# 1. $f(x) = x^2 + 3x + 1$ where $x1 = [0, 1, 2, 3, 4]$
# 2. $g(x) = 1/x$ where $x2 = [1, 2, 3, 4, 5, 6, 7, 8]$
# 3. $h(x) = x^3$ where $x3 = [0, .1, .2, ..., 1.9, 2.0]$

# In[19]:


#define f

#define x1


# In[20]:


#define g

#define x2


# In[21]:


#define h

#define x3


# ### Plotting Functions with `matplotlib`
# 
# To plot a given function, use `plt.plot(x, y)`.  This produces a basic plot of a function or sequence.  Below, the functions and domains from the previous three problems will be used to create plots below.

# In[22]:


#plt.plot(x1, f(x1))


# In[23]:


#plt.plot(x2, g(x2))


# In[24]:


#plt.plot(x3, h(x3))


# #### Computing Parital Sums
# 
# To compute the partial sums of a sequence, use the `np.cumsum` function.  This computes the cumulative sum of a given sequence.  

# In[25]:


def f(x): return x
x = np.arange(1, 11)
np.cumsum(x)


# In[26]:


plt.plot(x, np.cumsum(f(x)), '-o')


# #### Summary
# 
# Today, we began using partial sums to form new sequences from old.  You want to get practice defining and plotting functions in python as we had above.  Below are additional examples to use as practice with defining and plotting functions.

# 1. $f(x) = \frac{x-2}{3x + 8}$
# 2. $f(x) = 9$
# 3. $f(x) = (x - 4)^2 + 5$
# 4. $f(x) = \sqrt{x^2 - 3x}$

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




