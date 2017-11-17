

import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report




data=pd.read_csv('banking.csv', header=0)

data.drop(data.columns[[0,3,7,8,9,10,11,12,13,15,16,17,18,19]],axis=1,inplace=True)

data.head()

data2=pd.get_dummies(data, columns=['job','marital','default','housing','loan','poutcome'])


data2.head()

x=data2.iloc[:,1:]

y=data2.iloc[:,0]

x_train, x_test, y_train, y_test = train_test_split(x,y, random_state=0)

x_train.shape

x_test.shape

y_train.shape

y_test.shape

classifier = LogisticRegression(random_state=0)

classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)

confusion_matrix = confusion_matrix(y_test,y_pred)

print (confusion_matrix)




classifier.score(x_test,y_test)

print(classification_report(y_test,y_pred))

