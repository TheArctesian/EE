import os
import logging
from numpy import true_divide
import pandas as pd

# LOGGING 
class handler(logging.StreamHandler):
    colors = {
        logging.DEBUG: '\033[37m',
        logging.INFO: '\033[36m',
        logging.WARNING: '\033[33m',
        logging.ERROR: '\033[31m',
        logging.CRITICAL: '\033[101m',
    }
    reset = '\033[0m'
    fmtr = logging.Formatter('%(levelname)s %(message)s')

    def format(self, record):
        color = self.colors[record.levelno]
        log = self.fmtr.format(record)
        reset = self.reset
        return color + log + reset


logging.basicConfig(level=logging.DEBUG, handlers=[handler()])
logger = logging.getLogger('bobcat')
logger.setLevel('DEBUG')

def weight(number):
    if number > -0.3 < -0.1:
        return 0
    if number > -0.1:
        return 1
    if number < -0.1:
        return 2

def calAvg(array):
    total = 0
    for number in array: 
        total += number
    avg = total/len(array)
    return avg

def checkTopP(topPrice, new):
    if topPrice > new: 
        return topPrice
    if new > topPrice: 
        return new

def checkHalf(topPrice, half):
    if topPrice/2 == half:
        return True
    else:
        return False
    
def hundredDayAvg(array):
    while len(array) != 100 & len(array) <= 100:
        array.pop(0)
    HDA = calAvg(array) # Hundred day avg
    return HDA

def thirtyDayAvg(array):
    while len(array) != 30 & len(array) <= 30: 
        array.pop(0)
    TDA = calAvg(array) # Thirty Day Avg
    return TDA

def sevenDayAvg(array):
    while len(array) != 7 & len(array) <= 7:
        array.pop(0)
    SDA = calAvg(array) # Seven Day avg
    return SDA


def tester():
    Tprice7 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
    T2price7 = [1,1,1,1]
    T1 = thirtyDayAvg(Tprice7)
    T2 = sevenDayAvg(T2price7)
    print(f'{Tprice7} avg is {T1}')
    print(f'{T2price7} avg is {T2}')


def buy(price, balance, btc):
    if balance == 0:
        return btc
    if balance > price: 
        btc = balance/price
    if price > balance:
        btc = price/balance
    return btc

def sell(price, balance, btc):
    if btc == 0:
        return balance
    balance = price*btc 
    return balance

