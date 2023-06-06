"""
Created on Tue Jun  6 16:24:42 2023
@author: devAlberto
"""

import requests
from bs4 import BeautifulSoup

income_statement = {}

url = "https://finance.yahoo.com/quote/AAPL/financials?p=AAPL"

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
    #Iterate through tables:
    rows = t.find_all("div", {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})
        
    for row in rows:
        income_statement[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1]

print(income_statement)