import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv('lemma copy.csv')
X = df.iloc[:, 0].values
y = df.iloc[:, 1].values
print(y)

X_train, X_test, y_train, y_test =train_test_split(X,y,test_size= 0.25, random_state=0)

sc_X = StandardScaler() 
print(X_train)
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

classifer = GaussianNB()

classifer.fit(X_train, y_train)

# testing the model
y_pred = classifer.predict(X_test)

print(accuracy_score(y_pred, y_test))