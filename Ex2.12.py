#!/usr/bin/env python
# coding: utf-8

# In[53]:


# 2.12 Python Exercise: Calculating and Plotting Ongoing Drawdown of S&P 500 Futures

# Objective: Download front month S&P 500 futures prices, compute the logarithmic returns, calculate the cumulative return, and plot the ongoing drawdown
# with the ongoing drawdown represented as a red area.

# Requirements:
# • Python
# • Libraries: pandas, numpy, yfinance, matplotlib

# Steps:
# 1. Install Required Libraries: Ensure the necessary libraries are installed.
# Use pip to install them if needed:
# pip install pandas numpy yfinance matplotlib

# 2. Download Data and Calculate Returns:
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib . pyplot as plt

# Download S&P 500 front month futures data
sp500_futures = yf . download ('ES=F')

# Calculate logarithmic returns
sp500_futures ['Log_Returns'] = np . log (sp500_futures ['Adj Close'] / sp500_futures ['Adj Close']. shift (1))

# 3. Calculate Cumulative Returns and Ongoing Drawdown:
# Calculate cumulative returns
sp500_futures ['Cumulative_Returns'] = np . exp ( sp500_futures['Log_Returns']. cumsum () ) - 1

# Calculate ongoing drawdown
rolling_max = sp500_futures ['Cumulative_Returns']. cummax ()
sp500_futures ['Drawdown'] = rolling_max - sp500_futures ['Cumulative_Returns']

# Plotting the results
fig , ax = plt . subplots ()
ax . fill_between ( sp500_futures . index , sp500_futures ['Drawdown'], color='red', alpha=0.3)
ax . plot ( sp500_futures ['Cumulative_Returns'], label ='Cumulative Returns')
ax . set_title ('Cumulative Returns and Ongoing Drawdown')
ax.set_xlabel('Date')
ax . set_ylabel ('Returns / Drawdown')
ax.legend
plt.show()

#Find the max drawdown
max_drawdown=max(sp500_futures['Drawdown'].dropna())
print(f'the all-time maximum drawdown is {-round(max_drawdown,4)*100}%')


# In[ ]:





# In[ ]:




