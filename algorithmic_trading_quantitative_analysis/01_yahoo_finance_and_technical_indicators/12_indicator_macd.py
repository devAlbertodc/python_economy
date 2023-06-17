"""
Created on Tue Jun 13 21:18:13 2023
@author: User
"""

import yfinance as yf

tickers = ["AMZN","MSFT","META","GOOGL"]
ohlcv_data = {}

#Loop over tickers and create a dataframe with adjusted close prices
for ticker in tickers:
    temp = yf.download(ticker,period='1mo',interval='15m')
    temp.dropna(how='any',inplace=True)
    ohlcv_data[ticker] = temp

#Dataframe with all data and number of periods to operate between averages
def MACD(DF,a=12,b=26,c=9):
    df = DF.copy()
    df["ma_fast"] = df["Adj Close"].ewm(span=a, min_periods=a).mean()
    df["ma_slow"] = df["Adj Close"].ewm(span=b, min_periods=b).mean()
    df["macd"] = df["ma_fast"] - df["ma_slow"]
    df["signal"] = df["macd"].ewm(span=c, min_periods=c).mean()
    return df.loc[:,["macd","signal"]]

for ticker in ohlcv_data:
    ohlcv_data[ticker][["MACD","SIGNAL"]] = MACD(ohlcv_data[ticker])