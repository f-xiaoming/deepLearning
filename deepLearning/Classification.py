from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import BaggingClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import  train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

import pandas as pd


df = pd.read_csv("F:\\test2.csv", index_col=0)

df = df.astype("int64")
df.type.value_counts()
df.shape
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 1:841], df['type'], test_size=0.20, random_state=42)
gnb = GaussianNB()

gnb.fit(X_train, y_train)

pred = gnb.predict(X_test)
accuracy = accuracy_score(pred, y_test)
print("native_bayes")
print(accuracy)
print(classification_report(pred, y_test, labels=None))

for i in range(3, 15, 3):
    neigh = KNeighborsClassifier(n_neighbors=i)
    neigh.fit(X_train, y_train)
    pred = neigh.predict(X_test)
    accuracy = accuracy_score(pred, y_test)
    print("kneighbors{}".format(i))
    print(accuracy)
    print(classification_report(pred, y_test, labels=None))
    print("")
