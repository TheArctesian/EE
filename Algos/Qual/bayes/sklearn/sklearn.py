import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from coalas import csvReader as c
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

# df = pd.read_csv('lemma copy.csv')
def vect(X):
    features = vectorizer.fit_transform(X)
    features_nd = features.toarray()
    return features_nd

def vecSingle(st):
    v =CountVectorizer()
    v.fit(st)
    vector = v.transform(st)
    fe = vector.toarray()
    return fe

    
def test():
    y_pred = classifer.predict(X_test)
    print(accuracy_score(y_pred, y_test))

def testTrained(pred):
    return accuracy_score(pred,c.trained)
def testBest(pred):
    return accuracy_score(pred,c.Best)
def testWorst(pred):
    return accuracy_score(pred,c.Worst)

def checkWhole(): # idk u come up with a name
    df = pd.read_csv('lemma copy.csv')
    x = df.iloc[:, 0].values.astype('U')
    headl = vect(x)
    pred = classifer.predict(headl) 
    print(f'Trained: {testTrained(pred)}')
    print(f'Best: {testBest(pred)}')
    print(f'Worst: {testWorst(pred)}')

        # This throws error: ValueError: X has 31395 features, but GaussianNB is expecting 2881 features as input.
        # This error just wants less data 1093

def classify():
    d = pd.read_csv('out.csv')
    x = d.iloc[:, 2].values.astype('U')
    for i in x:
        i = [i]
        headl = vect(i)

        pred = classifer.predict(headl) 
        print(f'Best: {testBest(pred)}')
        print(f'Trained: {testTrained(pred)}')

if __name__ == '__main__':
    c.importCSV('lemma copy.csv')
    vectorizer = CountVectorizer(
        analyzer = 'word',
        lowercase = False,
    )
    X = c.lemma
    y = c.Best
    # y = c.trained 
    features_nd = vect(X)
    X_train, X_test, y_train, y_test =train_test_split(features_nd,y,test_size= 0.2, random_state=0)
    sc_X = StandardScaler() 
    # print(X_train)
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.fit_transform(X_test)

    classifer = GaussianNB()
    # classifer = BernoulliNB()
    classifer.fit(X_train, y_train)    
    test()
    checkWhole()
    classify()