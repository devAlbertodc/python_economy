from yahoofinancials import YahooFinancials

#Get ticker info using YahooFinancials class to create an objeect and use its methods:
ticker = 'MSFT'
yahoo_financials = YahooFinancials(ticker)
data = yahoo_financials.get_historical_price_data("2018-04-24", "2020-04-24", "daily")