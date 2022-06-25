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
    
def hundredDayAvg():
    return HDPA

def thirtyDayAvg():
    return TDPA

def sevenDayAvg():
    return SDPA

if __name__ == "__main__":

    topPrice = 19280
    SDPA = 0 #Seven Day Price Avg 
    TDPA = 0 #Thirty Day Price Avg
    HDPA = 0 #Hundred Day Price Avg
    price = []

    SDTdVA = 0 #Seven Day Trade Volume Avg
    TDTdVA = 0 #Thirty Day Trade Volume Avg
    HDTdVA = 0 #Hundred Day Trade Volume Avg 
    tradeVol = []

    SDTsVA = 0 #Seven Day Transaction Volume Avg
    TDTsVA = 0 #Thirty Day Transaction Volume Avg
    HDTsVA = 0 #Hundred Day Transaction Volume Avg  
    tranVol = [] 

    SDHA = 0 #Seven Day HashRate Avg
    TDHA = 0 #Thirty Day HashRate Avg
    HDHA = 0 #Hundred Day HashRate Avg 
    hashRate = []
    

    data = pd.read_csv('AllData.csv') 
    print(data.head())
   
