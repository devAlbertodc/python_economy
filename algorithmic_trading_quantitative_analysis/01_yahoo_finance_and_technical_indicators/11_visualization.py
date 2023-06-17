"""
Created on Wed Jun  7 21:24:47 2023
@author: Alberto
"""

import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ["AMZN","MSFT","META","GOOGL"]
#Range dates begin-end:
start = dt.datetime.today()-dt.timedelta(4200)
end = dt.datetime.today()
#Inicialize variables to fill values inside the loop
close_price = pd.DataFrame()

#Loop over tickers and create a dataframe with adjusted close prices
for ticker in stocks:
    close_price[ticker] = yf.download(ticker,start,end)['Adj Close']

#Dropping NaN values to remove missing values
#Axis 0 drop rows that contain missing values.
#Axis 1 drop columns that contain missing values.
close_price.dropna(axis=0, how='any')

#Calculate the return respective previous value. Both lines do the same calculation
daily_return = close_price.pct_change()
#daily_return = close_price/close_price.shift(1) -1

#Way to generate graphs:
close_price.plot(kind="line", subplots=True, layout=(2,2), title="Stock price evolution", grid=True)
daily_return.plot(kind="line", subplots=True, layout=(2,2), title="Stock price evolution", grid=True)

#Acumulated return (compounding) in a plot to show which evolution had every stock
(1+daily_return).cumprod().plot()