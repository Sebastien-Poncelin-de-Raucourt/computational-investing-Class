#!/usr/bin/env python
# coding: utf-8

# In[9]:


# 2.10 Python Exercise: Comparing S&P 500 Futures Logarithmic Returns with a Normal Distribution

# Objective: Analyze the distribution of S&P 500 front-month futures logarithmic returns and compare it with a normal distribution curve. The exercise will
# involve downloading data, calculating returns, and creating a histogram with a normal distribution overlay.
    
# Requirements:
# • Python
# • Libraries: numpy, yfinance, matplotlib, scipy

# Instructions:
# 1. Import Necessary Libraries: Begin by importing the required libraries: numpy (as np), yfinance (as yf), matplotlib.pyplot (as plt), and norm from scipy.stats.
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm

# 2. Download S&P 500 Futures Data: Use yfinance’s ‘download‘ function to retrieve the ’Adj Close’ prices of S&P 500 front-month futures (’ES=F’).
sp500_data = yf.download('ES=F')

# 3. Calculate Daily Logarithmic Returns: Compute the daily logarithmic returns of the S&P 500 futures. Use numpy’s ‘log‘ function and the
# ‘shift‘ method on the ’Adj Close’ prices. Remember to drop any NaN values that result from the calculation.
log_returns = np.log(sp500_data['Adj Close'] / sp500_data['Adj Close'].shift(1)).dropna()

# 4. Calculate Mean and Standard Deviation of Returns: Determine the mean and standard deviation of the logarithmic returns. Store these
# values in variables named ‘mean‘ and ‘std‘.
# Calculate mean and standard deviation of returns
mean , std = log_returns . mean () , log_returns . std ()

# 5. Generate Range of Values for Normal Distribution: Create a range
# of values (linspace) between the minimum and maximum of the logarithmic returns. Use numpy’s ‘linspace‘ function and multiply the difference
# between max and min returns by 10000 to determine the number of bins (‘n bins‘).
# Generate a range of values for the normal distribution
n_bins = int ( max ( log_returns ) - min ( log_returns ) * 10000)
norm_dist = np . linspace ( min ( log_returns ) , max ( log_returns ), n_bins )

# 6. Calculate Normal Distribution Curve: Compute the normal distribution curve with the same mean and standard deviation as the logarithmic returns. Use the ‘pdf‘ function from 
# the ‘norm‘ module of scipy.stats.
# Calculate the normal distribution with the same mean and standard deviation
normal_curve = norm . pdf ( norm_dist , mean , std )

# 7. Plot Histogram and Normal Distribution: Create a histogram of the logarithmic returns and overlay the normal distribution curve on it.
# Use matplotlib’s ‘plt.hist‘ for the histogram and ‘plt.plot‘ for the normal distribution curve. Ensure the histogram uses the same number of bins as
# calculated earlier and is colored orange. Label the histogram as ’Actual Distribution’ and the curve as ’Normal Distribution’.
plt.hist(log_returns, bins=n_bins, color='orange', alpha=0.7, label='Actual Distribution')
plt.plot(norm_dist, normal_curve, 'k--', label='Normal Distribution')

# 8. Add Vertical Lines for Mean and Standard Deviations: Draw vertical dashed lines at the mean and at one, two, and three standard
# deviations away from the mean on both sides. Color the lines differently for positive (green) and negative (red) standard deviations and label them accordingly.
plt.axvline(mean, color='black', linestyle='-', linewidth=2, label='Mean')
plt.axvline(mean + std, color='green', linestyle='--', linewidth=1, label='+1 Std Dev')
plt.axvline(mean - std, color='green', linestyle='--', linewidth=1)
plt.axvline(mean + 2 * std, color='blue', linestyle='--', linewidth=1, label='+2 Std Dev')
plt.axvline(mean - 2 * std, color='blue', linestyle='--', linewidth=1)
plt.axvline(mean + 3 * std, color='red', linestyle='--', linewidth=1, label='+3 Std Dev')
plt.axvline(mean - 3 * std, color='red', linestyle='--', linewidth=1)

# 9. Finalize the Plot: Add a title, labels for the x-axis (’Logarithmic Returns’) and y-axis (’Frequency/Density’), and a legend to the plot. Then, display the plot using ‘plt.show()‘.
plt.title('S&P 500 Futures Logarithmic Returns Distribution')
plt.xlabel('Logarithmic Returns')
plt.ylabel('Frequency/Density')
plt.legend()
plt.show()

# 10. Compute and Print Measures of Return and Risk: Print the annualized return, the annulaized volatility, the skewness and the kurtosis.
annualized_return = np.exp(mean * 252) - 1  # 252 trading days in a year
annualized_volatility = std * np.sqrt(252)
skewness = log_returns.skew()
kurtosis = log_returns.kurtosis()

print("Annualized Return:", annualized_return)
print("Annualized Volatility:", annualized_volatility)
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)

# This exercise will help you visualize how closely the logarithmic returns of S&P 500 futures follow a normal distribution, providing insights into the nature
# of return distributions in financial markets.


# In[ ]:





# In[ ]:




