#!/usr/bin/env python
# coding: utf-8

# In[96]:


# 1.5 Python Exercise: S&P 500 Futures Data Analysis

# In this exercise, you will apply the concepts of calculating and visualizing returns
# to real-world financial data. You will download daily data of S&P 500 front
# month futures from Yahoo Finance and perform a similar analysis as above.

# 1.5.1 Downloading the Data
# Requirements:
# • Python
# • Libraries: pandas, numpy, matplotlib, yfinance
# yfinance
# To get started, you need to download the daily price data for S&P 500
# futures. This can be done using Python’s pandas and yfinance libraries. Here
# is a step-by-step guide to download the data and put it into a pandas datagram:
#!pip install yfinance

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib . pyplot as plt

# Downloading S&P 500 futures data
ticker = "ES=F" # S&P 500 front - month futures ticker symbol
data = yf . download ( ticker )

# Creating a pandas dataframe
sp500_data = pd . DataFrame ( data )
print ( sp500_data . head () ) # Displaying the first few rows

# 1.5.2 Your Task

# Using this data, calculate and plot the annual arithmetic and logarithmic returns
# of the S&P 500 futures. Then, analyze the cumulative returns over the entire
# period. You should:

# 1. Calculate and Plot Cumulative Returns: Similar to the previous
# exercise, calculate the cumulative arithmetic and logarithmic returns for
# the S&P 500 futures data.

 # Calculating arithmetic and logarithmic returns
arithmetic_returns = sp500_data['Adj Close'] / sp500_data['Adj Close'].shift(1) - 1
log_returns = np . log ( sp500_data['Adj Close'] / sp500_data['Adj Close'].shift(1))

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

# 2. Compare and Discuss: Analyze the plots and discuss the visual differences. What insights can you gain about the performance of the S&P 500
# futures over this period?

# The first graph have so much data that it is hard to compare two points at a moment t. However we can say that both returns seem to have the same shape. Boxplots may have
# been more useful at comparing both returns. On Outliers, we can still note that each log return seems to be below each arithmetic return, which makes sense.
# We can also note a higher volatility of returns in 2009 and 2020.

# On the second graph, we see that until 2020, the cumulative arithmetic return outperformed, and that since then the cumulative log returns outperforms.
# This can be explained by the higher volatility from this period. Cmulative arithmetic retrns tend to cancel price swings whereas 
# cumultative log return account accurately for the impact of price swing. Ex, Price of 1, then 0.9, then 1.1. Cumulative Arithemtic return is Null (-0.1+0.1) 
# while log is about 10% : SUM(LOG(0.9),LOG(1.1))


# In[ ]:





# In[ ]:





# In[ ]:




