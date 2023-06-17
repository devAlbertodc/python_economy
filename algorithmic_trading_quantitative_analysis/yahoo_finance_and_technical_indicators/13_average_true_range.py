"""
Created on Wed Jun 14 21:16:00 2023

@author: User
"""

import yfinance as yf

tickers = ["AMZN","MSFT","META","GOOGL"]
ohlcv_data = {}

#Loop over tickers and create a dataframe with adjusted close prices
for ticker in tickers:
    temp = yf.download(ticker,period='1mo',interval='5m')
    temp.dropna(how='any',inplace=True)
    ohlcv_data[ticker] = temp

def ATR(DF,n=14):
    df = DF.copy()
    #Add column to get difference between high and low
    df["H-L"] = df["High"] - df["Low"]
    #Add column to get difference between high and previous close:
    #Shift to get the previous value of that column
    df["H-PC"] = df["High"] - df["Adj Close"].shift(1)
    #Add column to get difference between low and previous close:
    df["L-PC"] = df["Low"] - df["Adj Close"].shift(1)
    #True range of the stock:
    #Axis=1 return max value of those three columns for each row:
    df['TR'] = df[["H-L","H-PC","L-PC"]].max(axis=1, skipna=False)
    #Average true range (ATR)
    df['ATR'] = df["TR"].ewm(com=n, min_periods=n).mean()
    return df['ATR']
    
for ticker in ohlcv_data:
    ohlcv_data[ticker]["ATR"] = ATR(ohlcv_data[ticker])
    