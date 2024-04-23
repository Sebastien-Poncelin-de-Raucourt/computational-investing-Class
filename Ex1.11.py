#!/usr/bin/env python
# coding: utf-8

# In[37]:


# 1.11 Python Exercise: Visualizing S&P 500 Futures Logarithmic Returns Distribution

# Objective: Download the front month S&P500 futures prices using the ‘yfinance‘ library, compute the daily logarithmic returns, and visualize the distribution of these returns 
# in a histogram. Additionally, plot a vertical dashed line to indicate the mean of the daily logarithmic returns.

# Requirements:
# • Python
# • Libraries: pandas, numpy, yfinance, matplotlib

# Steps:
# 1. Install Required Libraries: Ensure you have the necessary libraries
# installed. Install them using pip if needed:
# pip install pandas numpy yfinance matplotlib

# Import libraries
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib . pyplot as plt
import matplotlib . ticker as ticker

# Download front month S& P500 futures price data
sp500_futures = yf . download ('ES=F')

# Calculate daily logarithmic returns of the futures prices
sp500_futures['Log_Returns'] = np.log (sp500_futures['Adj Close']).diff()

# Determine the number of bins for the histogram
max_daily_return = np . round ( sp500_futures['Log_Returns'].max () , 2)
min_daily_return = np . round ( sp500_futures['Log_Returns'].min () , 2)
n_bins = int (( max_daily_return - min_daily_return ) * 100)

# Plot a histogram of the logarithmic returns
plt.hist(sp500_futures['Log_Returns'], bins = n_bins , color = 'orange', label =" Return Distribution ")

# Add a vertical dashed line to indicate the mean of the returns
plt . axvline ( sp500_futures['Log_Returns']. mean () , color ='black', linestyle ='dashed', linewidth =2 , label =" Daily Mean Return ")

# Configure the plot
plt . title ('Histogram of S&P 500 Futures Logarithmic Returns ')
plt . xlabel ('Logarithmic Returns')
plt . ylabel ('Frequency (log)')
plt . yscale ('log')
plt . gca () . yaxis . set_major_formatter ( ticker . StrMethodFormatter ('{x: ,.0f}')) # Format y- axis labels as integers
plt . legend ()

# Display the plot
plt . show ()


# In[ ]:





# In[ ]:




