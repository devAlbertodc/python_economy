import pandas as pd
from yahoofinancials import YahooFinancials
import datetime as dt

#List of tickers (array)
all_tickers = ["AAPL","MSFT","CSCO","AMZN","INTC"]

# extracting stock data (historical close price) for the stocks identified
close_prices = pd.DataFrame()
# Dynamic range filters:
end_date = (dt.date.today()).strftime('%Y-%m-%d')
beg_date = (dt.date.today()-dt.timedelta(1825)).strftime('%Y-%m-%d')

for ticker in all_tickers:
    yahoo_financials = YahooFinancials(ticker)
    json_obj = yahoo_financials.get_historical_price_data(beg_date,end_date,"daily")
    #Generate dictionary with prices where every price is a dictionary with open,close,high,low...
    ohlv = json_obj[ticker]['prices']
    #Change dictionary to pandas dataframe for only a date yyyy-mm-dd and adjusted close for now:
    temp = pd.DataFrame(ohlv)[["formatted_date","adjclose"]]
    #The index will be a date instead of numeric index:
    temp.set_index("formatted_date",inplace=True)
    #Remove the na (not available) values
    temp.dropna(inplace=True)
    #Reasign the adjusted close to main dataframe:
    close_prices[ticker] = temp["adjclose"]

# extracting stock data (ohlcv) for the stocks identified
ohlv_dict = {}
end_date = (dt.date.today()).strftime('%Y-%m-%d')
beg_date = (dt.date.today()-dt.timedelta(1825)).strftime('%Y-%m-%d')
for ticker in all_tickers:
    yahoo_financials = YahooFinancials(ticker)
    json_obj = yahoo_financials.get_historical_price_data(beg_date,end_date,"daily")
    ohlv = json_obj[ticker]['prices']
    temp = pd.DataFrame(ohlv)[["formatted_date","adjclose","open","low","high","volume"]]
    temp.set_index("formatted_date",inplace=True)
    temp.dropna(inplace=True)
    ohlv_dict[ticker] = temp