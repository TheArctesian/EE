import logging
from operator import indexOf
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
    pol = TextBlob(review).sentiment.polarity
    if pol == 0:
        return 0
    if pol < 0:
        return -1
    if pol > 0:
        return 1


def vader(review):
    vs = analyzer.polarity_scores(review)
    
    if vs['compound'] >= 0.05 :
        return 1
 
    elif vs['compound'] <= - 0.05 :
        return -1
 
    else :
        return 0

def test():
    text = 'very bad man '
    text = clean(text)
    print(text)
    text = tokenize(text)
    print(text)
    text = [word for word in text if not word in stop_words]
    print(text)
    text = tagTokens(text)
    print(text)
    text = stem(text)
    print(text)
    text  = lemmatize(text)
    print(text)
    polarity = getPolarity(text)
    polarVader = vader(text)
    subjectivity = getSubjectivity(text)
    print(f'{text} is Polar: {polarity} Sub: {subjectivity}')
    print(f'{text} is {polarVader} and {subjectivity} subjective')

def getSubjectivity(review):
    return TextBlob(review).sentiment.subjectivity



if __name__ == "__main__":
    # Read 
    # data = pd.read_csv('news.csv')
    # Clean
    # tokenize, clean stop words, tag
    # for text in data['Headline']: 
        # text = clean(text)
        # text = tokenize(text)
        # text = [word for word in text if not word in stop_words]
        # print(text)
        # tagged = tagTokens(text)
        # stemd = stem(tagged)
        # lemma = lemmatize(stemd)

        # polarity = getPolarity(lemma)
        # print(polarity) 
        #data = pd.DataFrame([[indexOf(text)]])

    #    polarity = getPolarity(lemma)
    #    subjectivity = getSubjectivity(lemma)
    #    print(f'{lemma} is Polar: {polarity} Sub: {subjectivity}')
        # text = tagTokens(text)
        # Stemming
        # newList = stem(text)

        # tokenized = tokenize(text)
        # print(tokenized)
       #  data.to_csv("news.csv", mode="a")
