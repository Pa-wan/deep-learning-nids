from DataProccess import DataProccess
import numpy as np
import pandas as pd
from sklearn.kernel_approximation import RBFSampler
from sklearn.linear_model import SGDClassifier
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (precision_score, recall_score,f1_score, accuracy_score,mean_squared_error,mean_absolute_error)
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import (precision_score, recall_score,f1_score, accuracy_score,mean_squared_error,mean_absolute_error, roc_curve, classification_report,auc)


# get and proccess data
data = DataProccess()
# x_train, y_train, x_test, y_test, x_test_21, y_test_21 = data.return_proccessed_data_multiclass()
x_train, y_train, x_test, y_test, x_test_21, y_test_21 = data.return_proccessed_data_binary()


# reshape input to be [samples, timesteps, features]
x_train = x_train.reshape(x_train.shape[0], 1, x_train.shape[1])
x_test = x_test.reshape(x_test.shape[0], 1, x_test.shape[1])
x_test_21 = x_test_21.reshape(x_test_21.shape[0], 1, x_test_21.shape[1])

# multiclass
# y_train=np_utils.to_categorical(y_train)
# y_test=np_utils.to_categorical(y_test)
# y_test_21=np_utils.to_categorical(y_test_21)

model = LogisticRegression()
model.fit(x_train, y_train)


# make predictions
expected = y_test
predicted = model.predict(x_test)
np.savetxt('res/predictedLR.txt', predicted, fmt='%01d')
accuracy = accuracy_score(expected, predicted)
recall = recall_score(expected, predicted, average="binary")
precision = precision_score(expected, predicted , average="binary")
f1 = f1_score(expected, predicted , average="binary")
cm = metrics.confusion_matrix(expected, predicted)
print(cm)
tpr = float(cm[0][0])/np.sum(cm[0])
fpr = float(cm[1][1])/np.sum(cm[1])
print("%.3f" %tpr)
print("%.3f" %fpr)
print("Accuracy")
print("%.3f" %accuracy)
print("precision")
print("%.3f" %precision)
print("recall")
print("%.3f" %recall)
print("f-score")
print("%.3f" %f1)
print("fpr")
print("%.3f" %fpr)
print("tpr")
print("%.3f" %tpr)
print("***************************************************************")


# fit a Naive Bayes model to the data
model = GaussianNB()
model.fit(x_train, y_train)
print(model)
# make predictions
expected = y_test
predicted = model.predict(x_test)
np.savetxt('res/predictedNB.txt', predicted, fmt='%01d')
accuracy = accuracy_score(expected, predicted)
recall = recall_score(expected, predicted, average="binary")
precision = precision_score(expected, predicted , average="binary")
f1 = f1_score(expected, predicted , average="binary")
cm = metrics.confusion_matrix(expected, predicted)
print(cm)
tpr = float(cm[0][0])/np.sum(cm[0])
fpr = float(cm[1][1])/np.sum(cm[1])
print("%.3f" %tpr)
print("%.3f" %fpr)
print("Accuracy")
print("%.3f" %accuracy)
print("precision")
print("%.3f" %precision)
print("recall")
print("%.3f" %recall)
print("f-score")
print("%.3f" %f1)
print("fpr")
print("%.3f" %fpr)
print("tpr")
print("%.3f" %tpr)
print("***************************************************************")



# fit a k-nearest neighbor model to the data
model = KNeighborsClassifier()
model.fit(x_train, y_train)
print(model)
# make predictions
expected = y_test
predicted = model.predict(x_test)
np.savetxt('res/predictedKNN.txt', predicted, fmt='%01d')
# summarize the fit of the model
accuracy = accuracy_score(expected, predicted)
recall = recall_score(expected, predicted, average="binary")
precision = precision_score(expected, predicted , average="binary")
f1 = f1_score(expected, predicted , average="binary")

cm = metrics.confusion_matrix(expected, predicted)
print(cm)
tpr = float(cm[0][0])/np.sum(cm[0])
fpr = float(cm[1][1])/np.sum(cm[1])
print("%.3f" %tpr)
print("%.3f" %fpr)
print("Accuracy")
print("%.3f" %accuracy)
print("precision")
print("%.3f" %precision)
print("recall")
print("%.3f" %recall)
print("f-score")
print("%.3f" %f1)
print("fpr")
print("%.3f" %fpr)
print("tpr")
print("%.3f" %tpr)
print("***************************************************************")



model = DecisionTreeClassifier()
model.fit(x_train, y_train)
print(model)
# make predictions
expected = y_test
predicted = model.predict(x_test)
np.savetxt('res/predictedDT.txt', predicted, fmt='%01d')
# summarize the fit of the model
accuracy = accuracy_score(expected, predicted)
recall = recall_score(expected, predicted, average="binary")
precision = precision_score(expected, predicted , average="binary")
f1 = f1_score(expected, predicted , average="binary")

