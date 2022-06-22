import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
from sklearn.feature_extraction.text import CountVectorizer
import os
import logging

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


def readData():
    headlines = pd.read_csv('news.csv')
    price = pd.read_csv('price.csv')
    logging.info(price.head())
    headlines.head()


if __name__ == "__main__":
    readData()
    
