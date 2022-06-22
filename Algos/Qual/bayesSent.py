from sklearn.model_selection import train_test_split
import joblib
from sklearn.feature_extraction.text import CountVectorizer
import os
import logging
import pandas as pd
import re

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

# data
headlines = pd.read_csv('news.csv')
price = pd.read_csv('price.csv')

# data format
headlines['Headline'] = headlines['Headline'].str.strip().str.lower()

def clean(text):
    text = str(text)
    text = re.sub('[^A-Za-z]+', ' ', text).lower().strip()
    logger.info(text)
    return text


if __name__ == "__main__":
    # Read 
    headlines = pd.read_csv('news.csv')
    price = pd.read_csv('price.csv')


    # Clean
    headlines['Headline'] = headlines['Headline'].apply(clean)


    # TEXT BLOB 