cm = metrics.confusion_matrix(expected, predicted)
print(cm)
tpr = float(cm[0][0])/np.sum(cm[0])
fpr = float(cm[1][1])/np.sum(cm[1])
print("%.3f" %tpr)
print("%.3f" %fpr)
print("Accuracy")
print("%.3f" %accuracy)
print("precision")
print("%.3f" %precision)
print("recall")
print("%.3f" %recall)
print("f-score")
print("%.3f" %f1)
print("fpr")
print("%.3f" %fpr)
print("tpr")
print("%.3f" %tpr)
print("***************************************************************")






model = AdaBoostClassifier(n_estimators=100)
model.fit(x_train, y_train)

# make predictions
expected = y_test
predicted = model.predict(x_test)
np.savetxt('res/predictedABoost.txt', predicted, fmt='%01d')
# summarize the fit of the model
accuracy = accuracy_score(expected, predicted)
recall = recall_score(expected, predicted, average="binary")
precision = precision_score(expected, predicted , average="binary")
f1 = f1_score(expected, predicted , average="binary")

cm = metrics.confusion_matrix(expected, predicted)
print(cm)
tpr = float(cm[0][0])/np.sum(cm[0])
fpr = float(cm[1][1])/np.sum(cm[1])
print("%.3f" %tpr)
print("%.3f" %fpr)
print("Accuracy")
print("%.3f" %accuracy)
print("precision")
print("%.3f" %precision)
print("recall")
print("%.3f" %recall)
print("f-score")
print("%.3f" %f1)
print("fpr")
print("%.3f" %fpr)
print("tpr")
print("%.3f" %tpr)
print("***************************************************************")




model = RandomForestClassifier(n_estimators=100)
model = model.fit(x_train, y_train)

# make predictions
expected = y_test
predicted = model.predict(x_test)
np.savetxt('res/predictedRF.txt', predicted, fmt='%01d')
# summarize the fit of the model
accuracy = accuracy_score(expected, predicted)
recall = recall_score(expected, predicted, average="binary")
precision = precision_score(expected, predicted , average="binary")
f1 = f1_score(expected, predicted , average="binary")

cm = metrics.confusion_matrix(expected, predicted)
print(cm)
tpr = float(cm[0][0])/np.sum(cm[0])
fpr = float(cm[1][1])/np.sum(cm[1])
print("%.3f" %tpr)
print("%.3f" %fpr)
print("Accuracy")
print("%.3f" %accuracy)
print("precision")
print("%.3f" %precision)
print("recall")
print("%.3f" %recall)
print("f-score")
print("%.3f" %f1)
print("fpr")
print("%.3f" %fpr)
print("tpr")
print("%.3f" %tpr)
print("***************************************************************")



tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

scores = ['precision', 'recall']
X_train = x_train
y_train = y_train
X_test = x_test
y_test = y_test

for score in scores:
    print("# Tuning hyper-parameters for %s" % score)
    print()
    clf = GridSearchCV(SVC(C=1), tuned_parameters, cv=5,
                       scoring='%s_macro' % score)
    clf.fit(X_train, y_train)

    print("Best parameters set found on development set:")
    print()
    print(clf.best_params_)
    print()
    print("Grid scores on development set:")
    print()
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r"
              % (mean, std * 2, params))
    print("----------------------------------------------")
    print("cross-validation accuracy of train data set")
    print(means)
    
    print("----------------------------------------------")
    print()

    print("Detailed classification report:")
    print()
    print("The model is trained on the full development set.")
    print("The scores are computed on the full evaluation set.")
    print()
    y_true, y_pred = y_test, clf.predict(X_test)
    #print("accuracy score")
    #print(accuracy_score(y_true, y_pred))
    print("confusion matrix")
    print(confusion_matrix(y_true, y_pred))
    print("Classification report")
    print(classification_report(y_true, y_pred))
    print()
    print("***************************************************************************")
    print("for now")
    print("accuracy score")
    print(accuracy_score(y_true, y_pred))
    print("precision")
    print(precision_score(y_true, y_pred , average="binary"))
    print("recall")
    print(recall_score(y_true, y_pred , average="binary"))
    print("F-score")
    print(f1_score(y_true, y_pred , average="binary"))
    print("best parameters")
    print(clf.best_params_)
    print("***************************************************************************")
    predicted = y_pred
    expected = y_true
    cm = metrics.confusion_matrix(expected, predicted)
    print("==============================================")
    print(cm)
    tpr = float(cm[0][0])/np.sum(cm[0])
    fpr = float(cm[1][1])/np.sum(cm[1])
    print("%.3f" %tpr)
    print("%.3f" %fpr)