# ============================================================================
# Getting financial data from yahoo finance using webscraping - Intro
# Author - Mayank Rasu

# Please report bugs/issues in the Q&A section
# =============================================================================

import requests
from bs4 import BeautifulSoup

#Scraping income statement for a static ticker
income_statement = {}
url = "https://finance.yahoo.com/quote/AAPL/financials?p=AAPL"
#Avoid yahoo detect we are using a bot.
headers = {"User-Agent" : "Chrome/96.0.4664.110"}
#Send request and get html content back:
page = requests.get(url, headers=headers)
page_content = page.content
soup = BeautifulSoup(page_content,"html.parser")
#Get income statement table using find_all function:
tabl = soup.find_all("div" , {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
for t in tabl:
    rows = t.find_all("div" , {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})
    #Get all the rows attribute and its value:
    for row in rows:
        income_statement[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1]
