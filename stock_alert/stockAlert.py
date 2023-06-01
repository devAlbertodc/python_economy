import os
import time
import pandas_datareader as web
import datetime as dt
from winotify import Notification

tickers =      ['ACS.MC', 'ACX.MC', 'ELE.MC', 'FDR.MC', 'GRF.MC', 'IDR.MC', 'ITX.MC', 'SLR.MC']
upper_limits = [22.30, 9, 17.50, 16, 11.70, 7.90, 21.75, 19.50]
lower_limits = [22, 8.50, 17, 15, 11.25, 7.50, 21.25, 19]

while True:
    last_prices = [web.DataReader(ticker, "yahoo")['Adj Close'][-1] for ticker in tickers]
    #print(f"{dt.datetime.now()} ====== {last_prices:.2f}")

    #Crear diccionario con precios y valores:
    data = {}
    data['simbolo'] = [ticker for ticker in tickers];
    data['precio'] = [precio for precio in last_prices]

    time.sleep(60)
    for i in range(len(tickers)):
        if last_prices[i] > upper_limits[i]:
            toast = Notification(app_id="",
                                 title="Alerta" + tickers[i],
                                 msg=f"{tickers[i]} se valora en {last_prices[i]:.2f}",
                                 icon=os.path.join(os.getcwd(), "stop.png"),
                                 duration="long")
            toast.show()
        elif last_prices[i] < lower_limits[i]:
            toast = Notification(app_id="",
                                title="Alerta " + tickers[i],
                                msg=f"{tickers[i]} se valora en {last_prices[i]:.2f}",
                                icon=os.path.join(os.getcwd(), "profit.png"),
                                duration="long")
            toast.show()
        print(f"{dt.datetime.now()} - {data['simbolo'][i]} - {data['precio'][i]:.2f}")
    print("============================================")
    time.sleep(1)