from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from coalas import csv as c

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
            'moon',
            'halving',
            'record',
            'accepts',
            'buy',
            'embrace',
            'roar',
            'recover',
            "wo n't sell",
            ]
negative = ['dip',
            'issue',
            'meltdown',
            'high',
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
            'scam',
            'bubble',
            'burst',
            "fool 's gold"
            ]
neutral = [ 
        "learn",
        "class",
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



def checkN(string):
    print(neutral)
if __name__ == "__main__":
        #c.importData("../trained.csv")
        #c.printHeaders()
        #c.printAll()

    for text in negative:
        text = tokenize(text)
        text = [word for word in text if not word in stop_words]
        lemma = " ".join(text)
        print(lemma)
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
