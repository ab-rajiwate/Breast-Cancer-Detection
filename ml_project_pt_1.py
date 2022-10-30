import numpy as np
import pandas as pd

"""#Importing Data"""

dataset = pd.read_csv('breast_cancer.csv')

"""# Data Pre- Processing"""

#dataset.isnull().any()

x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

"""# Splitting the dataset intro Training and Test Set"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

"""#Training the SVM Model"""

from sklearn.svm import SVC
classifier = SVC( kernel = 'rbf' , random_state = 0, probability=True)
classifier.fit(x_train,y_train)

"""#Testing Phase

##Predicting the values
"""

y_pred = classifier.predict(x_test)

"""##Getting the accuracy of the predicted values"""

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)

print(f'\nTrue Positive [Is 4 and Predicted 4]: {cm[1][1]}')
print(f'True Negative [Is 2 and Predicted 2]: {cm[0][0]}')
print(f'False Positive [Is 2 and Predicted 4]: {cm[0][1]}')
print(f'False Negative [Is 4 and Predicted 2]: {cm[1][0]}') # This is very dangerous so this value must be kept at minimal


#      2   4 -->P  
# 2 [ [TN  FP]
# 4   [FN! TP]  ]
# A

precision = cm[1][1]/(cm[1][1]+cm[0][1])
recall = cm[1][1]/(cm[1][1]+cm[1][0])


f1 = 2 * (precision*recall)/(precision+recall)
print(f"\nThe F1 score is: {f1:{0}.{2}}")
print(f"\nThe Accuracy is: {accuracy_score(y_test, y_pred)*100:{0}.{4}} %")

"""**Linear Kernel**

F1 Score = 0.94

Accuracy = 95.62%
* True Positive  : 48 
* True Negative  : 83
* False Positive : 4 
* False Negative : 2 --->*Danger is Low*


---
**Sigmoid Kernel** WORST

F1 Score = nan

Accuracy = 47.45%
* True Positive  : 0 
* True Negative  : 65
* False Positive : 22 
* False Negative : 50 --->*Danger is very High*


---
**RBF Kernel** BEST

F1 Score = 0.95

Accuracy = 96.35%
* True Positive  : 49
* True Negative  : 83
* False Positive : 4
* False Negative : 1 --> *Danger is lowest*


---
**Poly Kernel**

F1 Score = 0.95

Accuracy =  96.35%
* True Positive  : 48
* True Negative  : 84
* False Positive : 3
* False Negative : 2


---


"""

#import random
#a = classifier.predict_proba([[random.randint(1,10)]*9])
#if a[0][0] <= a[0][1]:
#  print(f'Positive\n\t Benign: {a[0][0]*100:{0}.{4}}\n\t Melignant: {a[0][1]*100:{0}.{4}}')
#else:
#  print(f'Negative\n\t Benign: {a[0][0]*100:{0}.{4}}\n\t Melignant: {a[0][1]*100:{0}.{4}}')

"""#Saving the trained Model"""

import joblib
joblib.dump(classifier , 'SVM_Classifier.pkl')

