"""
Created on Wed Jun  7 11:24:49 2023
@author: Alberto
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

#List of tickers and dictionary to save info:
tickers = ['AAPL','META','CSCO']
key_stadistics = {}

#Iterate all the tickers dinamically
for ticker in tickers:
    url = "https://finance.yahoo.com/quote/{}/key-statistics?p={}".format(ticker,ticker)
    #Avoid yahoo detect we are using a bot.
    headers = {"User-Agent": "Chrome/114.0.5735.110"}
    #Make a request to the page and get the html code:
    page = requests.get(url, headers=headers)
    page_content = page.content
    #Generate a BeautifulSoup object sending html code and the parser:
    soup = BeautifulSoup(page_content,"html.parser")
    #Find the div with breakdown of income statements table
    table = soup.find_all("table", {"class": "W(100%) Bdcl(c)"})
    
    #Reset temporal dictionary:
    temp_stats = {}
    for t in table:    
        #Iterate through every row
        rows = t.find_all("tr")
        
        #Get attribute and its value inside every row.
        #The[-1] is to get the last value of a row, sometimes there is a <sup> element.
        for row in rows:
            temp_stats[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[-1]
            
        key_stadistics[ticker] = temp_stats