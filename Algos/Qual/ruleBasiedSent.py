import logging
from matplotlib.pyplot import polar
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from textblob import TextBlob
from nltk.stem import WordNetLemmatizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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

analyzer = SentimentIntensityAnalyzer()
wordnet_lemmatizer = WordNetLemmatizer()
# NLTK defs
stop_words = set(stopwords.words('english'))
pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}
# data


# data format
# headlines['Headline'] = headlines['Headline'].str.strip().str.lower()

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

def lemmatize(pos_data):
    lemma_rew = " "
    for word, pos in pos_data:
        if not pos:
            lemma = word
            lemma_rew = lemma_rew + " " + lemma
        else:
            lemma = wordnet_lemmatizer.lemmatize(word, pos=pos)
            lemma_rew = lemma_rew + " " + lemma
    return lemma_rew

def getPolarity(review):
    return TextBlob(review).sentiment.polarity

def vader(review):
    vs = analyzer.polarity_scores(review)
    return vs


def getSubjectivity(review):
    return TextBlob(review).sentiment.subjectivity
if __name__ == "__main__":
    # Read 
    # headlines = pd.read_csv('news.csv')
    # price = pd.read_csv('price.csv')
    text = 'Bitcoin Miners, Join Investors on Selling Spree '
    text = clean(text)
    print(text)
    text = tokenize(text)
    print(text)
    text = [word for word in text if not word in stop_words]
    print(text)
    tag = tagTokens(text)
    print(tag)
    stem = stem(tag)
    print(stem)
    lema = lemmatize(stem)
    print(lema) 
    polarity = getPolarity(lema)
    polarVader = vader(lema)
    subjectivity = getSubjectivity(lema)
    print(f'{lema} is Polar: {polarity} Sub: {subjectivity}')
    print(f'{lema} is {polarVader} and {subjectivity} subjective')
    # Clean
    # headlines['Headline'] = headlines['Headline'].apply(clean)

    # tokenize, clean stop words, tag
    #for text in headlines['Headline']:
    #    text = tokenize(text)
    #    text = [word for word in text if not word in stop_words]
    #    lemma = " ".join(text)

    #    polarity = getPolarity(lemma)
    #    subjectivity = getSubjectivity(lemma)
    #    print(f'{lemma} is Polar: {polarity} Sub: {subjectivity}')
        # text = tagTokens(text)
        # Stemming
        # newList = stem(text)

        # tokenized = tokenize(text)
        # print(tokenized)