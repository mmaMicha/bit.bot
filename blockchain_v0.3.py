
import datetime
import csv
import json
import urllib.request

def main():
    ticker()

# HISTORICAL DATA - HISTORICAL DATA - HISTORICAL DATA - HISTORICAL DATA - HISTORICAL DATA - HISTORICAL DATA - HISTORICAL DATA
def history(self):
    date_list = []
    price_list= []

    # Datei holen
    #urllib.request.urlretrieve('https://blockchain.info/charts/market-price?timespan=60days&format=csv', 'history.csv')
    with open('history.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:

            date_str = str(row[0])
            #print(datetime.datetime.utcfromtimestamp(date_int))
            date_list.append(date_str)

            price_float = float(row[1])
            self.price_int = round(price_float,2)
            price_list.append(price_int)

            algorythm()

            # write CSV file
            with open('/Users/Micha/Documents/bitbot/bit.bot/history_kenner.csv', 'w') as writeCSV:
                writer = csv.writer(writeCSV, dialect='excel')
                for row in zip(date_list, price_list, ema1_array, ema_ema1_array, dema1_array, ema2_array, ema_ema2_array, dema2_array, dema_diff_array, result_array):
                    writer.writerow(row)

# ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM
def algorythm(price):

    price_list = [price, history.price_int]

    weight1 = 0.18
    weight2 = 0.09

    ema1_array = []
    ema_ema1_array = []
    dema1_array = []

    ema2_array = []
    ema_ema2_array = []
    dema2_array = []
    
    dema_diff_array = []
    result_array = []

    for x in range(len(price_list)):

        if x==0:
            ema1_n1 = price_list[x]
            ema2_n1 = price_list[x]
            ema_ema1_n1 = price_list[x]
            ema_ema2_n1 = price_list[x]

        ema1 = (price_list[x] - ema1_n1)*weight1+ema1_n1
        ema1_array.append(ema1)

        ema2 = (price_list[x] - ema2_n1)*weight2+ema2_n1
        ema2_array.append(ema2)

        ema_ema1 = (ema1_array[x] - ema_ema1_n1)*weight1+ema_ema1_n1
        ema_ema1_array.append(ema_ema1)

        dema1 = (2*ema1)-ema_ema1
        dema1_array.append(dema1)

        ema_ema2 = (ema2_array[x] - ema_ema2_n1)*weight2+ema_ema2_n1
        ema_ema2_array.append(ema_ema2)

        dema2 = (2*ema2)-ema_ema2
        dema2_array.append(dema2)

        dema_diff = dema1 - dema2
        dema_diff_array.append(dema_diff)

        if dema_diff<=0: result = 0
        if dema_diff>0: result = 1
        result_array.append(result)

        ema1_n1 = ema1
        ema2_n1 = ema2
        ema_ema1_n1 = ema_ema1
        ema_ema2_n1 = ema_ema2

# TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER
def ticker():
    with urllib.request.urlopen('https://blockchain.info/ticker') as url:
        ticker = json.loads(url.read().decode())

    price_15m = ticker['EUR']['15m']
    price_last = ticker['EUR']['last']
    price_buy = ticker['EUR']['buy']
    price_sell = ticker['EUR']['sell']

    algorythm(price_15m)

    time.sleep(1.0)

if __name__ == "__main__":
    main()
