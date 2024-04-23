#!/usr/bin/env python
# coding: utf-8

# In[129]:


# 2.4 Python Exercise: Analyzing S&P 500 Futures Logarithmic Returns Distribution with Standard Deviation Lines

# Objective: Use Python to download the front month S&P500 futures prices, calculate the daily logarithmic returns, and create a histogram to visualize these
# returns. Enhance the histogram by adding vertical lines to represent the mean and standard deviations (one, two, and three standard deviations away from
# the mean) on both sides.
    
# Requirements:
# • Python
# • Libraries: pandas, numpy, yfinance, matplotlib

# Instructions:
# 1. First, ensure you have the necessary Python libraries (pandas, numpy,
# yfinance, and matplotlib). Install them using pip if they’re not already
# installed.

# 2. Import the required libraries in your Python script.
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# 3. Utilize the ‘yfinance‘ library to download the front month S&P500 futures price data. Store the downloaded data in a DataFrame.
sp500_futures = yf . download ('ES=F')
# 4. Calculate the daily logarithmic returns of the S&P500 futures prices. To do this, use the natural logarithm (‘np.log()‘) of the ’Adj Close’ price
# divided by its previous day’s value. The ‘diff()‘ method may be helpful here.
sp500_futures['Log_Returns'] = np.log(sp500_futures['Adj Close'] / sp500_futures['Adj Close'].shift(1))
# 5. Compute the mean of the logarithmic returns using the ‘.mean()‘ method, and store it in a variable named ‘mean return‘.
mean_return = sp500_futures['Log_Returns'].mean()
# 6. Calculate the standard deviation of the logarithmic returns using the ‘.std()‘ method. The code snippet for this and the following steps is provided:
std_return = sp500_futures ['Log_Returns']. std ()
# Adding vertical lines for mean and standard deviations
plt . axvline ( mean_return , color ='black', linestyle ='dashed', linewidth =2 , label =" Mean Return ")
for i in range (1 , 4) :
    plt . axvline ( mean_return + i * std_return , color ='green', linestyle ='dashed', linewidth =1 , label =f"+{i} STD ")
    plt . axvline ( mean_return - i * std_return , color ='red',linestyle ='dashed', linewidth =1 , label =f" -{i} STD ")

# 7. Determine the number of bins for the histogram based on the range of the logarithmic returns. Consider using ‘np.round()‘ to round the maximum
# and minimum log returns and then calculate the number of bins.
min_return = np.round(sp500_futures['Log_Returns'].min(), 2)
max_return = np.round(sp500_futures['Log_Returns'].max(), 2)
num_bins = int((max_return - min_return) * 70)  # Adjust for finer granularity

# 8. Create a histogram of the logarithmic returns using ‘plt.hist()‘. Ensure to label it appropriately.
plt.hist(sp500_futures['Log_Returns'], bins=num_bins, color='skyblue', edgecolor='black', alpha=0.7)

# 9. Add the vertical lines for the mean and standard deviations on the histogram, using the provided code snippet.
plt.axvline(mean_return, color='black', linestyle='dashed', linewidth=2, label="Mean Return")
for i in range(1, 4):
    plt.axvline(mean_return + i * std_return, color='green', linestyle='dashed', linewidth=1, label=f"+{i} STD")
    plt.axvline(mean_return - i * std_return, color='red', linestyle='dashed', linewidth=1, label=f"-{i} STD")
# 10. Configure your plot with a title, labels for the x-axis and y-axis, and a legend. Set the y-axis scale to logarithmic and format the y-axis labels to
# display integers.
plt.title('S&P 500 Futures Logarithmic Returns Distribution')
plt.xlabel('Logarithmic Returns')
plt.ylabel('Frequency')
plt.legend()
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(plt.ScalarFormatter())
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))
# 11. Finally, display the plot using ‘plt.show()‘.
plt.show()

# In this exercise, you will visually analyze the distribution of the S&P 500
# Futures Logarithmic Returns and understand how the returns deviate from the
# mean, providing insight into the volatility of the asset.


# In[ ]:





# In[ ]:





# In[ ]:




