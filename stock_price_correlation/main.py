#https://www.youtube.com/watch?v=Jfo22-qB4UI
#pip install matplotlib seaborn pandas pandas-datareader

import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

#Rango de fechas:
start = dt.datetime(2018,1,1)
end = dt.datetime.now()

#Empresas a comparar:
tickers = ["FB", "NVDA", "MSFT", "AAPL"]
#tickers = ['BMW.DE', 'VOW3.DE', 'PAH3.DE']
colnames = []

for ticker in tickers:
    #Obtengo datos de un ticker:
    data = web.DataReader(ticker, 'yahoo', start, end)
    #Si esta vacio - es la primera vez que se entra:
    if (len(colnames)) == 0:
        combined = data[['Adj Close']].copy()
    else:
        combined = combined.join(data['Adj Close'])
    colnames.append(ticker)
    combined.columns = colnames

#Mostrar en decimal o logaritmica:
plt.yscale("log")
for ticker in tickers:
    # Dibujar el grafico de cada ticker con su etiqueta:
    plt.plot(combined[ticker], label=ticker)

plt.legend(loc="upper right")
plt.show()

#Correlacion de empresas, cuanto se parecen entre si?
corr_data = combined.pct_change().corr(method="pearson")
sns.heatmap(corr_data, annot=True, cmap="coolwarm")
plt.show()