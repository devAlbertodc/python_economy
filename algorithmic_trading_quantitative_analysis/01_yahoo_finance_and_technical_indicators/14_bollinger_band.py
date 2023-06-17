"""
Created on Wed Jun 14 22:03:25 2023

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
    
def Boll_Band(DF, n=14):
    df = DF.copy()
    #Middle band. Simple moving average over N rolling window:
    df["MB"] = df["Adj Close"].rolling(n).mean()
    #Upper band:
    df["UB"] = df["MB"] + 2*df["Adj Close"].rolling(n).std(ddof=0)
    #Lower band
    df["LB"] = df["MB"] - 2*df["Adj Close"].rolling(n).std(ddof=0)
    #Bollinger band width
    df["BB_Width"] = df["UB"] - df["LB"]  
    return df[["MB","UB","LB","BB_Width"]]

for ticker in ohlcv_data:
    ohlcv_data[ticker][["MB","UB","LB","BB_Width"]] = Boll_Band(ohlcv_data[ticker],20)