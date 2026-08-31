import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier 
from sklearn.ensemble import VotingClassifier

#---------------------------------
#Step1:Load the dataset
#---------------------------------

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print("shape of datset:",df.shape)

print("First few records:")
print(df.head())

#---------------------------------
#Step2:check for missing values
#---------------------------------
print("Missing values:")
print(df.isnull().sum())

#---------------------------------
#Step3:separate features and lables
#---------------------------------

X = df.drop("Fraud",axis=1)
Y = df["Fraud"]

print("X shape:",X.shape)
print("Y shape:",Y.shape)

#---------------------------------
#Step3:split datstet
#---------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#---------------------------------
#Step4:scaling the features
#---------------------------------

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

#---------------------------------
#Step5.1:create the individual models
#---------------------------------
model_det = DecisionTreeClassifier(random_state=42)
model_bag = BaggingClassifier(random_state=42)
model_ran = RandomForestClassifier(random_state=42)
model_ada = AdaBoostClassifier(random_state=42)
model_vot = VotingClassifier(estimators=[
    ('decision_tree',model_det),
    ('bagging',model_bag),
    ('random_forest',model_ran),
    ('adaboost',model_ada)
    ], voting='hard') 


#---------------------------------
#Step6:Train individual models
#---------------------------------
model_det = model_det.fit(X_train,Y_train)
model_bag = model_bag.fit(X_train,Y_train)
model_ran = model_ran.fit(X_train,Y_train)
model_ada = model_ada.fit(X_train,Y_train)
model_vot = model_vot.fit(X_train,Y_train)

#---------------------------------
#step7: Test the models
#---------------------------------
Y_pred_det = model_det.predict(X_test)
Y_pred_bag = model_bag.predict(X_test)
Y_pred_ran = model_ran.predict(X_test)
Y_pred_ada = model_ada.predict(X_test)
Y_pred_vot = model_vot.predict(X_test)

#---------------------------------
#step8:Evaluate the models
#---------------------------------

print("Accuracy of decision tree model:",accuracy_score(Y_test,Y_pred_det))
print("precision:",precision_score(Y_test,Y_pred_det))
print("recall:",recall_score(Y_test,Y_pred_det))
print("F1:",f1_score(Y_test,Y_pred_det))
print("------------------------------------------------------")

print("Accuracy of Bagging model:",accuracy_score(Y_test,Y_pred_bag))
print("precision:",precision_score(Y_test,Y_pred_bag))
print("recall:",recall_score(Y_test,Y_pred_bag))
print("F1:",f1_score(Y_test,Y_pred_bag))
print("------------------------------------------------------")

print("Accuracy of random forest:",accuracy_score(Y_test,Y_pred_ran))
print("precision:",precision_score(Y_test,Y_pred_ran))
print("recall:",recall_score(Y_test,Y_pred_ran))
print("F1:",f1_score(Y_test,Y_pred_ran))
print("------------------------------------------------------")

print("Accuracy of adaboost model:",accuracy_score(Y_test,Y_pred_ada))
print("precision:",precision_score(Y_test,Y_pred_ada))
print("recall:",recall_score(Y_test,Y_pred_ada))
print("F1:",f1_score(Y_test,Y_pred_ada))
print("------------------------------------------------------")

print("Accuracy of voting classifier :",accuracy_score(Y_test,Y_pred_vot))
print("precision:",precision_score(Y_test,Y_pred_vot))
print("recall:",recall_score(Y_test,Y_pred_vot))
print("F1:",f1_score(Y_test,Y_pred_vot))
print("------------------------------------------------------")


