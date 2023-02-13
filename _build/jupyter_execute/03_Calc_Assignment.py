#!/usr/bin/env python
# coding: utf-8

# # Review: Definite Integral
# 
# **OBJECTIVES**
# 
# - Use summation notation 
# - Solve basic probability problems 
# - Use Riemann Summations to approximate area
# - Use Definite Integrals to solve area problems
# - Use Definite Integrals to solve Net Change problems
# 
# ------

# ## Problem I: Summation Notation
# 
# 1. Evaluate $\sum_{i = 1} ^ 5 3i^2 - 2$.
# 2. Rewrite in summation notation: $1 + 3 + 5 + 7 + 9$
# 3. Use a formula to determine $\sum_{i = 1}^{50} i^3 - i$

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Problem II: Probability Problems
# 
# 1. What is the probability that in 20 coin flips we get 9 Heads -- assuming a fair coin. 
# 2. Explain what the 21's mean in the triangle below:
# 
# ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/23050fcb53d6083d9e42043bebf2863fa9746043)
# 
# 3. What does the following code mean?
# 
# ```python
# import scipy.stats as stats
# d = stats.binom(10, .4)
# d.pmf(4)
# ```
# 
# 
# 

# In[ ]:





# 4. The plot below represents the distribution of burrito ratings in New York City on Google.  What does the shaded area represent in terms of probabilities?

# In[2]:


N = stats.norm(5, 1.5)
x = np.linspace(0, 10, 1000)
plt.plot(x, N.pdf(x))
plt.fill_between(x, N.pdf(x), where = x > 6)
plt.title('Area under Normal Distribution\nwhere $x > 6$');


# 5. Compute the area above using the distribution `N`.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Problem III: Riemann Sums
# 
# 1. Write a formula for the area approximations below for $R(6)$ (b) in the image below where $f(x) = \frac{x^2}{2}$. Evaluate.
# 2. Write a formula for the area approximation in the image below for $L(6)$ (a) where $f(x) = \frac{x^2}{2}$. Evaluate. 
# 
# 
# ![](https://openstax.org/resources/d966b9a6dd578072e41c3ddc3447f8894861f3d0)
# 
# 3. Evaluate $L(6)$ for $f(x) = \frac{1}{x(x - 1)}$ on $[2, 5]$. 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Problem IV: Definite Integral 
# 
# 1. What does $\int_0^3 \sqrt{x} ~dx$ mean?
# 2. Evaluate the integral $\int_0^3 \sqrt{x} ~dx$.
# 3. Find the area under the curve $f(x) = x^4$ from $x = 1$ to $x = 4$.  Plot the region.
# 4. Plot the line $y = x$ on $[-2, 2]$. Evaluate the definite integral $\int_{-2}^2 x ~dx$ and interpret your results.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Problem V: Net Change Theorem
# 
# 1. Given a velocity function  $v(t) = 5t - 1$  (in meters per second) for a particle in motion from time  $t = 0$  to time  $t = 4$,  find the net displacement of the particle.
# 2. Find the total distance traveled of the particle above.
# 3. If the motor on a motorboat is started at  $t = 0$  and the boat consumes gasoline at the rate of  $7 - t^3$  gal/hr, how much gasoline is used in the first  3  hours?
