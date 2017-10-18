
import csv
import numpy as np
import datetime
import json

def main():

    # HISTORICAL DATA HISTORICAL DATA HISTORICAL DATA HISTORICAL DATA HISTORICAL DATA HISTORICAL DATA

    date_array = []
    amount_array = []
    price_array = []
    value_array = []

    # CSV file lesen
    with open('krakenEUR_short.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:

            date_int = float(row[0])
            #print(datetime.datetime.utcfromtimestamp(date_int))
            date_array.append(date_int)

            amount_float = float(row[1])
            amount_array.append(amount_float)

            price_float = float(row[2])
            price_array.append(price_float)

            # 09.01.14 -> 1389225600
            # ein Tag -> 86400
            # 16.10.17 -> 1508104800

            # Mittelwert pro Tag
            y = 1389225600
            for x in range(1389225600, 1508104800):
                # neuer Tag
                if y == y+86400:
                    tag+=tag
                    y=x

    # Algorythmus Algorythmus Algorythmus Algorythmus Algorythmus Algorythmus Algorythmus Algorythmus Algorythmus
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

    for x in range(0,10):

        if x==0:
            ema1_n1 = price_array[x]
            ema2_n1 = price_array[x]

        ema1 = (price_array[x] - ema1_n1)*weight1+ema1_n1
        ema1_array.append(ema1)

        ema2 = (price_array[x] - ema2_n1)*weight2+ema2_n1
        ema2_array.append(ema2)

        ema_ema1 = (ema1_array[x] - ema1_n1)*weight1+ema1_n1
        ema_ema1_array.append(ema_ema1)

        dema1 = (2*ema1)-ema_ema1
        dema1_array.append(ema1)

        ema_ema2 = (ema2_array[x] - ema2_n1)*weight2+ema2_n1
        ema_ema2_array.append(ema_ema2)

        dema2 = (2*ema2)-ema_ema2
        dema2_array.append(dema2)

        dema_diff = dema1 - dema2
        dema_diff_array.append(dema2)

        if dema_diff<=0: result = 0
        if dema_diff>0: result = 1
        result_array.append(result)

        ema1_n1 = ema1
        ema2_n1 = ema2

    # write CSV file
    with open('/Users/Micha/Documents/bitbot/bit.bot/krakenEUR_neu.csv') as readCSV:
        outfile = open('/Users/Micha/Documents/bitbot/bit.bot/krakenEUR_neu.csv', 'w')
        writer = csv.writer(outfile, dialect='excel')

        for row in zip(date_array, amount_array, price_array, ema1_array, ema_ema1_array, dema1_array, ema1_array, ema_ema1_array, dema1_array, dema_diff_array, result_array):
            writer.writerow(row)

    """
    # TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER
    full_url = 'https://blockchain.info/ticker'
    urllib.request.urlretrieve(full_url, "ticker.csv")

    time.sleep(0.5)
    """

if __name__ == "__main__":
    main()