if __name__ == "__main__":

    balance = 0
    btc = 1
    netBal = 11766

    topPrice = 19280
    SDPA = 0 #Seven Day Price Avg 
    TDPA = 0 #Thirty Day Price Avg
    HDPA = 0 #Hundred Day Price Avg
    price = []
    price100 = []
    price30 = []
    price7 = []

    topTradeVol = 4970000000
    SDTdVA = 0 #Seven Day Trade Volume Avg
    TDTdVA = 0 #Thirty Day Trade Volume Avg
    HDTdVA = 0 #Hundred Day Trade Volume Avg 
    tradeVol = []
    tradeVol100 = []
    tradeVol30 = []
    tradeVol7 = []

    SDTsVA = 0 #Seven Day Transaction Volume Avg
    TDTsVA = 0 #Thirty Day Transaction Volume Avg
    HDTsVA = 0 #Hundred Day Transaction Volume Avg  
    tranVol = [] 
    tranVol100 = [] 
    tranVol30 = [] 
    tranVol7 = [] 

    SDHA = 0 #Seven Day HashRate Avg
    TDHA = 0 #Thirty Day HashRate Avg
    HDHA = 0 #Hundred Day HashRate Avg 
    hashRate = []
    hashRate100 = []
    hashRate30 = []
    hashRate7 = []
    

    print("price,balance,btc,action,netBalance")
    data = pd.read_csv('AllData.csv') 

    for p in data['Price']:
        price.append(p)

    for tdv in data['Trade Volume']:
        tradeVol.append(tdv)
    
    for tnv in data['Transactions Volume']:
        tranVol.append(tnv)
    
    for has in data['Hash Rate']:
        hashRate.append(has)

    for i in range(len(price)):
        price100.append(price[i])
        price30.append(price[i])
        price7.append(price[i])

        tradeVol100.append(tradeVol[i])
        tradeVol30.append(tradeVol[i])
        tradeVol7.append(tradeVol[i])

        hashRate100.append(hashRate[i])
        hashRate30.append(hashRate[i])
        hashRate7.append(hashRate[i])

        tranVol100.append(tranVol[i])
        tranVol30.append(tranVol[i])
        tranVol7.append(tranVol[i])
        if i > 10:  
            SDPA = sevenDayAvg(price7) #Seven Day Price Avg 
        
        if i > 35: 
            TDPA = thirtyDayAvg(price30) #Thirty Day Price Avg
        if i > 110: 
            HDPA = hundredDayAvg(price100) #Hundred Day Price Avg
       
        if i > 10: 
            SDTdVA = sevenDayAvg(tradeVol7)#Seven Day Trade Volume Avg
        if i > 35: 
            TDTdVA = thirtyDayAvg(tradeVol30) #Thirty Day Trade Volume Avg
        if i > 110: 
            HDTdVA = hundredDayAvg(tradeVol100) #Hundred Day Trade Volume Avg 
        

        if i > 10: 
            SDTsVA = sevenDayAvg(tranVol7) #Seven Day Transaction Volume Avg
        if i > 35: 
            TDTsVA = thirtyDayAvg(tranVol30) #Thirty Day Transaction Volume Avg
        if i > 110: 
            HDTsVA = hundredDayAvg(tradeVol100) #Hundred Day Transaction Volume Avg  
        
        if i > 10: 
            SDHA = sevenDayAvg(hashRate7)#Seven Day HashRate Avg
        
        if i > 35: 
            TDHA = thirtyDayAvg(hashRate30) #Thirty Day HashRate Avg
        
        if i > 110: 
            HDHA = hundredDayAvg(hashRate100) #Hundred Day HashRate Avg 
        
        w = 0  # general weight
        if HDPA > price[i] & i > 110:
            w += 0.1
        else: 
            w -= 0.1

        if TDPA > price[i] & i > 35:
            w += 0.2
        else: 
            w -= 0.2

        if SDPA > price[i] & i > 10:
            w += 0.3
        else: 
            w -= 0.3
        

        if HDTdVA < price[i] & i > 110:
            w += 0.05
        else: 
            w -= 0.05

        if TDTdVA < price[i] & i > 35:
            w += 0.1
        else: 
            w -= 0.1

        if SDTdVA < price[i] & i > 10:
            w += 0.2
        else: 
            w -= 0.2
        

        if HDTsVA < price[i] & i > 110:
            w += 0.1
        else: 
            w -= 0.1

        if TDTsVA < price[i] & i > 35:
            w += 0.15
        else: 
            w -= 0.15

        if SDTsVA < price[i] & i > 10:
            w += 0.2
        else: 
            w -= 0.2


        if HDHA > price[i] & i > 110:
            w += 0.1
        else: 
            w -= 0.1

        if TDHA> price[i] & i > 35:
            w += 0.1
        else: 
            w -= 0.1

        if SDHA > price[i] & i > 7:
            w += 0.1
        else: 
            w -= 0.1
        
        action = weight(w)
        if action == 0: # None 
            netBal = btc*price[i]
            netBal += balance
            print(f"{price[i]},{balance},{btc},None,{netBal}")
        if action == 1: #you wont be able to buy anything on turn 1
            btc = buy(price[i], balance, btc)
            balance = 0
            netBal = btc*price[i]
            netBal += balance
            print(f"{price[i]},{balance},{btc},Buy,{netBal}")
        if action == 2:
            balance = sell(price[i], balance, btc)
            btc = 0
            netBal = balance
            print(f"{price[i]},{balance},{btc},Sell,{netBal}")
    
   # print(price, tradeVol, tranVol, hashRate)
   
