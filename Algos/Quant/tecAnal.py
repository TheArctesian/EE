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

    print(array)
    SDA = calAvg(array) # Seven Day avg

    return SDA
def tester():
    Tprice7 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
    T2price7 = [1,1,1,1]
    T1 = thirtyDayAvg(Tprice7)
    T2 = sevenDayAvg(T2price7)
    print(f'{Tprice7} avg is {T1}')
    print(f'{T2price7} avg is {T2}')


if __name__ == "__main__":

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
    
    
    data = pd.read_csv('AllData.csv') 
   # print(data.head())
   
