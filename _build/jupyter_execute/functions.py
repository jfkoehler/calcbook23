#!/usr/bin/env python
# coding: utf-8

# # Functions

# <center>
#     <img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Function_machine2.svg/440px-Function_machine2.svg.png" width = 40%/>
# </center>

# **Definition**
# 
# *In mathematics, a function is a binary relation between two sets that associates every element of the first set to exactly one element of the second set. Typical examples are functions from integers to integers, or from the real numbers to real numbers.*
# 

# ### Starting with Sequences
# 
# > *In mathematics, a sequence is an enumerated collection of objects in which repetitions are allowed and order matters. Like a set, it contains members (also called elements, or terms). The number of elements (possibly infinite) is called the length of the sequence. Unlike a set, the same elements can appear multiple times at different positions in a sequence, and unlike a set, the order does matter. Formally, a sequence can be defined as a function from natural numbers (the positions of elements in the sequence) to the elements at each position.*

# ### Examples of Sequences
# 
# Below, sequences are displayed visually.  
# 
# - Determine an expression for the number of white dots
# - Determine an expression for the number of black dots
# - Determine an expression for the number of total dots
# - Use your expression to determine how many white, black and total dots there would be in the 20th term of the sequence
# 
# ![](images/sequences_1.png)

# #### Problems
# 
# ![](images/sequence_2.png)

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Visualizing with Google Sheets
# 
# Now, we will use google sheets do define and visualize the first ten terms of our four sequence.  To do so, we will define our functions in **two** ways.  The first method for defining function is a *recursive* definition.  This explains how to get from a previous term in a sequence $a_n$ to the next term $a_{n+1}$.  

# Let's start with the first sequence:
# 
# $$a_n = 4, 9, 16, 25$$

# $$a_1 = 4$$
# $$a_2 = 4 + 5$$
# $$a_3 = 9 + 7$$
# $$a_4 = 16 + 9$$
# 
# The key here is determining a way to generalize the $5, 7, 9$ in terms of the index value $n$.  Let's try to figure out this expression and use it to define the sequence in sheets [here](https://docs.google.com/spreadsheets/d/1iC_gAnenRtXLrKoT83GFuMCv2M5dF4L6Mib8u0SFk_c/edit?usp=sharing).

# - **STEP 1**: Define the index
# 
# Set the first cell as 1.  Set the second cell below as equal to the previous cell plus one.  
# 
# ![](images/sheets1.png)

# - **Step 2**: Apply to 10 Cells
# 
# Drag the values through the first ten rows of the data using the small blue square in the corner of the second cell.
# 
# ![](images/sheets2.png)

# - **Step 3**: Define Sequence
# 
# Define the first term of the sequence in the second column.  In the second cell, define your rule based on the previous term and index value.
# 
# ![](images/sheets3.png)

# #### Problem
# 
# Use google sheets to plot sequences A - D above.

# ### Closed Form definition
# 
# An alternative approach to defining the sequences is to determine a rule in general where given the index value the function returns the term of the sequence.  For example, sequence A can be defined as:
# 
# $$f(n) = (n + 1)^2$$

# Use closed form definitions to define sequences E-H from above on the second sheet named *closed*.

# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:





# #### Summary
# 
# Today we examined tools for representing patterns of numbers using both *recursive* and *closed form* functions.  We used numbers, tables, and graphs to examine these.  Next class, we will dive deeper into sequences and functions and begin plotting and defining them using the Python computer language.

# 1. $a_n = [1, 3, 5, 7, 9]$
# 2. $a_n = [0, 3, 8, 15, 24]$
# 3. ![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/First_six_triangular_numbers.svg/440px-First_six_triangular_numbers.svg.png)
