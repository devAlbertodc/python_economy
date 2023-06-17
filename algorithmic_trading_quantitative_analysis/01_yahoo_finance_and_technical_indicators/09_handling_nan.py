"""
Created on Wed Jun  7 15:09:12 2023
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
ohlcv_data = {}

#Loop over tickers and create a dataframe with adjusted close prices
for ticker in stocks:
    close_price[ticker] = yf.download(ticker,start,end)['Adj Close']

#Filling NaN values, axis 0 means to fill getting the previous before to the Nan from the same row
#Axis 1 is to fill NaN getting the last value of the row.
#Inplace true to show the changes to the original dataframe.
close_price.fillna(method='bfill', axis=0, inplace=True)

#Dropping NaN values to remove missing values
#Axis 0 drop rows that contain missing values.
#Axis 1 drop columns that contain missing values.
close_price.dropna(axis=0, how='any')
