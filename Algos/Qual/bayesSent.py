import logging
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from textblob import TextBlob
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

# NLTK defs
stop_words = set(stopwords.words('english'))
pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}
# data
headlines = pd.read_csv('news.csv')
price = pd.read_csv('price.csv')

# data format
headlines['Headline'] = headlines['Headline'].str.strip().str.lower()

def clean(text):
    text = str(text)
    text = re.sub('[^A-Za-z]+', ' ', text).lower().strip()
    return text

def tokenize(text):
    text = word_tokenize(text)
    return text

def tagTokens(text):
    text = pos_tag(text)
    return text 

def stem(text):
    newList = []
    for word, tag in text:
            if word not in set(stopwords.words('english')):
                newList.append(tuple([word, pos_dict.get(tag[0])])) 
    return newList

def train():



if __name__ == "__main__":
    # Read 
    headlines = pd.read_csv('news.csv')
    price = pd.read_csv('price.csv')

    # Clean
    headlines['Headline'] = headlines['Headline'].apply(clean)

    # tokenize, clean stop words, tag
    for text in headlines['Headline']:
        text = tokenize(text)
        text = [word for word in text if not word in stop_words]
        lemma = " ".join(text)

        polarity = getPolarity(lemma)
        subjectivity = getSubjectivity(lemma)
        print(f'{lemma} is Polar: {polarity} Sub: {subjectivity}')
        # text = tagTokens(text)
        # Stemming
        # newList = stem(text)

        # tokenized = tokenize(text)
        # print(tokenized)