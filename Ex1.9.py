#!/usr/bin/env python
# coding: utf-8

# In[21]:


# 1.9 Python Exercise: Downloading S&P500 Futures Prices and Calculating Annualized Mean Logarithmic Return
    
# Objective: Download the front month S&P500 futures prices, compute the
# logarithmic returns, and then annualize the mean return.

#     Requirements:
# • Python
# • Libraries: pandas, numpy, yfinance
# Steps:

# 1. Install Required Libraries: Ensure you have the necessary libraries
# installed. You can install them using pip:

# pip install pandas numpy finance

# Import libraries
import pandas as pd
import numpy as np
import yfinance as yf

# Use the ‘yfinance ‘ library to download the front month S&P500 futures price data .
sp500_futures = yf.download ('ES=F')

# Calculate the daily logarithmic returns of the futures prices .
sp500_futures['Log_Returns'] = np . log ( sp500_futures['Adj Close'] / sp500_futures['Adj Close']. shift (1) )

# Annualize the mean of the logarithmic returns .
annualized_return = sp500_futures['Log_Returns'].mean() * 252

print (" annualized_return :", annualized_return)


# In[ ]:




