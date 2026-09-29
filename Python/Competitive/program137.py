# [Age, Monthly Charges, Tenure, Complaints, Support Calls]
#0 = Customer will stay
#1 = Customer will leave

from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

#----------------------------------------------------
# 1.create dataset
#----------------------------------------------------
X = pd.DataFrame([
[25, 500, 12, 1, 2],
[30, 700, 24, 0, 1],
[45, 1200, 6, 5, 8],
[50, 1500, 5, 6, 10],
[28, 600, 18, 1, 1],
[35, 800, 30, 0, 0],
[48, 1400, 4, 7, 9],
[52, 1600, 3, 8, 12],
[27, 550, 20, 0, 1],
[42, 1300, 8, 4, 7]
])

Y = pd.Series([
0, 0, 1, 1, 0,
0, 1, 1, 0, 1
])

#----------------------------------------------------
#2.split the dataset
#----------------------------------------------------
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#----------------------------------------------------
#3.scaling
#----------------------------------------------------
scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

#----------------------------------------------------
#4.model train
#----------------------------------------------------

model = MLPClassifier(hidden_layer_sizes=(8,4),
                      activation='relu',
                      max_iter=1000,
                      random_state=42)

model = model.fit(X_train_scaled,Y_train)

#----------------------------------------------------
#5.evaluate model
#----------------------------------------------------

Y_pred = model.predict(X_test_scaled)

print("actual values:",Y_test)
print("predicted values:",Y_pred)

#----------------------------------------------------
#6. calculate accuracy
#----------------------------------------------------

accuracy = accuracy_score(Y_test,Y_pred)
print("accuracy:",accuracy)

#----------------------------------------------------
#7.test input
#----------------------------------------------------
new_customer = pd.DataFrame([[46, 1450, 5, 6, 9]])
new_customer_scaled = scalar.transform(new_customer)

prediction =model.predict(new_customer_scaled)

if prediction[0] == 0:
    print("customer will stay")

else:
    print("customer will leave")





