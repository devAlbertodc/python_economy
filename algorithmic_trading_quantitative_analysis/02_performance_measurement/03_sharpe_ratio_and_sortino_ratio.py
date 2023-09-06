"""
Created on Wed Sep 6 12:52:40 2023
@author: devAlbertodc
"""

#Sharpe ratio is the average return earned in excess of the risj free rate per unit of volatility
#When is greater than 1 is good, greater than 2 very good and greater than 3 excellent.

#Sortino applies the same but using standart deviation of negative asset return.
import yfinance as yf
import pandas as pd
import numpy as np

# Download data for required stocks
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

def volatility(DF):
    df = DF.copy()
    df['return'] = df['Adj Close'].pct_change()
    #Anual return using numpy square function for 252 trading days per year.
    vol = df['return'].std() * np.sqrt(252)
    return vol

def sharpe(DF, rf):
    df = DF.copy()
    return (CAGR(df) - rf) / volatility(df)

def sortino (DF, rf):
    df = DF.copy()
    df['return'] = df['Adj Close'].pct_change()
    neg_return = np.where(df['return'] > 0,0, df['return'])
    neg_volatility = pd.Series(neg_return[neg_return != 0]).std()
    return (CAGR(df) - rf) / neg_volatility

for ticker in ohlcv_data:
    print("Sharpe for {} = {}".format(ticker,sharpe(ohlcv_data[ticker], 0.03)))
    print("Sortino for {} = {}".format(ticker,sortino(ohlcv_data[ticker], 0.03)))