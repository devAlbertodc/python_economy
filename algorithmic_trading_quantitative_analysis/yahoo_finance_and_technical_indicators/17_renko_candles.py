"""
Created on Sat Jun 17 17:09:18 2023
@author: Alberto
"""

# Import necesary libraries
import yfinance as yf
import numpy as np
from stocktrends import Renko

# Download historical data for required stocks
tickers = ["AMZN","MSFT","META","GOOGL"]
ohlcv_data = {}
hour_data = {}
renko_data = {}

# looping over tickers and storing OHLCV dataframe in dictionary
for ticker in tickers:
    temp = yf.download(ticker,period='1mo',interval='5m')
    temp.dropna(how="any",inplace=True)
    ohlcv_data[ticker] = temp
    
    temp = yf.download(ticker,period='1y',interval='1h')
    temp.dropna(how="any",inplace=True)
    hour_data[ticker] = temp
    
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

def renko_DF(DF, hourly_df):
    df = DF.copy()
    #Drop column Close and modify the column names for Renko library compatibility
    df.drop("Close",axis=1, inplace=True)
    df.reset_index(inplace=True)
    df.columns = ["date","open","high","low","close","volume"]
    
    df2 = Renko(df)
    df2.brick_size = 3*round(ATR(hourly_df,120).iloc[-1],0)
    renko_df =  df2.get_ohlc_data()
    return renko_df

for ticker in ohlcv_data:
    renko_data[ticker] = renko_DF(ohlcv_data[ticker], hour_data[ticker])
    