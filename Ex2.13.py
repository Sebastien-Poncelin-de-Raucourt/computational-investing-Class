#!/usr/bin/env python
# coding: utf-8

# In[215]:


# 2.13 Python Exercise: Calculating and Plotting Ongoing Drawdown of a Mixed Portfolio

# Objective: Construct a portfolio with 60% weight in S&P 500 futures (ES=F)
# and 40% weight in US 10-year Treasury futures (ZN=F), calculate the logarithmic returns of the portfolio, compute the cumulative return, and plot the
# ongoing drawdown with the drawdown represented as a red area. Then, print the maximum drawdown, as well the other measures of return and risk we studied so far: annualized return, 
# annualized volatility, skewness and kurtosis.

# Requirements:
# • Python
# • Libraries: pandas, numpy, yfinance, matplotlib

# Steps:
# 1. Install Required Libraries: Ensure the necessary libraries are installed.
# Use pip to install them if needed:
# pip install pandas numpy yfinance matplotlib

# Import libraries
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib . pyplot as plt

# Download S&P 500 and US 10 - year Treasury futures data
sp500_futures = yf . download ('ES=F') ['Adj Close']
treasury_futures = yf . download ('ZN=F')['Adj Close']

# Align the datasets
data = pd . DataFrame ({'SP500': sp500_futures ,'Treasury': treasury_futures}) . dropna ()

# Calculate daily logarithmic returns
data ['SP500_Returns'] = np . log ( data ['SP500'] / data ['SP500']. shift (1) )
data ['Treasury_Returns'] = np . log ( data ['Treasury'] / data ['Treasury']. shift (1) )

# Calculate portfolio returns (60% SP500 , 40% Treasury )
data ['Portfolio_Returns'] = 0.6 * data ['SP500_Returns'] + 0.4 * data ['Treasury_Returns']

# Calculate cumulative returns for SP500 , Treasury , and Portfolio
data ['Cumulative_SP500_Returns'] = data ['SP500_Returns'].cumsum ()
data ['Cumulative_Treasury_Returns'] = data ['Treasury_Returns']. cumsum ()
data ['Cumulative_Returns'] = data ['Portfolio_Returns'].cumsum ()

# Calculate ongoing drawdown
rolling_max = data ['Cumulative_Returns']. cummax ()
data ['Drawdown'] = rolling_max - data ['Cumulative_Returns']

# Plotting the results
fig , ax = plt . subplots ()
ax . fill_between ( data . index , - data ['Drawdown'], color ='red', alpha =0.3)
ax . plot ( data ['Cumulative_Returns'] , label ='Portfolio Cumulative Returns')
ax . plot ( data ['Cumulative_SP500_Returns'], label ='S&P 500 Cumulative Returns', linestyle ='--', linewidth =0.5)
ax . plot ( data ['Cumulative_Treasury_Returns'] , label ='10 - Year Treasury Cumulative Returns', linestyle ='--', linewidth =0.5)
ax . set_title ('Portfolio Cumulative Returns and Ongoing Drawdown')
ax . set_xlabel ('Date')
ax . set_ylabel ('Returns / Drawdown')
ax . legend ()
plt . show ()

# 2. Compute and Print Measures of Return and Risk: Print the annualized return, the annualized volatility, the skewness, the kurtosis and the maximum drawdown.
# Annualized Return
total_return = np.exp(sum(data['Portfolio_Returns'].dropna()))
n_years = len(data) / 252  # Assuming 252 trading days in a year
annualized_return = (total_return ** (1 / n_years) - 1)
print("Annualized Return:", np.round(annualized_return *100 ,2),"%")

# Annualized Volatility
annualized_volatility = data['Portfolio_Returns'].std() * np.sqrt(252)
print("Annualized Volatility:", annualized_volatility)

# Skewness
skewness = data['Portfolio_Returns'].skew()
print("Skewness:", skewness)

# Kurtosis
kurtosis = data['Portfolio_Returns'].kurtosis()
print("Kurtosis:", kurtosis)

# Maximum Drawdown
max_drawdown = data['Drawdown'].max()
print("Maximum Drawdown:", max_drawdown)

print("personal note : this does not seem to include the dividends/coupons reinvestment")


# Note: This exercise guides you through the process of constructing a mixed
# asset portfolio, calculating its returns, and visualizing the risk through drawdown analysis. The plot will display the cumulative returns of the portfolio
# and highlight the drawdown periods in red, offering insights into the risk-return profile of the portfolio.


# In[ ]:





# In[ ]:




