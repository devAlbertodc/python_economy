"""
Created on Tue Jun  6 16:24:42 2023
@author: devAlberto
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

tickers = ['AAPL','META','CSCO']
income_statement_dict = {}
balance_sheet_dict = {}
cashflow_st_dict = {}

for ticker in tickers:
    
    #Scraping income statement:
    url = "https://finance.yahoo.com/quote/{}/financials?p={}".format(ticker,ticker)
    income_statement = {}
    table_title = {}
        
    #Avoid yahoo detect we are using a bot.
    headers = {"User-Agent": "Chrome/114.0.5735.110"}
    #Make a request to the page and get the html code:
    page = requests.get(url, headers=headers)
    page_content = page.content
    #Generate a BeautifulSoup object sending html code and the parser:
    soup = BeautifulSoup(page_content,"html.parser")
    #Find the div with breakdown of income statements table
    table = soup.find_all("div", {"class": "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    
    
    #Loop through every 
    for t in table:
        #Get first line headers of the table. The title will be the key and the rest of the columns will be values:
        heading = t.find_all("div", {"class":"D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator="|").split("|")[0]] = top_row.get_text(separator="|").split("|")[1:]
                
        #Iterate through tables:
        rows = t.find_all("div", {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})
        
        #Get the first value of the row as dictionary key and the other columns as values.
        for row in rows:
            income_statement[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1:]

        #Apply .T to change the properties on columns to rows and viceversa:
        temp = pd.DataFrame(income_statement).T
        #At this point, the headers are numbers like 0,1,2,3... Instead of dates
        temp.columns = table_title["Breakdown"]
        income_statement_dict[ticker] = temp
                
    #Scraping balance sheet statement:
    url = "https://finance.yahoo.com/quote/{}/balance-sheet?p={}".format(ticker,ticker)
    balance_sheet = {}
    table_title = {}
        
    #Avoid yahoo detect we are using a bot.
    headers = {"User-Agent": "Chrome/114.0.5735.110"}
    #Make a request to the page and get the html code:
    page = requests.get(url, headers=headers)
    page_content = page.content
    #Generate a BeautifulSoup object sending html code and the parser:
    soup = BeautifulSoup(page_content,"html.parser")
    #Find the div with breakdown of income statements table
    table = soup.find_all("div", {"class": "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    
    #Loop through every 
    for t in table:
        #Get first line headers of the table. The title will be the key and the rest of the columns will be values:
        heading = t.find_all("div", {"class":"D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator="|").split("|")[0]] = top_row.get_text(separator="|").split("|")[1:]
                
        #Iterate through tables:
        rows = t.find_all("div", {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})
        
        #Get the first value of the row as dictionary key and the other columns as values.
        for row in rows:
            balance_sheet[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1:]
    
        #Apply .T to change the properties on columns to rows and viceversa:
        temp = pd.DataFrame(balance_sheet).T
        #At this point, the headers are numbers like 0,1,2,3... Instead of dates
        temp.columns = table_title["Breakdown"]
        balance_sheet_dict[ticker] = temp
        
  
    #Scraping cashflow statement:
    url = "https://finance.yahoo.com/quote/{}/cash-flow?p={}".format(ticker,ticker)
    cashflow = {}
    table_title = {}
        
    #Avoid yahoo detect we are using a bot.
    headers = {"User-Agent": "Chrome/114.0.5735.110"}
    #Make a request to the page and get the html code:
    page = requests.get(url, headers=headers)
    page_content = page.content
    #Generate a BeautifulSoup object sending html code and the parser:
    soup = BeautifulSoup(page_content,"html.parser")
    #Find the div with breakdown of income statements table
    table = soup.find_all("div", {"class": "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    
    #Loop through every 
    for t in table:
        #Get first line headers of the table. The title will be the key and the rest of the columns will be values:
        heading = t.find_all("div", {"class":"D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator="|").split("|")[0]] = top_row.get_text(separator="|").split("|")[1:]
                
        #Iterate through tables:
        rows = t.find_all("div", {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})
        
        #Get the first value of the row as dictionary key and the other columns as values.
        for row in rows:
            cashflow[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1:]
    
        #Apply .T to change the properties on columns to rows and viceversa:
        temp = pd.DataFrame(cashflow).T
        #At this point, the headers are numbers like 0,1,2,3... Instead of dates
        temp.columns = table_title["Breakdown"]
        cashflow_st_dict[ticker] = temp

#Iterate all the columns from every ticker dataframe to change the values that are object datatype to float64 as numbers
for ticker in tickers:
    for col in income_statement_dict[ticker].columns:
        income_statement_dict[ticker][col] = income_statement_dict[ticker][col].str.replace(',|-','')
        income_statement_dict[ticker][col] = pd.to_numeric(income_statement_dict[ticker][col], errors='coerce')

    for col in balance_sheet_dict[ticker].columns:
        balance_sheet_dict[ticker][col] = balance_sheet_dict[ticker][col].str.replace(',|-','')
        balance_sheet_dict[ticker][col] = pd.to_numeric(balance_sheet_dict[ticker][col], errors='coerce')

    for col in cashflow_st_dict[ticker].columns:
        cashflow_st_dict[ticker][col] = cashflow_st_dict[ticker][col].str.replace(',|-','')
        cashflow_st_dict[ticker][col] = pd.to_numeric(cashflow_st_dict[ticker][col], errors='coerce')
