#!/usr/bin/env python
# coding: utf-8

# ### Mathematical Models and More with Sequences
# 
# **Learning Objectives**
# 
# - Use closed form and recursive form definitions of sequences
# - Determine closed and recursive form given sequence terms
# - Use spreadsheets to model sequences
# 

# #### Problem 1: Money and Interest
# 
# Suppose you have \$500 dollars that you want to invest.  It is often said that the stock market generates an average 10% annual return. 
# 
# Complete the table linked below on the first sheet and create a google sheet with the first ten years of the balance on the account.  What is the total percent change in your balance over 10 years?
# 
# - [Starter](https://docs.google.com/spreadsheets/d/1BpMkBSYGCdnJhGhmN2KG0GWN65wtgqK6KNbrNTKUHJE/edit?usp=sharing)

# #### Problem 2: Sandhill Crane Population
# 
# > *The sandhill crane (Antigone canadensis) is a species of large crane of North America and extreme northeastern Siberia. The common name of this bird refers to habitat like that at the Platte River, on the edge of Nebraska's Sandhills on the American Great Plains. Sandhill Cranes are known to hangout at the edges of bodies of water especially in the Central Florida region. This is the most important stopover area for the nominotypical subspecies, the lesser sandhill crane (A. c. canadensis), with up to 450,000 of these birds migrating through annually.* -- [Wikipedia](https://en.wikipedia.org/wiki/Sandhill_crane)
# 
# Suppose the starting population of a sandhill crane community is 50 birds and each year this increases by 8.  How many birds will there be in 20 years?  Use the second sheet in the file to create a plot of this sequence.  What was the percent change in the population over the 20 years?
# 
# 

# #### Revisiting the Cranes
# 
# Perhaps these models don't tell the full story.  We haven't explored any different suppositions in population growth.  Suppose instead we aim to compare a lower growth rate with that above.  
# 
# - Use a growth rate of -.3 and of -.1 and examine the first 20 years of population for these new series.  Be sure to represent each of these as recurrence relationships and closed form formulas.

# #### A Different Population Model
# 
# Suppose the following definition of the crane population is given:
# 
# $$x_{n+1} = rx_n(1-x_n)$$
# 
# Simulate the first 20 years for growth rate $r$ = 0.5, 2.2, and 2.8.  What do you think about these models?  Use the sheet `logistic model` to explore these sequences and their behavior.

# #### PROBLEMS
# 
# 1. Create a new spreadsheet to generate the first 10 terms following sequences:
# 
# - $a_{n+1} = a_n + 5$ where $a_0 = 10$.  
# - $a_{n+1} = a_n - 3$ where $a_0 = 15$
# - $a_{n+1} = a_n + n$ where $a_0 = 2$
# - $a_{n+1} = a_n + 2n - 1$ where $a_0 = 3$
# 
# 2. In the same spreadsheet but on a new sheet, define and plot the following functions:
# 
# - $f(n) = 2n + 5$
# - $f(n) = -n + 10$
# - $f(n) = n^2  - n + 3$
# - $f(n) = n^2 - 1$
# 
# Discuss the similarities and differences between the two groups of sequences defined recursively and in closed form.  
# 

# In[ ]:




