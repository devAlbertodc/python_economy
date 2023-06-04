import datetime as dt
import pandas as pd
import yfinance as yf

#Inicialize values
stocks = ["AMZN","MSFT","INTC"]
start = dt.datetime.today() - dt.timedelta(30)
end = dt.datetime.today()
cl_price = pd.DataFrame()
ohclv_data = {}

#Iterate loops to get only the adjusted close for every ticker:
for ticker in stocks:
    cl_price[ticker] = yf.download(ticker,start,end)['Adj Close']

print(cl_price)