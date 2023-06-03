import datetime as dt
import pandas as pd
import yfinance as yf

#
stocks = ["AMZN","MSFT","INTC"]
start = dt.datetime.today() - dt.timedelta(30)
end = dt.datetime.today()
cl_price = pd.DataFrame()
ohclv_data = {}

for ticker in stocks:
    cl_price[ticker] = yf.download(ticker,start,end)['Adj Close']

print(cl_price)