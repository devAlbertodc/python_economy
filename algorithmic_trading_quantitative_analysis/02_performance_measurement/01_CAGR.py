"""
Created on Sat Jun 17 23:27:46 2023
@author: User
"""

#CAGR (Cumulative Anual Growth Rate)
# Import necesary libraries
import yfinance as yf
import numpy as np

# Download historical data for required stocks
tickers = ["AMZN","MSFT","META","GOOGL","OXY"]
ohlcv_data = {}

# looping over tickers and storing OHLCV dataframe in dictionary
for ticker in tickers:
    temp = yf.download(ticker,period='1y',interval='1d')
    temp.dropna(how="any",inplace=True)
    ohlcv_data[ticker] = temp
    
def CAGR(DF):
    df = DF.copy()
    df = df.copy()
    #Get percentage change of close for every period:
    df['return'] = df['Adj Close'].pct_change()
    df['cumulative_return'] = (1+df['return']).cumprod()
    #Number of rows of dataframe divided by trading days in a year
    n = len(df) / 252

    #Last value
    CAGR = (df['cumulative_return'][-1])**(1/n) -1
    return CAGR

for ticker in ohlcv_data:
    print("CAGR for {} = {}".format(ticker,CAGR(ohlcv_data[ticker])))