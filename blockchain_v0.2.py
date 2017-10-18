import datetime
import time
import csv
import json
import urllib.request

global tag_neu
tag_neu = True
global counter
counter = 1
global mod_time_day_last
mod_time_day_last = -1

class main():
    def __init__(self, *args, **kwargs):
        main.prog(self)

    def prog(self):

        global tag_neu
        global counter
        global mod_time_day_last

        # HISTORICAL DATA HISTORICAL DATA HISTORICAL DATA HISTORICAL DATA HISTORICAL DATA HISTORICAL DATA HISTORICAL DATA HISTORICAL DATA
        date_list = []
        price_list = []
        
        # Datei holen
        if tag_neu == True:
            urllib.request.urlretrieve('https://blockchain.info/charts/market-price?timespan=60days&format=csv', 'history.csv')
            
        with open('history.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:

                date_str = str(row[0])
                #print(datetime.datetime.utcfromtimestamp(date_int))
                date_list.append(date_str)

                price_float = float(row[1])
                price_int = round(price_float,2)
                price_list.append(price_int)

        # TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER TICKER
        with urllib.request.urlopen('https://blockchain.info/ticker') as url:
            ticker = json.loads(url.read().decode())

        price_15m = ticker['EUR']['15m']
        price_last = ticker['EUR']['last']
        price_buy = ticker['EUR']['buy']
        price_sell = ticker['EUR']['sell']

        date_akt = datetime.datetime.now().isoformat()

        price_list.append(price_last)
        date_list.append(date_akt)

        # ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM ALGORYTHM
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

        # CSV file mit Kenner wegschreiben
        if tag_neu == False:
            # erste komplett neu einlesen und dannach neu schreiben
            with open('/Users/Micha/Documents/bitbot/bit.bot/history_kenner.csv') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                write_array = []
                for row in readCSV:
                    write_array.append(row)
            with open('/Users/Micha/Documents/bitbot/bit.bot/history_kenner.csv', 'w') as writeCSV:
                writer = csv.writer(writeCSV, dialect='excel')
                for row in write_array:
                    writer.writerow(row)
                write_array = date_list[60], price_list[60], ema1_array[60], ema_ema1_array[60], dema1_array[60], ema2_array[60], ema_ema2_array[60], dema2_array[60], dema_diff_array[60], result_array[60]
                writer.writerow(write_array)

        if tag_neu == True:
            with open('/Users/Micha/Documents/bitbot/bit.bot/history_kenner.csv', 'w') as writeCSV:
                writer = csv.writer(writeCSV, dialect='excel')
                for row in zip(date_list, price_list, ema1_array, ema_ema1_array, dema1_array, ema2_array, ema_ema2_array, dema2_array, dema_diff_array, result_array):
                    writer.writerow(row)
                tag_neu = False

        # TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE TRADE
        # todo
        if result_array[59] == 0 and result == 1:
            print("BUY BUY BUY BUY BUY BUY BUY BUY BUY BUY BUY BUY BUY BUY BUY BUY BUY BUY ")
        if result_array[59] == 1 and result == 0:
            print("SELL SELL SELL SELL SELL SELL SELL SELL SELL SELL SELL SELL SELL SELL SELL ")
        price_diff = round(price_last - price_list[59], 2)
        print(counter, " Diff:", price_diff, " -  Price_yesterday:", price_list[59], "Price:", price_last, " -  Result_yesterday:", result_array[59], "Result:", result)

        # Bei neuem Tag:
        time_day = time.time()
        # ACHTUNG => UTC = GMT - 2
        #mod_time_day = time_day % (60*60*24)
        mod_time_day = time_day % (60) # aktuell jede Minute
        if mod_time_day<mod_time_day_last:
            tag_neu = True
        mod_time_day_last = mod_time_day

        counter += 1
        time.sleep(1.0)
        main.prog(self)

if __name__ == "__main__":
    main()
