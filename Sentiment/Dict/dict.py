from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from coalas import csvReader as c
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
import time
analyzer = SentimentIntensityAnalyzer()
wordnet_lemmatizer = WordNetLemmatizer()
# NLTK defs
stop_words = set(stopwords.words('english'))
pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}
# data

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

positive = ['soar',
            'bull',
            'rise',
            'skyrocket',
            'bounce',
            'rise', 
            'blasts',
            'boom',
            'high',
            'alltime'
            'moon',
            'halving',
            'record',
            'accepts',
            'buy',
            'embrace',
            'roar',
            'serges',
            'over',
            'recover',
            "wo n't sell",
            'returns',
            'beats',
            'profit',
            'bump',
            ]
negative = ['dip',
            'seizes',
            'illegally',
            'bad',
            'losing',
            'issue',
            'meltdown',
            'dig',
            'climate',
            'slide',
            'selloff',
            'low',
            'fake',
            'fail',
            'worthless',
            'hack',
            'bear',
            'fall',
            'alarm',
            'worst',
            'moon',
            'drop',
            'kill',
            'ponzi',
            'outflows',
            'hit',
            'ban',
            'volatile',
            'regulation',
            'regulate',
            'farce',
            'sell',
            'plunge',
            'rough',
            'struggle',
            'pain',
            'cut',
            'illusion',
            'tumble',
            'loss',
            'rejects',
            'risk',
            'worth nothing',
            'crash',
            'scam',
            'bubble',
            'burst',
            'slow',
            'troll',
            'hack',
            'tumbles',
            'trouble',
            'criminal'
            'anti',
            'dodging',
            'dodgers',
            'doges',
            'bans',
            'kill',
            "fool 's gold"
            ]
neutral = [ 
        "learn",
        "class",
        'roller',
        'frequent',
        'explain',
        'proof',
        'stock',
        'basic',
        'common',
        'beginner',
        'basic',
        'top'
        ]

# NLTK defs
stop_words = set(stopwords.words('english'))
pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}
# data


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

def lemma(text):
    text = tokenize(text)
    text = [word for word in text if not word in stop_words]
    lemma = " ".join(text)
    lemma = lemma.lower()
    return lemma
def checkNeu(string):
    x = string.split()
    score = 0
    for text in x:
        if text in neutral:
            score+=1
    return score

def checkNeg(string):
    x = string.split()
    score = 0
    for text in x:
        if text in negative:
            score+=1
    return score

def checkPos(string):
    x = string.split()
    score = 0
    for text in x:
        if text in positive:
            score+=1
    return score


def calAction(Pos,Neg,Neu):
    print(f'{Pos},{Neg},{Neu}')
    if Pos > Neg and Pos > Neu:
        return "Buy"
    if Neg > Pos and Neg > Neu:
        return "Sell"
    if Neu > Pos and Neu > Neg: 
        return "Hold"
    return "Hold"

def calActionB(Pos,Neg,Neu):
    if Pos > Neg and Pos > Neu:
        return 1
    if Neg > Pos and Neg > Neu:
        return -1
    if Neu > Pos and Neu > Neg: 
        return 0
    return 0

def getPolarity(review):
    pol = TextBlob(review).sentiment.polarity
    if pol < 0.2:
        return -1
    if pol > -0.2:
        return 1
    return 0

def vader(review):
    vs = analyzer.polarity_scores(review)
    
    if vs['compound'] >= 0.05 :
        return 1
 
    elif vs['compound'] <= - 0.05 :
        return -1
 
    else :
        return 0

if __name__ == "__main__":
    start = time.time()
    c.importData("../trained.csv")
    c.addCol('Lemma')
    c.addCol('TextBlobPol')
    c.addCol('VaderPol')
    c.addCol('DictPol')
    # c.addCol('DictPos')
    # c.addCol('DictNeg')
    # c.addCol('DictNeu')
    c.addCol('DictAction')
    c.printHeaders()
    for i in range(len(c.headline)):
        text = lemma(c.headline[i])
        c.Lemma.append(text)
    for i in range(len(c.headline)):
        pos =checkPos(c.Lemma[i])
        neg =checkNeg(c.Lemma[i])
        neu =checkNeu(c.Lemma[i])
        # action = calAction(pos,neg,neu)
        blob = getPolarity(c.Lemma[i])
        vad = vader(c.Lemma[i])
        actionB = calActionB(pos,neg,neu)
        c.DictPol.append(actionB)
        c.TextBlobPol.append(blob) 
        c.VaderPol.append(vad)
        # c.DictPos.append(pos)
        # c.DictNeg.append(neg)
        # c.DictNeu.append(neu)
        # c.DictAction.append(action)
    
    c.writeCSV("comp.csv")
    print("--- %s sec ---" % (time.time() - start))
"""
stop
CRYPTOVERSE
Satoshi Nakaboto:
LIVE MARKETS 
This Week's Top Bitcoin and Crypto News: 
This Week's Top Bitcoin and Crypto News - CNET
- CNBC Television
- Reuters
– Bitcoin News - Bitcoin News
"""
