"""
Created on Thu Jun  8 07:54:51 2023
@author: Alberto
"""

import datetime as dt
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ["AMZN","MSFT","META","GOOGL"]
#Range dates begin-end:
start = dt.datetime.today()-dt.timedelta(4200)
end = dt.datetime.today()
#Inicialize variables to fill values inside the loop
close_price = pd.DataFrame()

#Loop over tickers and create a dataframe with adjusted close prices
for ticker in tickers:
    close_price[ticker] = yf.download(ticker,start,end)['Adj Close']

#Dropping NaN values to remove missing values
#Axis 0 drop rows that contain missing values.
#Axis 1 drop columns that contain missing values.
close_price.dropna(axis=0, how='any', inplace=True)

#Calculate the return respective previous value. Both lines do the same calculation
daily_return = close_price.pct_change()
#daily_return = close_price/close_price.shift(1) -1

#Matplotlib has more custom parameters to allow you to improve your graphs:
fig, ax = plt.subplots()
plt.style.available
plt.style.use("seaborn-darkgrid")
ax.set(title="Mean Daily Return", xlabel="Stocks", ylabel="Mean Return")
plt.bar(x=daily_return.columns, height=daily_return.mean())
plt.bar(x=daily_return.columns, height=daily_return.std())
