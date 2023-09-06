"""
Created on Wed Sep 6 12:52:40 2023
@author: devAlbertodc
"""

#Volatility of a strategy is represented by the standard deviation of the returns.
#This captures the variability of returns from the mean return.
import yfinance as yf
import numpy as np

# Download data for required stocks
tickers = ["AMZN","MSFT","META","GOOGL","OXY"]
ohlcv_data = {}

# looping over tickers and storing OHLCV dataframe in dictionary
for ticker in tickers:
    temp = yf.download(ticker,period='1y',interval='1d')
    temp.dropna(how="any",inplace=True)
    ohlcv_data[ticker] = temp

def volatility(DF):
    df = DF.copy()
    df['return'] = df['Adj Close'].pct_change()

    #Anual return using numpy square function for 252 trading days per year.
    vol = df['return'].std() * np.sqrt(252)

    return vol

for ticker in ohlcv_data:
    print("Volatility of {} = {}".format(ticker,volatility(ohlcv_data[ticker])))