#!/usr/bin/env python
# coding: utf-8

# In[12]:


# 2.2 Python Exercise: Downloading S&P500 Futures Prices and Calculating Annualized Volatility

# Objective: Download the front month S&P500 futures prices, compute the logarithmic returns, and then calculate the annualized volatility.

# Requirements:
# • Python
# • Libraries: pandas, numpy, yfinance

# Steps:
# 1. Install Required Libraries: Ensure you have the necessary libraries
# installed. Install them using pip if needed:
# pip install pandas numpy yfinance

# Import libraries
import pandas as pd
import numpy as np
import yfinance as yf

# Downloading S&P 500 front month futures price data using yfinance
sp500_futures = yf . download ('ES=F')

# Calculate the daily logarithmic returns
sp500_futures['Log_Returns'] = np . log ( sp500_futures['Adj Close'] / sp500_futures['Adj Close']. shift (1) )

# Calculate the standard deviation ( volatility ) of the logarithmic returns
volatility = sp500_futures['Log_Returns']. std ()

# Annualize the volatility
# There are approximately 252 trading days in a year
annualized_volatility = volatility * np . sqrt (252)
print (" Annualized Volatility :", annualized_volatility )


# In[ ]:




