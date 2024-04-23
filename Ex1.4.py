#!/usr/bin/env python
# coding: utf-8

# In[31]:


# # 1.4 Python Exercise: Calculating and Visualizing Returns

# You are given a dataset representing the annual closing values of an investment
# portfolio over a five-year period with more volatile values. Calculate both the
# arithmetic and logarithmic returns for each year, the total returns over the entire period, and visualize the cumulative returns to see the difference visually.

# Annual closing values of the portfolio (in millions USD):

# • Year 0: $10.0
# • Year 1: $12.5
# • Year 2: $8.0
# • Year 3: $13.5
# • Year 4: $7.5
# • Year 5: $15.0

# 1.4.1 Calculate and Plot Annual Arithmetic and Logarithmic Returns

# Requirements:
# • Python
# • Libraries: pandas, numpy, matplotlib

import numpy as np
import matplotlib . pyplot as plt

# Updated portfolio values
values = np . array ([10.0 , 12.5 , 8.0 , 13.5 , 7.5 , 15.0])

 # Calculating arithmetic and logarithmic returns
arithmetic_returns = (values [1:] / values [: -1]) - 1
log_returns = np . log ( values [1:] / values [: -1])

# Plotting the returns
plt . figure ( figsize =(10 , 6) )
plt . plot ( arithmetic_returns , label ='Arithmetic Returns', marker ='o'
)
plt . plot ( log_returns , label =' Logarithmic Returns ', marker ='x')
plt . title ('Annual Arithmetic vs. Logarithmic Returns ')
plt . xlabel ('Year ')
plt . ylabel ('Returns ')
plt . legend ()
plt . grid ( True )
plt . show ()

#1.4.2 Calculate and Plot Cumulative Returns

# Calculating cumulative returns
cumulative_arithmetic_return = np . cumsum ( arithmetic_returns)
cumulative_logarithmic_return = np . exp ( np . cumsum ( log_returns )) - 1

# Plotting cumulative returns
plt . figure ( figsize =(10 , 6) )
plt . plot ( cumulative_arithmetic_return , label ='Cumulative Arithmetic Returns ', marker ='o')
plt . plot ( cumulative_logarithmic_return , label ='Cumulative Logarithmic Returns ', marker ='x')
plt . title ('Cumulative Arithmetic vs. Logarithmic Returns ')
plt . xlabel ('Year ')
plt . ylabel ('Cumulative Returns ')
plt . legend ()
plt . grid ( True )
plt . show ()

# 1.4.3 Compare and Discuss
# After plotting the returns, compare the graphs of arithmetic and logarithmic
# returns, as well as their cumulative returns. Discuss the visual differences and
# the implications of these differences for investment performance measurement.

print('''
On the first graph, we can observe that logarithmic returns are always lower than arithmetic returns. This is because
for any return (given non-negative prices) log(x) < x or log(a/b) < a/b - 1. This means that when tracking investments, one should
compare them on an the same basis (either log or arithmetic. And one should always remember to trasnform the logarithmic return to 
obtain the actual value of an investment at given time.

On the second graph, we can see a growing disparity between the cumulative returns. Arithmetic returns taking the lead.
This is a consequence of what we explaine din the previous paragraph : higher Arithmetic returns will lead to a higher cumulative compounding. 
However if we transform the log cumulative return at any point, it should be equal to arithemtic cumulative return.
''')


# In[ ]:





# In[ ]:




