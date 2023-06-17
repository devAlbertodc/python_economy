"""
Created on Wed Jun  7 15:52:23 2023
@author: Alberto
"""

import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ["AMZN","MSFT","META","GOOGL"]
#Range dates begin-end:
start = dt.datetime.today()-dt.timedelta(3900)
end = dt.datetime.today()
#Inicialize variables to fill values inside the loop
close_price = pd.DataFrame()
ohlcv_data = {}

#Loop over tickers and create a dataframe with adjusted close prices
for ticker in stocks:
    close_price[ticker] = yf.download(ticker,start,end)['Adj Close']

#Dropping NaN values to remove missing values
#Axis 0 drop rows that contain missing values.
#Axis 1 drop columns that contain missing values.
close_price.dropna(axis=0, how='any')

#♥Functions to apply to the dataframe prices:
close_price.mean()
close_price.std()
close_price.median()
close_price.describe()
close_price.head(10)
close_price.tail(10)

#Calculate the return respective previous value. Both lines do the same calculation
daily_return = close_price.pct_change()
#daily_return = close_price/close_price.shift(1) -1

#Average of daily return per stock:
daily_return.mean()
#Average of daily return per all stocks:
daily_return.mean(axis=1)
#Standard deviation for daily return:
daily_return.std()


#Simple Moving Average (SMA) Range to the number of periods (10 days into 1 entry)
#The weight of the values is the same. Add the 10 last values and divide it by 10.
daily_return.rolling(window=10, min_periods=6).mean()
daily_return.rolling(window=10).std()
daily_return.rolling(window=10).max()
daily_return.rolling(window=10).min()

#Exponential moving average (EMA) Exponential weighting operation
#More recent values have more weight over the last values.
df2= daily_return.ewm(com=10, min_periods=10).mean()
