import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from coalas import csvReader as c
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('lemma copy.csv')
c.importCSV('lemma copy.csv')
vectorizer = CountVectorizer(
    analyzer = 'word',
    lowercase = False,
)

# X = df.iloc[:, 0].values
# y = df.iloc[:, 1].values
X = c.lemma
# y = c.Best
y = c.trained
# count_vec = CountVectorizer(ngram_range=(
    # 1, 3), stop_words="english").fit(X)
features = vectorizer.fit_transform(X)

features_nd = features.toarray()
# X = count_vec.transform(X)
X_train, X_test, y_train, y_test =train_test_split(features_nd,y,test_size= 0.2, random_state=0)

sc_X = StandardScaler() 
# print(X_train)
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

classifer = GaussianNB()

classifer.fit(X_train, y_train)

# testing the model
y_pred = classifer.predict(X_test)

print(accuracy_score(y_pred, y_test))